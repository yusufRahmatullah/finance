from datetime import date

from model import Budget
from service.base import Base
from service.error import RecordNotFoundError


class BudgetService(Base):
    @classmethod
    def add_budget(cls, name: str, amount: int, year: int, month: int):
        budget = Budget(name=name, amount=amount, period=date(year, month, 1))
        cls.save(budget)
        return budget

    @classmethod
    def delete_budget(cls, id: int):
        budget = Budget.query.get(id)
        if not budget:
            raise RecordNotFoundError
        cls.delete(budget)
        return budget


    @staticmethod
    def get_budgets():
        return Budget.query.all()
