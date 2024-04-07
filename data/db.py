from aiogram import types, Bot
from gino import Gino
#
from sqlalchemy import (Column, Integer, BigInteger, String,
                        Sequence, TIMESTAMP, Boolean, JSON, DateTime)
from sqlalchemy import sql
#
from config import load_config, POSTGRES_URL

db = Gino()


# Документация
# http://gino.fantix.pro/en/latest/tutorials/tutorial.html

# Модель пользователя в Gino
class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer(), primary_key=True)
    user_id = Column(BigInteger())
    refferal = Column(Integer())

    query: sql.Select

    def __repr__(self):
        return "<User(id='{}' refferal= '{}')>".format(
            self.id, self.refferal)


class DBCommands:

    async def get_user(self, user_id):
        user = await User.query.where(User.user_id == user_id).gino.first()
        return user

    # Check if the user is in the database
    async def add_new_user(self, refferal=None):
        user = types.User.get_current()
        old_user = await self.get_user(user.id)

        if old_user:
            return old_user
        new_user = User()
        new_user.user_id = user.id

        if refferal:
            new_user.refferal = int(refferal)
        await new_user.create()

        return new_user

    # Check refferal in the data
    async def check_referrals(self):
        bot = Bot.get_current()
        user_id = types.User.get_current()
        user = await self.get_user(user_id.id)

        refferals = await User.query.where(User.refferal == user.user_id).gino.all()
        print(refferals)
        return ", ".join([
            f"{num + 1}. " + (await bot.get_chat(refferal.user_id)).get_mention(as_html=True)
            for num, refferal in enumerate(refferals)
        ])


async def create_db():
    await db.set_bind(POSTGRES_URL)

    #     # Create tables
    await db.gino.create_all()
