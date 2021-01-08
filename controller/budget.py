from flask import Blueprint, jsonify, request

from controller.base import serialize
from service import BudgetService
from serializer import BudgetSerializer

BudgetController = Blueprint('budget', __name__)


@BudgetController.route('/')
def budgets():
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    return serialize(BudgetService.get_budgets(year, month), BudgetSerializer)


@BudgetController.route('/add')
def add_budget():
    name = request.args.get('name')
    amount = int(request.args.get('amount'))
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    budget = BudgetService.add_budget(name, amount, year, month)
    return serialize(budget, BudgetSerializer)


@BudgetController.route('/delete')
def delete_budget():
    id = int(request.args.get('id'))
    budget = BudgetService.delete_budget(id)
    return serialize(budget, BudgetSerializer)


@BudgetController.route('/total')
def total_budgets():
    year = int(request.args.get('year'))
    month = int(request.args.get('month'))
    total = BudgetService.total_budgets(year, month)
    return jsonify({
        'total': total
    })
