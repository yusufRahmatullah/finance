from app import db
from model.base import Base, cached


class Wallet(Base, db.Model):
    name = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, default=0)
    period = db.Column(db.Date)

    def __repr__(self):
        return f'{self.name} | {self.amount} | {self.left }'

    @property
    @cached
    def transactions(self):
        return []  # wallet-transaction not implemented yet

    @property
    @cached
    def left(self):
        spend = sum(map(lambda x: x.outcome, self.transactions))
        income = sum(map(lambda x: x.income, self.transactions))
        return self.amount - spend + income
