from model import Budget
from serializer.base import Base


class BudgetSerializer(Base):
    @classmethod
    def serialize(cls, model: Budget):
        return cls._merge(super().serialize(model), {
            'name': model.name,
            'amount': model.amount,
            'period': model.period.strftime('%Y-%m-%d')
        })
