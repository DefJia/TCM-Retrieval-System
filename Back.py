from configparser import ConfigParser
import sqlite3
#import UI.Wrong
import time

class Backend:
    def __init__(self):
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
        self.relations = config.get('Setting', 'relations').split(',')
        # 读取配置文件
        db_path = config.get('Environment', 'database_path')
        self.database = sqlite3.connect(db_path)
        self.cursor = self.database.cursor()
        # 连接数据库

    def get_data(self, field_name, column = "name"):
        """
        :param field_name: str/int 字段名称（可填序号或名称）
        :return: list 相关字段数据列表
        """
        if type(field_name) == int and 0 <= field_name <= 3:
            field_name = self.index[field_name]
        if type(field_name) == str and field_name in self.index:
            sql = 'select ' + column + ' from ' + field_name
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        else:
            return []

    def init(self, type_):
        # 初始化界面数据
        data = list()
        type_ = 0
        # 突然觉得任何模式都应该显示所有信息
        if type_ == 0:
            for elem in self.index:
                data.append(self.get_data(elem))
        elif type_ == 1:
            data.append(list())
            for elem in self.index[1:-1]:
                data.append(self.get_data(elem))
            data.append(list())
        return data

    def query_similar_data(self, box_id, content):
        self.cursor.execute('select name from %s where name LIKE ?' % self.index[box_id], ('%%%s%%' % content, ))
        names = self.cursor.fetchall()
        data = self.convert_raw_to_data(names) if names else list()
        return data


    def union_query(self, box_id, index, text):
        """
        :param box_id: 输入的id
        :param index: 查询的id
        :param text: 匹配文本
        :return: data
        """
        self.cursor.execute('select id from %s where name = ?' % self.index[box_id], (text, ))
        # 先查询关系号
        res = self.cursor.fetchone()
        if res:
            id = res[0]
            # db_name = self.relations[int((box_id + index - 1) / 2)]
            t = self.index[index]
            s = self.index[box_id]
            a = self.index[min(index, box_id)]
            b = self.index[max(index, box_id)]
            sql = format('select name from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            if 'medicine' in (a, b):
                sql = format('select name, grams from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            self.cursor.execute(sql, (id, ))
            raw = self.cursor.fetchall()
            return self.convert_raw_to_data(raw)

    def iq_inquire(self, name, phone, idcard):
        try:
            sqlname = 'select * from history where name = ?'
            sqlphone = 'select * from history where phone = %s'
            sqlidcard = 'select * from history where idcard = %s'

            if name and phone =='' and idcard =='':
                print (sqlname +'(name)')
               # ('select id from patient where %s = ?' % column, (text,))
                self.cursor.execute(sqlname +' (name)')
            elif name =='' and phone and idcard =='':
                self.cursor.execute(sqlphone % name)
            elif name =='' and phone =='' and idcard:
                self.cursor.execute(sqlphone % name)
            elif name and phone and idcard =='':
                'select * from'+ sqlname + 'where phone' + phone
            elif name and phone  == '' and idcard:
                'select * from' + sqlname + 'where idcard' + idcard
            elif name == '' and phone  and idcard:
                'select * from' + sqlphone + 'where idcard' + idcard
            elif name and phone and idcard:
                'select* from select * from' + sqlphone + 'where idcard' + idcard  +'where name ='+ name
            #self.cursor.execute(  )
            data = self.cursor.fetchall()
            return data

        except Exception as e:
            print(e)
        pass

    def save_data(self, db_name, name):
        sql = format('insert into %s (name) values ("%s")' % (db_name, name))
        try:
            self.cursor.execute(sql)
            self.database.commit()

            return 0
        except sqlite3.IntegrityError:
            return 1

    def i_save_data(self,name,gender,age,phone,
                    identitynum,address,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom):

        if phone == "" and identitynum == "":
            #UI.Wrong.show()#不知道行不行
            print("wrong")
        else:
            if identitynum =="":
                identitynum.settext(000000000000000000)
                # 这里有错
                id = '000000000000000000' + phone

            else:
                id =identitynum + phone
                inquirydate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
                print(id)
            sql1 = format('insert into patient (name,gender,age,phone,identitynum,address,id) '
                     'values ("%s","%s","%s","%s","%s","%s","%s")' % (name,gender,age,phone,identitynum,address,id))
            print(sql1)
            sql2 = format('insert into history (id,inquirydate,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom) '
                     'values ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'
                         % (id,inquirydate,look,listen,question,feel,menstruation,leucorrhoea,prescription,mainsymptom))

            try:
                self.cursor.execute(sql1)
                #self.database.commit()
                self.cursor.execute(sql2)
                self.database.commit()
                return id
            #这里如何把ID弄到control里面
            except sqlite3.IntegrityError:
                return 1

    def search_data(self, dbname, column, data):
        try:
            sql = 'select ' + column + ' from ' + dbname + " where name = '" + data +"'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data[0]
        except Exception as e:
            print(e)
    def save_relation(self,dbid,left_data,right_data):
        db_name = self.relations[dbid]
        left_name = db_name.split("_")[0]
        right_name = db_name.split("_")[-1]
        left_id = int(self.search_data(left_name,"id",left_data)[0])
        right_id = int(self.search_data(right_name,"id",right_data)[0])
        sql = format('insert into %s (%s_id,%s_id) values (%s,%s)' % (db_name,left_name,right_name,left_id, right_id))
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return 0
        except Exception as e:
            print(e)

    def drop_relation(self,dbid,left_data,right_data):
        db_name = self.relations[dbid]
        front_name = db_name.split("_")[0]
        back_name = db_name.split("_")[-1]
        front_id = int(self.search_data(front_name, "id", left_data)[0])
        back_id = int(self.search_data(back_name, "id", right_data)[0])
        sql = format(
            'DELETE FROM %s WHERE %s_id = %s and %s_id = %s' %(db_name, front_name, front_id, back_name, back_id)
        )
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return 0
        except Exception as e:
            print(e)
        pass

    def deletedate(self,dbid,text):
        db_name = self.index[dbid]
        id = int(self.search_data(db_name, "id", text)[0])
        sql = format(
            'DELETE FROM %s WHERE id = %s' % (db_name, id)
        )
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return 0
        except Exception as e:
            print(e)
        pass


    def get_relations(self):
        pass

    def match_data(self):
        pass

    @staticmethod
    def convert_raw_to_data(raw):
        tmp = list()
        for elem in raw:
            tmp.append(list())
            for item in elem:
                tmp[-1].append(str(item))
        return tmp
    
    def getPatientID(self,column,text):
        self.cursor.execute('select id from patient where %s = ?' % column, (text, ))
        # 先查询关系号
        patientID = self.cursor.fetchone()
        return patientID[0]
    def get_full_patient_info(self,patientID):
        self.cursor.execute('select name,gender,age,phone,identitynum,address from patient where id = ?' , (patientID, ))
        # 先查询关系号
        data = self.cursor.fetchone()
        name = data[0]
        gender = data[1]
        age = data[2]
        phone = data[3]
        identitynum = data[4] 
        address = data[5]
        return name,gender,age,phone,identitynum,address 


if __name__ == '__main__':
    test = Backend()
    # test.query_similar_data(1, '少')
    test.union_query(1, 0, '少阳症')
