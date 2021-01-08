from model import Transaction
from serializer.base import Base


class TransactionSerializer(Base):
    @classmethod
    def serialize(cls, model: Transaction):
        return cls._merge(super().serialize(model), {
            'date': model.date.strftime('%Y-%m-%d'),
            'budget': model.budget.name,
            'thing': model.thing,
            'income': model.income,
            'outcome': model.outcome
        })
