from datetime import date

from model import Wallet
from service.base import Base
from service.error import RecordNotFoundError, WalletProhibitedNameError

HAND_NAME = 'hand'


class WalletService(Base):
    @classmethod
    def add_wallet(cls, name: str, amount: int, period: date):
        name = name.replace(' ', '_').lower()
        if name == HAND_NAME:
            raise WalletProhibitedNameError(HAND_NAME)
        wallet = Wallet(name=name, amount=amount, period=period)
        cls.save(wallet)
        return wallet

    @staticmethod
    def find_by_name(name: str, mutation_date: date):
        month = mutation_date.month
        year = mutation_date.year
        if mutation_date.day >= 27:
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
        period = date(year, month, 1)
        wallet = Wallet.query.filter_by(name=name, period=period).first()
        if not wallet:
            raise RecordNotFoundError
        return wallet

    @staticmethod
    def get_wallet(period: date, name: str):
        return Wallet.query.filter_by(period=period, name=name).first()

    @staticmethod
    def get_wallets(period: date):
        return Wallet.query \
            .filter_by(period=period) \
            .order_by(Wallet.name.asc()).all()

    @staticmethod
    def get_wallet_names(period: date):
        return list(map(
            lambda x: x.name,
            Wallet.query.filter_by(period=period).all()
        )) + [HAND_NAME]

    @staticmethod
    def total_wallets(period: date):
        wallets = Wallet.query.filter_by(period=period).all()
        if not wallets:
            return 0
        s = 0
        for wallet in wallets:
            s += wallet.amount
        return s
