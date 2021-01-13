from model import Wallet
from serializer.base import Base


class WalletSerializer(Base):
    @classmethod
    def serialize(cls, model: Wallet):
        return cls._merge(super().serialize(model), {
            'name': model.name,
            'amount': model.amount,
            'period': model.period.strftime('%Y-%m-%d'),
            'transactions': cls._serialize_transactions(model.transactions),
            'left': model.left
        })

    @staticmethod
    def _serialize_transactions(transactions):
        return transactions  # notimplemented yet
