from datetime import date

from flask import Flask, jsonify, request

from app import db, migrate
from model import Budget
from serializer import BudgetSerializer
from service import BudgetService, RecordNotFoundError

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
migrate.init_app(app, db)


@app.errorhandler(RecordNotFoundError)
def handle_not_found(e):
    code = 404
    return jsonify(error=str(e)), code


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
