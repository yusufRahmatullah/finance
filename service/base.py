from datetime import date

from app import db


class Base:
    @staticmethod
    def save(model):
        db.session.add(model)
        db.session.commit()

    @staticmethod
    def delete(model):
        db.session.delete(model)
        db.session.commit()

    @staticmethod
    def generate_period(period_date: date):
        year = period_date.year
        month = period_date.month
        end = date(year, month, 26)
        if month == 1:
            begin = date(year - 1, 12, 27)
        else:
            begin = date(year, month - 1, 27)
        return begin, end
