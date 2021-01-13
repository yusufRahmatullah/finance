from app import db
from model.base import Base, cached
from model import budget


class Transaction(Base, db.Model):
    date = db.Column(db.Date, nullable=False)
    budget_id = db.Column(db.Integer, nullable=False)
    thing = db.Column(db.String, default='')
    income = db.Column(db.Integer, default=0)
    outcome = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'{self.date} | {self.thing} | {self.income} | {self.outcome}'

    @property
    @cached
    def budget(self):
        return budget.Budget.query.get(self.budget_id)
