from flask import Blueprint, jsonify, render_template, request

from controller.base import get_period, serialize
from service import WalletService
from serializer import WalletSerializer

WalletController = Blueprint('wallet', __name__)


@WalletController.route('/')
def show():
    return render_template('wallet.html')


@WalletController.route('/add-form')
def add_form():
    return render_template('wallet_add_form.html')


@WalletController.route('/get')
def get_wallets():
    period = get_period()
    return serialize(WalletService.get_wallets(period), WalletSerializer)


@WalletController.route('/add')
def add_wallet():
    name = request.args.get('name')
    amount = int(request.args.get('amount'))
    period = get_period()
    wallet = WalletService.add_wallet(name, amount, period)
    return serialize(wallet, WalletSerializer)
