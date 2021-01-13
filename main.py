from datetime import date

from flask import Flask, jsonify, request

from app import db, migrate
from controller import (
    BaseController,
    BudgetController,
    TransactionController,
    WalletController
)
from model import Budget, Transaction
from serializer import BudgetSerializer, TransactionSerializer
from service import BudgetService, RecordNotFoundError, TransactionService

app = Flask(
    __name__,
    static_url_path='',
    static_folder='static',
    template_folder='templates'
)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['TEMPLATES_AUTO_RELOAD'] = True
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(BaseController)
app.register_blueprint(BudgetController, url_prefix='/budgets')
app.register_blueprint(TransactionController, url_prefix='/transactions')
app.register_blueprint(WalletController, url_prefix='/wallets')
