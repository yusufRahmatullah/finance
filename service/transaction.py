from datetime import date

from model import Transaction
from service.base import Base
from service import budget as budget_service
from service.error import BudgetAmountExceedLimitError, RecordNotFoundError


class TransactionService(Base):
    @classmethod
    def add_transaction(cls,
        trx_date: date, budget_name: str, thing: str,
        income: int, outcome: int):
        budget = budget_service.BudgetService.find_by_name(
            budget_name, trx_date
        )
        if outcome > budget.left + income:
            raise BudgetAmountExceedLimitError(budget.left)
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
    def add_split_transactions(cls,
        trx_date: date, budget_names: list, thing: str,
        income: int, outcome: int):
        budgets = cls._get_budgets_by_names(budget_names, trx_date)
        total_left = sum(map(lambda x: x.left, budgets))
        cur_outcome = outcome - income
        if cur_outcome > total_left:
            raise BudgetAmountExceedLimitError(total_left)

        trxs = []
        for budget in budgets:
            if cur_outcome == 0:
                break

            left = budget.left
            if left == 0:
                continue

            trx_outcome = cur_outcome
            if trx_outcome > left:
                trx_outcome = left
                cur_outcome -= left
            else:
                cur_outcome = 0
            trx = Transaction(
                date=trx_date, budget_id=budget.id, thing=thing,
                income=0, outcome=trx_outcome
            )
            cls.save(trx)
            trxs.append(trx)
        return trxs

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

    @classmethod
    def get_transactions(cls, period: date):
        begin, end = cls.generate_period(period)
        return Transaction.query \
            .filter(Transaction.date.between(
                begin.isoformat(),
                end.isoformat()
            )) \
            .order_by(Transaction.date.asc()).all()

    @staticmethod
    def _get_budgets_by_names(names: list, trx_date: date):
        budgets = []
        for name in names:
            budgets.append(budget_service.BudgetService.find_by_name(
                name, trx_date
            ))
        return budgets
