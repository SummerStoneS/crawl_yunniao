import pymongo


class Processing(object):
    def __init__(self):
        self.client = pymongo.MongoClient('192.168.3.109')     # 创建一个连接
        self.client['test'].authenticate('srf', 'chenbingxuan')       # 登陆信息
        self.db = self.client['mck']                           # 创建数据库
        self.collection = self.db['yunniao']                   # 创建collection类似表

    def find_exist(self, task_id):
        find_result = self.collection.find_one({'task_id': task_id})
        return find_result

    def insert(self, task):
        self.collection.insert_one(task)                        # 插入数据