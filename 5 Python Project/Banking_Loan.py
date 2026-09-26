import os
from datetime import datetime
import json

FILE = "loans.json"
MIN_SALARY = 20000

def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, 'r') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def safe_date_input(msg):
    while True:
        date_str = input(msg)
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            print("Invalid date format.\n")
            
def next_due(start_date):
    
    d= datetime.strptime(start_date, "%d-%m-%Y")
   
    if d.month == 12:
        nxt = d.replace(year=d.year+1,month=1)
    else:
        nxt = d.replace(month=d.month+1)
    return nxt.strftime("%d-%m-%Y")
         
def generate_id(data):
    if not data:
        return 1001
    
    max_id = max(loan['loan_id'] for loan in data)
    return max_id + 1

def save_data(data):
    with open(FILE,"w") as f:
        json.dump(data,f,indent=2)
   
def find_loan(data,loan_id):
    for loan in data:
        if loan['loan_id'] == loan_id:
            return loan
    return None

def apply_loan(data):
    name = input("Enter your name: ")
    try:
        salary = int(input("Enter your monthly salary: "))
    except ValueError:
        print("Invalid salary amount.\n")
        return
    
    if salary < MIN_SALARY:
        print(f"Salary must be at least {MIN_SALARY} to get a loan.\n")
        return
    
    loan_amount = salary * 10
    emi = int(salary * 0.10)
    months = loan_amount // emi
    
    print(f"Congratulations {name}! You are eligible for a loan.")
    print(f"Loan Amount: {loan_amount}")
    print(f"EMI: {emi}")
    print(f"Tenure: {months} months\n")
    
    confirm = input("Do you want to proceed with the loan application? (yes/no):").lower()
    if confirm != 'yes':
        print("Loan application cancelled.\n")
        
        
    start_date = safe_date_input("Enter loan start date (dd-mm-yyyy):")

    first_due =  next_due(start_date)
    
    loan_id = generate_id(data)
    
    record ={
        "loan_id": loan_id,
        "name": name,
        "salary": salary,
        "loan_amount": loan_amount,
        "emi": emi,
        "tenure": months,
        "balance": loan_amount,
        "status": "ongoing",
        "next_due": first_due,
        "history" : []
        
    }
    data.append(record)
    save_data(data)
    print(f"Loan Approved. Your loan Id:{loan_id}")


def pay_emi(data):
    try:
        loan_id = int(input("Enter your loan id:"))
    except ValueError:
        print("Invalid loan Id.\n")
        return 
    
    loan = find_loan(data,loan_id)
    
    if not loan:
        print("Loan Not Found\n")
        return
    if loan["status"]=="Cleared":
        print("Loan already Cleared\n")
        return
    print(f"Next Emi Due:{loan['next_due']}")
    
    try:
        amt = int(input(f"Enter EMI ({loan['emi']}):"))
    except ValueError:
        print("Invalid Amount.\n")
        return
    
    if amt!=loan['emi']:
        print(f"Wrong Emi Amount,Expected({loan['emi']}),got{amt}")
        return
    
    loan['balance']-=amt
    loan['tenure'] -=1
    loan['history'].append({"date":loan['next_due'], "amount": amt})

    loan['next_due']=next_due(loan['next_due'])

    if loan['balance'] <=0:
        loan['status'] = "CLeared"
        loan['balance']=0
        loan['tenure']=0
        print("Loan Cleared Successfully.\n")
    else:
        print(f"EMI Paid, Balance Left: {loan['balance']}\nRemaining Tenure: {loan['tenure']} months.\n")

    save_data(data)

def clear_loan(data):
    try:
        loan_id = int(input("Enter your loan id:"))
    except ValueError:
        print("Invalid loan Id.\n")
        return 
    loan =find_loan(data,loan_id)
    
    if not loan:
        print("Loan Not Found\n")
        return
    if loan["status"]=="Cleared":
        print("Loan already Cleared\n")
        return
    
    print(f"Balance Left:{loan['balance']}")
    try:
        amt = int(input("Enter amount to clear (Full/Partial):"))
    except ValueError:
        print("Invalid amount.\n")
        return
    
    if amt == loan['balance']:
        pay_date =safe_date_input("Enter payment date(dd-mm-yyyy):")
        loan['history'].append({'date':pay_date, 'amount': amt})
        
        loan['status'] = "CLeared"
        loan['balance']=0
        loan['tenure']=0
        print("Loan Cleared Successfully.\n")
    elif amt<loan['balance'] and amt % loan['emi']==0:
        months_reduced = amt // loan['emi']
        pay_date = safe_date_input("enter Payment date(dd-mm-yyyy):")
        loan['history'].append({'date':pay_date, "amount":amt})
        
        loan['balance'] -=amt
        loan['tenure'] -= months_reduced
        
        print(f"Partial Clearence Done. Paid {amt}")
        print(f"Remaining Balance:{loan['balance']}, New Tenure: {loan['tenure']} months")
    else:
        print("Invalid amount. Must match balance(full) or be multiple of EMI (Partial)!")  
        return
    save_data(data)
    
def view_payment_history(data):
    try:
        loan_id =int(input("Enter Your Loan ID:"))
    except ValueError:
        print("Invalid ID")
        return

    loan = find_loan(data,loan_id)
    
    if not loan:
        print("Loan Nor Found\n")
        return
    print(f"\nPayment History For Loan Id {loan['loan_id']} - {loan['name']}")
    for p in loan['history']:
        print(f"Date:{p['date']} - Amount: {p['amount']}")
    print(f"\nBalance Remaining: {loan['balance']}")
    print(f"Status: {loan['status']}")
    
    if loan['status'] == "Ongoing":
        print(f"Next EMI Due: {loan['next_due']}\nRemaining Tenure: {loan['tenure']} months")
    
    
def main():
    
    data = load_data()
    
    
    while True:
        print("\n------- Bank Loan System ------")
        print("1. Apply for a loan")
        print("2. Pay EMI")
        print("3. clear loan")
        print("4. View Payment History")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            apply_loan(data)
        elif choice == '2':
            pay_emi(data)
        elif choice == '3':
            clear_loan(data)
        elif choice == '4':
            view_payment_history(data)
        elif choice == '5':
            print("Bye! Thank you")
            break
        else:
            print("Invalid choice. Please try again.")
    
main()