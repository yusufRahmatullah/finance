class RecordNotFoundError(Exception):
    def __init__(self):
        super().__init__('Record Not Found')


class UnprocessableEntityError(Exception):
    def __init__(self, msg='Unprocessable Entity'):
        super().__init__(msg)


class BudgetAmountExceedLimitError(UnprocessableEntityError):
    def __init__(self, left: int):
        super().__init__(f'Budget left is only {left}')


class WalletAmountExceedLimitError(UnprocessableEntityError):
    def __init__(self, left: int):
        super().__init__(f'Wallet left is only {left}')


class WalletProhibitedNameError(UnprocessableEntityError):
    def __init__(self, name: str):
        super().__init__(f'Cannot use {name} as Wallet name')
