from model import Wallet
from serializer.base import Base
from serializer import mutation


class WalletSerializer(Base):
    @classmethod
    def serialize(cls, model: Wallet):
        return cls._merge(super().serialize(model), {
            'name': model.name,
            'amount': model.amount,
            'period': model.period.strftime('%Y-%m-%d'),
            'from_mutations': cls._serialize_mutations(model.from_mutations),
            'to_mutations': cls._serialize_mutations(model.to_mutations),
            'left': model.left
        })

    @staticmethod
    def _serialize_mutations(mutations):
        return list(map(
            mutation.MutationSerializer.serialize,
            mutations
        ))
