from datetime import date

from model import Wallet
from service.base import Base
from service.error import RecordNotFoundError


class WalletService(Base):
    @classmethod
    def add_wallet(cls, name: str, amount: int, period: date):
        name = name.replace(' ', '_').lower()
        wallet = Wallet(name=name, amount=amount, period=period)
        cls.save(wallet)
        return wallet

    @staticmethod
    def get_wallets(period: date):
        return Wallet.query.filter_by(period=period).all()
