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
            t = self.index[rid]
            s = self.index[qid]
            a = self.index[min(rid, qid)]
            b = self.index[max(rid, qid)]
            #sql = format('select name from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            sql = format('select name from %s inner join %s_%s on %s.name = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            if 'medicine' in (a, b):
                #sql = format('select name, grams from %s inner join %s_%s on %s.id = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
                sql = format('select name, grams from %s inner join %s_%s on %s.name = %s_%s.%s_id where %s_id = ?' % (t, a, b, t, a, b, t, s))
            #self.cursor.execute(sql, (id, ))
            self.cursor.execute(sql, (text, ))
            raw = self.cursor.fetchall()
            return self.convert_raw_to_data(raw)    

    def find_relative_info(self, id, content):
        data_left = self.query_similar_data(id-1, content) if 1 <= id <= 3 else list()
        data_right = self.query_similar_data(id+1, content) if 0 <= id <= 2 else list()
        data = dict()
        if data_left:
            data[id-1] = data_left
        if data_right:
            data[id+1] = data_right
        return data

    @staticmethod
    def convert_raw_to_data(raw):
        lst = list()
        for elem in raw:
            lst.append(list())
            for item in elem:
                lst[-1].append(str(item))
        return lst