from configparser import ConfigParser
import sqlite3


class Database:
    def __init__(self):
        # 连接数据库
        config = ConfigParser()
        config.read('.config.ini')
        db_path = config.get('Database', 'Path')
        self.database = sqlite3.connect(db_path)
        self.cursor = self.database.cursor()
        # 数据库信息
        self.index = config.get('Setting', 'Index').split(',')
        self.relations = config.get('Setting', 'Relations').split(',')
    
    def query_similar_data(self, id, content):
        self.cursor.execute('select name from %s where name LIKE ?' % self.index[id], ('%%%s%%' % content, ))
        names = self.cursor.fetchall()
        data = self.convert_raw_to_data(names) if names else list()
        return data
        # data是一个列表，表中元素还是列表，代表每行的显示内容
        # 子列表中的元素是该行中每列显示的内容

    def union_query(self, rid, qid, text):
        """
        :param rid: recieve id
        :param qid: query id
        :param text: 匹配文本
        :return: data
        """
        '''
        self.cursor.execute('select id from %s where name = ?' % self.index[rid], (text, ))
        res = self.cursor.fetchone()
        if res:
            id = res[0]
        '''
        if text:
            s = self.index[rid]
            t = self.index[qid]
            a = self.index[min(rid, qid)]
            b = self.index[max(rid, qid)]
            sql = format('select id from %s where name = ?' % self.index[rid])
            self.cursor.execute(sql, (text, ))
            id = self.cursor.fetchall()[0][0]
            if qid == 3:
                sql = format('select name, grams from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
                flag = 1
            else:
                sql = format('select name from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
                flag = 0
            self.cursor.execute(sql, (id, ))
            raw = self.cursor.fetchall()
            return self.convert_raw_to_data(raw, flag)    

    def find_relative_info(self, id, content):
        data_left = self.union_query(id, id-1, content) if 1 <= id <= 3 else 0
        data_right = self.union_query(id, id+1, content) if 0 <= id <= 2 else 0
        data = dict()
        if data_left != 0:
            data[id-1] = data_left
        if data_right != 0:
            data[id+1] = data_right
        return data

    @staticmethod
    def convert_raw_to_data(raw, flag=0):
        # 若flag==1则需要加一列“克”
        lst = list()
        for elem in raw:
            lst.append(list())
            for item in elem:
                lst[-1].append(str(item))
            if flag: lst[-1].append('克')
        return lst

    # 以下为插入操作
    def save_single_item(self, id, name):
        db_name = self.index[id]
        sql = format('insert into %s (name) values ("%s")' % (db_name, name))
        try:
            self.cursor.execute(sql)
            self.database.commit()
            return 0    
        except Exception as e:
            print(e)
            return 1

    # 以下为删除操作
    def delete_single_item(self, id, text):
        sql = format('select id from %s where name = ?' % self.index[id])
        self.cursor.execute(sql, (text, ))
        ori_id = self.cursor.fetchall()[0][0]
        sql = format('delete from %s where name = "%s"' % (self.index[id], text))
        try:
            self.cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            print(e)
            return 1
        if id < 3:
            sql = format('delete from %s_%s where %s_id = %s' % (self.index[id], self.index[id+1], self.index[id], ori_id))
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except Exception as e:
                print(e)
                return 1
        if id > 0:
            sql = format('delete from %s_%s where %s_id = %s' % (self.index[id-1], self.index[id], self.index[id], ori_id))
            try:
                self.cursor.execute(sql)
                self.database.commit()
            except Exception as e:
                print(e)
                return 1
        return 0

    def save_relation(self, dbid, name1, name2):
        db_name = self.relations[dbid]
        front_name = db_name.split("_")[0]
        back_name = db_name.split("_")[-1]
        front_id = int(self.search_data(front_name, "id", name1)[0])
        back_id = int(self.search_data(back_name, "id", name2)[0])
        sql = format('insert into %s (%s_id,%s_id) values (%d, %d)' % (db_name,front_name,back_name,front_id,back_id))
        try:
            self.cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            print(e)
        return 0

    def drop_relation(self, dbid, name1, name2):
        db_name = self.relations[dbid]
        front_name = db_name.split("_")[0]
        back_name = db_name.split("_")[-1]
        front_id = int(self.search_data(front_name, "id", name1)[0])
        back_id = int(self.search_data(back_name, "id", name2)[0])
        sql = format('DELETE FROM %s WHERE %s_id = %d and %s_id = %d' %(db_name, front_name, front_id, back_name, back_id))
        try:
            self.cursor.execute(sql)
            self.database.commit()
        except Exception as e:
            print(e)
        return 0

    def search_data(self, dbname, column, data):
        try:
            sql = 'select ' + column + ' from ' + dbname + " where name = '" + data +"'"
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data[0]
        except Exception as e:
            print(e)


if __name__ == "__main__":
    a = Database()
    b = a.union_query(1,2,'少阳症')