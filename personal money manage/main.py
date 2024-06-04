import pandas as pd
import matplotlib.pyplot as plt

# Load data
def load_data(file_path):
    return pd.read_csv(file_path, parse_dates=['Date'])

# Add new transaction
def add_transaction(df, date, category, description, amount, trans_type):
    new_transaction = {
        'Date': date,
        'Category': category,
        'Description': description,
        'Amount': amount,
        'Type': trans_type
    }
    df = df.append(new_transaction, ignore_index=True)
    return df

# Save data
def save_data(df, file_path):
    df.to_csv(file_path, index=False)

# Generate summary
def generate_summary(df):
    income = df[df['Type'] == 'Income']['Amount'].sum()
    expenses = df[df['Type'] == 'Expense']['Amount'].sum()
    balance = income + expenses
    return income, expenses, balance

# Generate category summary
def generate_category_summary(df):
    return df.groupby('Category')['Amount'].sum()

# Plot data
def plot_data(df):
    df['Amount'] = df.apply(lambda x: x['Amount'] if x['Type'] == 'Income' else -x['Amount'], axis=1)
    df.set_index('Date', inplace=True)
    df['Amount'].cumsum().plot()
    plt.title('Cumulative Income and Expenses Over Time')
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.show()

# Main program
def main():
    file_path = 'finance_data.csv'
    df = load_data(file_path)

    while True:
        print("\nFinance Tracker")
        print("1. Add Transaction")
        print("2. View Summary")
        print("3. View Category Summary")
        print("4. Plot Data")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: "))
            trans_type = input("Enter type (Income/Expense): ")
            df = add_transaction(df, date, category, description, amount, trans_type)
            save_data(df, file_path)
            print("Transaction added successfully!")
        elif choice == '2':
            income, expenses, balance = generate_summary(df)
            print(f"\nSummary:")
            print(f"Total Income: {income}")
            print(f"Total Expenses: {expenses}")
            print(f"Balance: {balance}")
        elif choice == '3':
            category_summary = generate_category_summary(df)
            print("\nCategory Summary:")
            print(category_summary)
        elif choice == '4':
            plot_data(df)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
