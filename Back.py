from configparser import ConfigParser
import sqlite3


class Backend:
    def __init__(self):
        config = ConfigParser()
        config.read('.config.ini')
        # 读取配置文件
        db_path = config.get('Environment', 'database_path')
        self.database = sqlite3.connect(db_path)
        # 连接数据库

    def get_data(self, field_name):
        """
        :param field_name: str/int 字段名称（可填序号或名称）
        :return: list 相关字段数据列表
        """
        pass

    def init(self, type):
        pass

    def query(self, box_id, content=''):
        pass

    def add_data(self):
        pass

    def get_relations(self):
        pass

    def match_data(self):
        pass


if __name__ == '__main__':
    test = Backend()
