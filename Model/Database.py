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