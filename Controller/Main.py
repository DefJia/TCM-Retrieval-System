from configparser import ConfigParser
from PyQt5.QtWidgets import QTableWidgetItem


class Controller:
    def __init__(self, interface, reminder=None, information = None,property=None) :
        config = ConfigParser()
        config.read('.config.ini')
        self.index = config.get('Setting', 'index').split(',')
        # 读取配置文件
