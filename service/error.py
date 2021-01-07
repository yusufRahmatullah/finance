class RecordNotFoundError(Exception):
    def __init__(self):
        super().__init__('Record Not Found')
