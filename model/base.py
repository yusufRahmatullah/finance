from datetime import datetime

from app import db


class Base:
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
    updated_at = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.now,
        onupdate=datetime.now
    )


def cached(func):
    def wrapper(self=None):
        var_name = f'_{func.__name__}'
        if not hasattr(self, var_name):
            setattr(self, var_name, func(self))
        return getattr(self, var_name)
    return wrapper
