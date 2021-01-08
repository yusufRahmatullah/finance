from app import db
from model.base import Base
from model import transaction


class Budget(Base, db.Model):
    name = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, default=0)
    period = db.Column(db.Date)

    def __repr__(self):
        return f'{self.name} | {self.amount} | {self.humanize_period() }'

    @property
    def transactions(self):
        return transaction.Transaction.query.filter_by(budget_id=self.id).all()
