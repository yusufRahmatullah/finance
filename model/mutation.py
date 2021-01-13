from app import db
from model.base import Base, cached
from model import wallet


class Mutation(Base, db.Model):
    date = db.Column(db.Date, nullable=False)
    thing = db.Column(db.String, default='')
    from_id = db.Column(db.Integer, nullable=False)
    to_id = db.Column(db.Integer, nullable=False)
    amount = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'{self.date} | {self.thing} | {self.from_wallet} | {self.to}'

    @property
    @cached
    def from_left(self):
        return self.from_wallet.left

    @property
    @cached
    def from_wallet(self):
        return wallet.Wallet.query.get(self.from_id)

    @property
    @cached
    def to(self):
        return wallet.Wallet.query.get(self.to_id)
