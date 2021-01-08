from datetime import date

from flask import Flask, jsonify, request

from app import db, migrate
from controller import base
from model import Budget, Transaction
from serializer import BudgetSerializer, TransactionSerializer
from service import BudgetService, RecordNotFoundError, TransactionService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(base)


def serialize(model, serializer):
    if isinstance(model, list):
        return jsonify(list(map(
            lambda x: serializer.serialize(x),
            model
        )))
    else:
        return jsonify(serializer.serialize(model))


@app.route('/')
def index():
    return 'Hello'


@app.route('/add-budget')
def add_budget():
    name = request.args.get('name')
    amount = int(request.args.get('amount'))
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    budget = BudgetService.add_budget(name, amount, year, month)
    return serialize(budget, BudgetSerializer)


@app.route('/delete-budget')
def delete_budget():
    id = int(request.args.get('id'))
    budget = BudgetService.delete_budget(id)
    return serialize(budget, BudgetSerializer)


@app.route('/budgets')
def budgets():
    return serialize(BudgetService.get_budgets(), BudgetSerializer)


@app.route('/total-budgets')
def total_budgets():
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    total = BudgetService.total_budgets(year, month)
    return jsonify({
        'total': total
    })


@app.route('/add-transaction')
def add_transaction():
    trx_date = date.fromisoformat(request.args.get('date'))
    budget_name = request.args.get('budget')
    thing = request.args.get('thing')
    income = request.args.get('income')
    if not income:
        income = 0
    outcome = request.args.get('outcome')
    if not outcome:
        outcome = 0
    trx = TransactionService.add_transaction(
        trx_date, budget_name, thing, income, outcome
    )
    return serialize(trx, TransactionSerializer)


@app.route('/transactions')
def transactions():
    return serialize(
        TransactionService.get_transactions(), TransactionSerializer
    )
