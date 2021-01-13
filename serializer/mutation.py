from model import Mutation
from serializer.base import Base
from service.wallet import HAND_NAME


class MutationSerializer(Base):
    @classmethod
    def serialize(cls, model: Mutation):
        to_name = HAND_NAME
        if model.to:
            to_name = model.to.name

        return cls._merge(super().serialize(model), {
            'date': model.date.strftime('%Y-%m-%d'),
            'thing': model.thing,
            'from': model.from_wallet.name,
            'from_left': model.from_left,
            'to': to_name,
            'amount': model.amount,
        })
