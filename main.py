from datetime import date

from flask import Flask, jsonify, request

from app import db, migrate
from controller import (
    BaseController, BudgetController, TransactionController,
    serialize
)
from model import Budget, Transaction
from serializer import BudgetSerializer, TransactionSerializer
from service import BudgetService, RecordNotFoundError, TransactionService

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(BaseController)
app.register_blueprint(BudgetController, url_prefix='/budgets')
app.register_blueprint(TransactionController, url_prefix='/transactions')
