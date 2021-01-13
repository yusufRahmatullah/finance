from datetime import date

from model import Budget
from service.base import Base
from service.error import RecordNotFoundError


class BudgetService(Base):
    @classmethod
    def add_budget(cls, name: str, amount: int, year: int, month: int):
        name = name.replace(' ', '_').lower()
        budget = Budget(name=name, amount=amount, period=date(year, month, 1))
        cls.save(budget)
        return budget

    @classmethod
    def delete_budget(cls, id: int):
        budget = cls.get_budget(id)
        cls.delete(budget)
        return budget

    @staticmethod
    def find_by_name(name: str, trx_date: date):
        period = date(trx_date.year, trx_date.month, 1)
        if trx_date.day >= 27:
            if period.month == 12:
                period.month = 1
                period.year += 1
            else:
                period.month += 1
        budget = Budget.query.filter_by(name=name, period=period).first()
        if not budget:
            raise RecordNotFoundError
        return budget

    @staticmethod
    def get_budget(id: int):
        budget = Budget.query.get(id)
        if not budget:
            raise RecordNotFoundError
        return budget

    @staticmethod
    def get_budget_names(year: int, month: int):
        period = date(year, month, 1)
        return list(map(
            lambda x: x.name,
            Budget.query.filter_by(period=period).all()
        ))

    @staticmethod
    def get_budgets(year: int, month: int):
        period = date(year, month, 1)
        return Budget.query.filter_by(period=period).all()        

    @staticmethod
    def total_budgets(year: int, month: int):
        period = date(year, month, 1)
        budgets = Budget.query.filter_by(period=period).all()
        if not budgets:
            return 0
        s = 0
        for budget in budgets:
            s += budget.amount
        return s
