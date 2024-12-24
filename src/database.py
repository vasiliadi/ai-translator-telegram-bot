from sqlalchemy import create_engine
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from config import DB_URL


class Base(DeclarativeBase):
    pass


class UsersOrm(Base):
    __tablename__ = "users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str | None]
    last_name: Mapped[str | None]
    username: Mapped[str | None]
    approved: Mapped[bool] = mapped_column(server_default="False")


sync_engine = create_engine(DB_URL, echo=False)
Base.metadata.create_all(sync_engine, checkfirst=True)


engine = create_async_engine(DB_URL, echo=False)
Session = async_sessionmaker(engine)


async def auth(user_id):
    async with Session() as session:
        user = await session.get(UsersOrm, user_id)
        if user is None:
            msg = "User not found"
            raise ValueError(msg)
        return user.approved


async def register_user(user_id, first_name, last_name, username, approved=False):
    async with Session() as session:
        try:
            stmt = UsersOrm(
                user_id=user_id,
                first_name=first_name,
                last_name=last_name,
                username=username,
                approved=approved,
            )
            session.add(stmt)
            await session.commit()
            return True
        except IntegrityError:
            await session.rollback()
            return False  # already registered user
