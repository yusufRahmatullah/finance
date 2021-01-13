from datetime import date

from flask import Blueprint, jsonify, render_template, request

from service import (
    BudgetService,
    RecordNotFoundError,
    UnprocessableEntityError,
    WalletService
)

BaseController = Blueprint('base', __name__)


@BaseController.route('/')
def index():
    return render_template('index.html')


@BaseController.route('/summary')
def summary():
    period = get_period()
    budgets = BudgetService.get_budgets(period.year, period.month)
    budget_left = 0
    for b in budgets:
        budget_left += b.left

    wallet_jenius = 0
    wallet = WalletService.get_wallet(period, 'jenius')
    if wallet:
        wallet_jenius = wallet.left

    total = budget_left + wallet_jenius
    data = {
        'budget_left': budget_left,
        'wallet_jenius': wallet_jenius,
        'total': total,
    }
    return jsonify(data)


@BaseController.app_errorhandler(RecordNotFoundError)
def handle_not_found(e):
    return jsonify(error=str(e)), 404


@BaseController.app_errorhandler(UnprocessableEntityError)
def handle_not_found(e):
    return jsonify(error=str(e)), 422


def serialize(model, serializer):
    if isinstance(model, list):
        return jsonify(list(map(
            lambda x: serializer.serialize(x),
            model
        )))
    else:
        return jsonify(serializer.serialize(model))


def get_period():
    now = date.today()
    year = now.year
    month = now.month
    day = now.day
    if day >= 27:
        month += 1
        if month >= 12:
            month = 1
            year += 1
    return date(year, month, 1)
