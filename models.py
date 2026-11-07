from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey


class Base(DeclarativeBase):
    pass

class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str | None] = mapped_column(unique=True, index=True, nullable=True)
    full_name: Mapped[str | None] = mapped_column(nullable=True)
    is_active: Mapped[bool] = mapped_column(default=True)
    age: Mapped[int] = mapped_column()


class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(unique=True, index=True)
    theme: Mapped[int] = mapped_column()
    author: Mapped[str] = mapped_column(index=True)