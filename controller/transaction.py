from datetime import date

from flask import Blueprint, jsonify, request

from controller.base import serialize
from service import TransactionService
from serializer import TransactionSerializer

TransactionController = Blueprint('transaction', __name__)


@TransactionController.route('/')
def transactions():
    return serialize(
        TransactionService.get_transactions(), TransactionSerializer
    )


@TransactionController.route('/add')
def add_transaction():
    trx_date = date.fromisoformat(request.args.get('date'))
    budget_name = request.args.get('budget')
    thing = request.args.get('thing')
    income = int(request.args.get('income', default=0))
    outcome = int(request.args.get('outcome', default=0))
    trx = TransactionService.add_transaction(
        trx_date, budget_name, thing, income, outcome
    )
    return serialize(trx, TransactionSerializer)
