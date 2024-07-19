from typing import List
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Column, Integer

from app import dB
from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from flask_login import UserMixin


class Pizza(dB.Model):
    __tablename__ = "pizzas"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50))
    description: Mapped[str] = mapped_column(String(100))
    prize: Mapped[int] = mapped_column(default=79)

    def __str__(self):
        return f"<Pizzas title:{self.name}>"


class Feedback(dB.Model):
    __tablename__ = "reviews"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    nickname: Mapped[str] = mapped_column(String(50))
    feedback: Mapped[str] = mapped_column(String(100))

    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship("User", back_populates="reviews")

    def __str__(self):
        return f"Review {self.id}: {self.feedback}"


class User(UserMixin, dB.Model):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    nickname: Mapped[str] = mapped_column(String(25), unique=True)
    email: Mapped[str] = mapped_column(String(50), unique=True)
    password: Mapped[str] = mapped_column(String(50))

    reviews = relationship("Feedback", back_populates="user")

    def __repr__(self):
        return f"User: {self.nickname}"

    def __str__(self):
        return self.nickname.capitalize()
