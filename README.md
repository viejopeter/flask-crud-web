# Flask Transactions CRUD App

This is a simple Flask web application that demonstrates basic CRUD (Create, Read, Update, Delete) operations on a list of financial transactions.

## 🚀 Features

- **Create**: Add a new transaction with date and amount.
- **Read**: View a list of all transactions.
- **Update**: Edit the date or amount of an existing transaction.
- **Delete**: Remove a transaction from the list.

## 📦 Requirements

- Python 3.x
- Flask

## 🔧 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/viejopeter/flask-crud-web.git
   cd flask-crud-web

    (Optional) Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install Flask:

pip install flask

Run the app:

    python app.py

    The app will be available at http://localhost:5000.

## 🗂 Project Structure

- `templates/`
  - `transactions.html` – Page to list all transactions
  - `form.html` – Form to add a new transaction
  - `edit.html` – Form to edit an existing transaction
  - `search.html` – Form to search an existing transaction
- `app.py` – Main Flask app

📋 Sample Data

The app uses a predefined list of sample transactions:

transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 200},
    {'id': 2, 'date': '2022-10-05', 'amount': 300},
    {'id': 3, 'date': '2025-02-20', 'amount': 400},
    {'id': 4, 'date': '2024-07-14', 'amount': -200}
]

📌 Notes

    This app stores data in memory (in a Python list). It does not use a database.

    Ideal for learning Flask fundamentals or demonstrating basic CRUD operations.

📄 License

This project is open source and available under the MIT License.