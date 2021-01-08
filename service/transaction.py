from datetime import date

from model import Transaction
from service.base import Base
from service.budget import BudgetService
from service.error import RecordNotFoundError


class TransactionService(Base):
    @classmethod
    def add_transaction(cls,
        trx_date: date, budget_name: str, thing: str,
        income: int, outcome: int):
        budget = BudgetService.find_by_name(budget_name, trx_date)
        trx = Transaction(
            date=trx_date,
            budget_id=budget.id,
            thing=thing,
            income=income,
            outcome=outcome
        )
        cls.save(trx)
        return trx

    @classmethod
    def delete_transaction(cls, id: int):
        trx = cls.get_transaction(id)
        cls.delete(trx)
        return trx

    @staticmethod
    def get_transaction(id):
        trx = Transaction.query.get(id)
        if not trx:
            raise RecordNotFoundError
        return trx

    @staticmethod
    def get_transactions():
        return Transaction.query.all()
