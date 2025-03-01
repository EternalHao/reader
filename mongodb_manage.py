from pymongo import MongoClient

class MongoDBManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.client = MongoClient('mongodb://localhost:27017/')
        return cls._instance

    def get_db(self):
        """获取数据库实例"""
        return self.client['reader']

# 全局实例
mongo_manager = MongoDBManager()
