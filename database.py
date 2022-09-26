from os import environ
from motor import motor_asyncio as ma


class Database:
    def __init__(self):
        self.client = ma.AsyncIOMotorClient(environ.get('DATABASE_URL'))
        self.db = self.client['AutoRequestBot']
        self.users = self.db.users


    async def is_user_exist(self, user_id):
        user = await self.users.find_one({'id': user_id})
        return True if user else False
    

    async def add_user(self, user_id):
        if not await self.is_user_exist(user_id):
            await self.users.insert_one({'id': user_id})


    async def get_all_users(self):
        users = self.users.find({})
        return users


    async def total_users_count(self):
        count = await self.col.count_documents({})
        return count


    async def delete_user(self, user_id):
        try:
            await self.user.delete_many({"id": user_id})
        except:
            pass