from flask import Blueprint, jsonify, render_template, request

from controller.base import get_period, serialize
from service import BudgetService
from serializer import BudgetSerializer

BudgetController = Blueprint('budget', __name__)


@BudgetController.route('/')
def show():
    return render_template('budget.html')


@BudgetController.route('/add-form')
def add_form():
    return render_template('budget_add_form.html')


@BudgetController.route('/get')
def get_budgets():
    period = get_period()
    return serialize(
        BudgetService.get_budgets(period.year, period.month),
        BudgetSerializer
    )


@BudgetController.route('/names')
def get_budget_names():
    period = get_period()
    budget_names = BudgetService.get_budget_names(period.year, period.month)
    return jsonify(budget_names)


@BudgetController.route('/add')
def add_budget():
    name = request.args.get('name')
    amount = int(request.args.get('amount'))
    period = get_period()
    budget = BudgetService.add_budget(name, amount, period.year, period.month)
    return serialize(budget, BudgetSerializer)


@BudgetController.route('/delete')
def delete_budget():
    id = int(request.args.get('id'))
    budget = BudgetService.delete_budget(id)
    return serialize(budget, BudgetSerializer)


@BudgetController.route('/total')
def total_budgets():
    period = get_period()
    total = BudgetService.total_budgets(period.year, period.month)
    return jsonify({
        'total': total
    })
