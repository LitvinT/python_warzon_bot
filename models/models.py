from datetime import datetime

from sqlalchemy import Column, Integer, ForeignKey, VARCHAR, DECIMAL, select, Boolean, BigInteger, SmallInteger, \
    TIMESTAMP
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, join

from loader import DATABASE_URL


Base = declarative_base()


class BaseMixin(object):
    id = Column(Integer, primary_key=True)

    engine = create_async_engine(f'postgresql+asyncpg://{DATABASE_URL}')

    def __init__(self, **kwargs) -> None:
        for kw in kwargs.items():
            self.__getattribute__(kw[0])
            self.__setattr__(*kw)

    @staticmethod
    def create_async_session(func):
        async def wrapper(*args, **kwargs):
            async with AsyncSession(bind=BaseMixin.engine) as session:
                return await func(*args, **kwargs, session=session)

        return wrapper

    @create_async_session
    async def save(self, session: AsyncSession = None) -> None:
        session.add(self)
        await session.commit()
        await session.refresh(self)

    @classmethod
    @create_async_session
    async def get(cls, pk: int, session: AsyncSession = None) -> Base:
        return await session.get(cls, pk)

    @classmethod
    @create_async_session
    async def all(cls, order_by: str = 'id', session: AsyncSession = None, **kwargs) -> list[Base]:
        return [obj[0] for obj in await session.execute(select(cls).filter_by(**kwargs).order_by(order_by))]

    @create_async_session
    async def delete(self, session: AsyncSession = None) -> None:
        await session.delete(self)
        await session.commit()

    @classmethod
    @create_async_session
    async def join(cls, right: Base, session: AsyncSession = None, **kwargs) -> list[tuple[Base, Base]]:
        return await session.execute(join(left=cls, right=right).filter_by(**kwargs))


class User(BaseMixin,Base):
    __tablename__: str = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(255), nullable=False)


class Category(BaseMixin, Base):
    __tablename__: str = 'categories'

    id = Column(SmallInteger, primary_key=True)
    category = Column(VARCHAR(15), nullable=False, unique=True)
    is_published = Column(Boolean, default=True, nullable=True)


class Brand(BaseMixin, Base):
    __tablename__: str = 'brands'

    category_id = Column(Integer, ForeignKey('categories.id', ondelete='CASCADE'), nullable=False)
    name = Column(VARCHAR(64), nullable=False, unique=True)


class Model(BaseMixin, Base):
    __tablename__: str = 'models'

    name = Column(VARCHAR(64), nullable=False, unique=True)
    brand_id = Column(Integer, ForeignKey('brands.id', ondelete='CASCADE'), nullable=False)


class ProductImage(BaseMixin, Base):
    __tablename__: str = 'product_images'

    model_id = Column(Integer, ForeignKey('models.id', ondelete='CASCADE'), nullable=False)
    url = Column(VARCHAR(512), nullable=False)
    title = Column(VARCHAR(256), nullable=False)
    telegram_id = Column(VARCHAR(512), nullable=True)



