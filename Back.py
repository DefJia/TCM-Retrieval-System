from configparser import ConfigParser
import sqlite3


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

    def get_data(self, field_name):
        """
        :param field_name: str/int 字段名称（可填序号或名称）
        :return: list 相关字段数据列表
        """
        if type(field_name) == int and 0 <= field_name <= 3:
            field_name = self.index[field_name]
        if type(field_name) == str and field_name in self.index:
            sql = 'select name from ' + field_name
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
        data = names if names else None
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
            db_name = self.relations[int((box_id + index - 1) / 2)]
            t = self.index[index]
            s = self.index[box_id]
            a = self.index[min(index, box_id)]
            b = self.index[max(index, box_id)]
            sql = format('select name from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            self.cursor.execute(sql, (id, ))
            raw = self.cursor.fetchall()
            if raw:
                data = list()
                for elem in raw:
                    data.append(elem[0])
                return data

    def save_data(self, db_name, name):
        sql = format('insert into %s (name) values ("%s")' % (db_name, name))
        try:
            self.cursor.execute(sql)
            return 0
        except sqlite3.IntegrityError:
            return 1

    def query_option(self):
        pass

    def get_relations(self):
        pass

    def match_data(self):
        pass


if __name__ == '__main__':
    test = Backend()
    # test.query_similar_data(1, '少')
    test.union_query(1, 0, '少阳症')
	
