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
            sql = 'select * from ' + field_name
            self.cursor.execute(sql)
            data = self.cursor.fetchall()
            return data
        else:
            return []

    def init(self, type_):
        data = list()
        if type_ == 0:
            for elem in self.index:
                data.append(self.get_data(elem))
        elif type_ == 1:
            for elem in self.index[1:-1]:
                data.append(self.get_data(elem))
        return data

    def query(self, box_id, content):
        para = (self.index[box_id], content)
        # self.cursor.execute('select ')
        pass

    def add_data(self):
        pass

    def get_relations(self):
        pass

    def match_data(self):
        pass


if __name__ == '__main__':
    test = Backend()
    a = test.get_data(1)
    print(a)
