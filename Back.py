from configparser import ConfigParser
import sqlite3


class Backend:
    def __init__(self):
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
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
        if type_ == 0:
            for elem in self.index:
                data.append(self.get_data(elem))
        elif type_ == 1:
            data.append(list())
            for elem in self.index[1:-1]:
                data.append(self.get_data(elem))
            data.append(list())
        return data

    def query_input(self, box_id, content):
        # data = self.union_query(box_id, content)
        self.cursor.execute('select name from %s where name LIKE ?' % self.index[box_id], ('%%%s%%' % content, ))
        names = self.cursor.fetchall()
        data = names if names else None
        return data

    def save_data(self):
        pass

    def query_option(self):
        pass

    def get_relations(self):
        pass

    def match_data(self):
        pass

    def union_query(self, a, b, text):
        """
        :param a:
        :param b:
        :return: data
        """
        self.cursor.execute('select id from %s where name = ?' % self.index[a], (text, ))
        id = self.cursor.fetchone()[0]
        if a + b == 1: db_name = 'illness_symptom'
        elif a + b == 3: db_name = 'illness_anagraph'
        elif a + b == 5: db_name = 'anagraph_medicine'
        else: db_name = ''
        self.cursor.execute('select name from illness inner join illness_symptom on illness.id = illness_symptom.illness_id where symptom_id = ?', (id, ))
        raw = self.cursor.fetchall()
        data = list()
        for elem in raw[0]:
            data.append(elem)
        return data


if __name__ == '__main__':
    test = Backend()
    test.query_input(1, '少')
	
