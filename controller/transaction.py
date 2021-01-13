from datetime import date

from flask import Blueprint, jsonify, render_template, request

from controller.base import get_period, serialize
from service import TransactionService
from serializer import TransactionSerializer

TransactionController = Blueprint('transaction', __name__)


@TransactionController.route('/')
def show():
    return render_template('transaction.html')


@TransactionController.route('/add-form')
def add_form():
    return render_template('transaction_add_form.html')


@TransactionController.route('/get')
def get_transactions():
    return serialize(
        TransactionService.get_transactions(get_period()),
        TransactionSerializer
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


@TransactionController.route('/add-split')
def add_split_transactions():
    trx_date = date.fromisoformat(request.args.get('date'))
    budget_names = request.args.getlist('budgets[]')
    thing = request.args.get('thing')
    income = int(request.args.get('income', default=0))
    outcome = int(request.args.get('outcome', default=0))
    trxs = TransactionService.add_split_transactions(
        trx_date, budget_names, thing, income, outcome
    )
    return serialize(trxs, TransactionSerializer)
