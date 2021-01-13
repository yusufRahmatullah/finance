from datetime import date

from model import Mutation
from service.base import Base
from service import wallet as wallet_service
from service.error import RecordNotFoundError, WalletAmountExceedLimitError


class MutationService(Base):
    @classmethod
    def add_mutation(cls,
        mutation_date: date, thing: str,
        from_name: str, to_name: str, amount: int):
        from_wallet = wallet_service.WalletService.find_by_name(
            from_name, mutation_date
        )
        if to_name == wallet_service.HAND_NAME:
            to_id = 0
        else:
            to_wallet = wallet_service.WalletService.find_by_name(
                to_name, mutation_date
            )
            to_id = to_wallet.id

        if amount > from_wallet.left:
            raise WalletAmountExceedLimitError(from_wallet.left)
        mutation = Mutation(
            date=mutation_date,
            thing=thing,
            from_id=from_wallet.id,
            to_id=to_id,
            amount=amount,
        )
        cls.save(mutation)
        return mutation

    @classmethod
    def get_mutations(cls, period: date):
        begin, end = cls.generate_period(period)
        return Mutation.query \
            .filter(Mutation.date.between(
                begin.isoformat(),
                end.isoformat()
            )).all()
