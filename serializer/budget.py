from model import Budget
from serializer.base import Base
from serializer import transaction


class BudgetSerializer(Base):
    @classmethod
    def serialize(cls, model: Budget):
        return cls._merge(super().serialize(model), {
            'name': model.name,
            'amount': model.amount,
            'period': model.period.strftime('%Y-%m-%d'),
            'transactions': cls._serialize_transactions(model.transactions)
        })

    @staticmethod
    def _serialize_transactions(transactions):
        return list(map(
            transaction.TransactionSerializer.serialize,
            transactions
        ))
