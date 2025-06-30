# Import libraries
from flask import Flask,request,url_for,redirect,render_template
# Instantiate Flask functionality
app = Flask(__name__)
# Sample data
transactions= [
    {'id':1,'date': '2023-06-01','amount':200},
    {'id':2,'date': '2022-10-05','amount':300},
    {'id':3,'date': '2025-02-20','amount':400},
    {'id':4,'date': '2024-07-14','amount':-200}
]
# Read operation: List all transactions
@app.route('/')
def get_transactions():
    return render_template("transactions.html",transactions=transactions)
# Create operation: Display add transaction form
# Route to handle the creation of a new transaction
@app.route('/add', methods=['POST','GET'])
def add_transaction():
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Create a new transaction object using form field values
        transaction = {
            'id': len(transactions) + 1,
            'date': request.form['date'],
            'amount': request.form['amount'],
        }
        # Append the new transaction to the transactions list
        transactions.append(transaction)
        # Redirect to the transactions list page after adding the new transaction
        return redirect(url_for('get_transactions'))
    # If the request method is GET, render the form template to display the add transaction form
    return render_template("form.html")

# Update operation: Display edit transaction form
# Route to handle the editing of an existing transaction
@app.route('/edit/<int:transaction_id>', methods=['POST','GET'])
def edit_transaction(transaction_id):
    # Check if the request method is POST (form submission)
    if request.method == 'POST':
        # Extract the updated values from the form fields
        date = request.form['date']# Get the 'date' field value from the form
        amount = request.form['amount'] # Get the 'amount' field value from the form

        # Find the transaction with the matching ID and update its values
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date  # Update the 'date' field of the transaction
                transaction['amount'] = amount # Update the 'amount' field of the transaction
                break
        # Redirect to the transactions list page after updating the transaction
        return redirect(url_for("get_transactions"))

    # If the request method is GET, find the transaction with the matching ID and render the edit form
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            # Render the edit form template and pass the transaction to be edited
            return render_template("edit.html", transaction=transaction)

    # If the transaction with the specified ID is not found, handle this case (optional)
    return {"message":"Transaction not found"},400

# Delete operation: Delete a transaction
# Route to handle the deletion of an existing transaction
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    # Find the transaction with the matching ID and remove it from the list
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction) # Remove the transaction from the transactions list
            break # Exit the loop once the transaction is found and removed
    # Redirect to the transactions list page after deleting the transaction
    return redirect(url_for("get_transactions"))

# Run the Flask app
if __name__=='__main__':
    app.run(debug=True)