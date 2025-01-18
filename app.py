from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

# Dummy data for transactions
transactions = [
    {'user': 'User1', 'amount': 100, 'status': 'completed', 'timestamp': datetime.now()},
    {'user': 'User2', 'amount': 200, 'status': 'pending', 'timestamp': datetime.now()},
    {'user': 'User3', 'amount': 50, 'status': 'waiting for payment', 'timestamp': datetime.now()},
    {'user': 'User4', 'amount': 150, 'status': 'cancelled by user', 'timestamp': datetime.now()},
]

# Transaction statistics
def get_transaction_stats():
    completed = len([t for t in transactions if t['status'] == 'completed'])
    pending = len([t for t in transactions if t['status'] == 'pending'])
    waiting = len([t for t in transactions if t['status'] == 'waiting for payment'])
    cancelled = len([t for t in transactions if t['status'] == 'cancelled by user' or t['status'] == 'cancelled by admin'])
    return completed, pending, waiting, cancelled

@app.route('/')
def index():
    completed, pending, waiting, cancelled = get_transaction_stats()
    return render_template('index.html', 
                           transactions=transactions,
                           completed=completed,
                           pending=pending,
                           waiting=waiting,
                           cancelled=cancelled,
                           operator_status='online')  # Change to 'offline' as needed

@app.route('/exchange', methods=['POST'])
def exchange():
    exchange_type = request.form.get('exchange_type')
    payeer_account = request.form.get('payeer_account')
    amount = request.form.get('amount')
    evc_number = request.form.get('evc_number')

    return render_template('confirmation.html',
                           exchange_type=exchange_type,
                           payeer_account=payeer_account,
                           amount=amount,
                           evc_number=evc_number)

if __name__ == '__main__':
    app.run(debug=True)
