# from aiogram import types, Bot
# from gino import Gino
# #
# from sqlalchemy import (Column, Integer, BigInteger, String,
#                         Sequence, TIMESTAMP, Boolean, JSON, DateTime)
# from sqlalchemy import sql
# #
# from config import load_config, POSTGRES_URL
#
# db = Gino()
# #
# #
# # # Документация
# # # http://gino.fantix.pro/en/latest/tutorials/tutorial.html
# #
# # Модель пользователя в Gino
# class User(db.Model):
#     __tablename__ = 'users'
#     id = Column(Integer(), primary_key=True)
#     user_id = Column(BigInteger(), unique=True)
#     referral = Column(Integer)
#     query: sql.Select
#
#     def __repr__(self):
#         return "<User(id='{}', fullname='{}', username='{}')>".format(
#             self.id, self.full_name, self.username)
#
#
# class DBCommands:
#
#     async def get_user(self, user_id):
#         user = await User.query.where(User.user_id == user_id).gino.first()
#         return user
#
#     async def add_new_user(self, referral=None):
#         user = types.User.get_current()
#         old_user = await self.get_user(user.id)
#         if old_user:
#             return old_user
#         new_user = User()
#         new_user.user_id = user.id
#         new_user.username = user.username
#         new_user.full_name = user.full_name
#
#         if referral:
#             new_user.referral = int(referral)
#         await new_user.create()
#         return new_user
#
#     async def count_users(self) -> int:
#         total = await db.func.count(User.id).gino.scalar()
#         return total
#
#     async def check_referrals(self):
#         bot = Bot.get_current()
#         user_id = types.User.get_current().id
#
#         user = await User.query.where(User.user_id == user_id).gino.first()
#         referrals = await User.query.where(User.referral == user.id).gino.all()
#
#         return ", ".join([
#             f"{num + 1}. " + (await bot.get_chat(referral.user_id)).get_mention(as_html=True)
#             for num, referral in enumerate(referrals)
#         ])
#
#
# async def create_db():
#     await db.set_bind(POSTGRES_URL)
# #
# #     # Create tables
# #
# #     await db.gino.create_all()
