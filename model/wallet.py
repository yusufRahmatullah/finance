from app import db
from model.base import Base, cached
from model import mutation


class Wallet(Base, db.Model):
    name = db.Column(db.String, nullable=False)
    amount = db.Column(db.Integer, default=0)
    period = db.Column(db.Date)

    def __repr__(self):
        return f'{self.name} | {self.amount} | {self.left }'

    @property
    @cached
    def from_mutations(self):
        return mutation.Mutation.query.filter_by(from_id=self.id)

    @property
    @cached
    def left(self):
        tos = sum(map(lambda x: x.amount, self.to_mutations))
        froms = sum(map(lambda x: x.amount, self.from_mutations))
        return self.amount - froms + tos

    @property
    @cached
    def to_mutations(self):
        return mutation.Mutation.query.filter_by(to_id=self.id)
