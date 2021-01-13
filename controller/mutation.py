from datetime import date

from flask import Blueprint, jsonify, render_template, request

from controller.base import get_period, serialize
from service import MutationService
from serializer import MutationSerializer

MutationController = Blueprint('mutation', __name__)


@MutationController.route('/')
def show():
    return render_template('mutations.html')


@MutationController.route('/add-form')
def add_form():
    return render_template('mutation_add_form.html')


@MutationController.route('/get')
def get_mutations():
    return serialize(
        MutationService.get_mutations(get_period()),
        MutationSerializer
    )


@MutationController.route('/add')
def add_mutation():
    mutation_date = date.fromisoformat(request.args.get('date'))
    thing = request.args.get('thing')
    from_name = request.args.get('from')
    to_name = request.args.get('to')
    amount = int(request.args.get('amount', default=0))

    mutation = MutationService.add_mutation(
        mutation_date, thing, from_name, to_name, amount
    )
    return serialize(mutation, MutationSerializer)
