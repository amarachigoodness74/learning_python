import pandas as pd
import csv
from datetime import datetime
from data_entry import get_date, get_amount, get_category, get_description

class CSV :
  CSV_FILE = "finance_data.csv"
  COLUMNS = ["Date", "Amount", "Category", "Description"]
  DATEFORMAT= "%d-%m-%Y"

  @classmethod
  def initialize_csv(cls):
    try:
      pd.read_csv(cls.CSV_FILE)
    except FileNotFoundError:
      df = pd.DataFrame(columns=cls.COLUMNS)
      df.to_csv(cls.CSV_FILE, index=False)

  @classmethod
  def add_entry(cls, date, amount, category, description):
    new_entry = {
      "Date": date,
      "Amount": amount,
      "Category": category,
      "Description": description,
    }
    with open(cls.CSV_FILE, "a", newline="") as csvfile:
      writer = csv.DictWriter(csvfile, fieldnames=cls.COLUMNS)
      writer.writerow(new_entry)
    print("Entry added successfully")

  @classmethod
  def get_transactions(cls, start_date, end_date):
    df = pd.read_csv(cls.CSV_FILE)
    df["Date"] = pd.to_datetime(df["Date"], format=CSV.DATEFORMAT)
    start_date = datetime.strptime(start_date, CSV.DATEFORMAT)
    end_date = datetime.strptime(end_date, CSV.DATEFORMAT)

    mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
    filtered_df = df.loc[mask]

    if filtered_df.empty:
      print('No transactions found in the given date range')
    else:
      print(f"Transactions from {start_date.strftime(CSV.DATEFORMAT)} to {end_date.strftime(CSV.DATEFORMAT)}")
      print(filtered_df.to_string(index=False, formatters={"Date": lambda x: x.strftime(CSV.DATEFORMAT)}))

      total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
      total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
      total_saving = filtered_df[filtered_df["Category"] == "Saving"]["Amount"].sum()
      print("\nSummary:")
      print(f"Total Income: ${total_income:.2f}")
      print(f"Total Expenses: ${total_expense:.2f}")
      print(f"Total Emergency Savings: ${total_saving:.2f}")
      print(f"Net Savings: ${(total_income - total_expense - total_saving):.2f}")

    return filtered_df

  @classmethod
  def get_total_per_category(cls, category, start_date, end_date):
    df = pd.read_csv(cls.CSV_FILE)
    df["Date"] = pd.to_datetime(df["Date"], format=CSV.DATEFORMAT)
    start_date = datetime.strptime(start_date, CSV.DATEFORMAT)
    end_date = datetime.strptime(end_date, CSV.DATEFORMAT)

    mask = (df["Date"] >= start_date) & (df["Date"] <= end_date)
    filtered_df = df.loc[mask]

    if filtered_df.empty:
      print('No transactions found in the given date range')
    else:
      print(f"Total {category} from {start_date.strftime(CSV.DATEFORMAT)} to {end_date.strftime(CSV.DATEFORMAT)}")

      if category == "Income":
        total_income = filtered_df[filtered_df["Category"] == "Income"]["Amount"].sum()
        print(f"Total Income: ${total_income:.2f}")
      elif category == "Expense":
        total_expense = filtered_df[filtered_df["Category"] == "Expense"]["Amount"].sum()
        print(f"Total Expenses: ${total_expense:.2f}")
      elif category == "Emergency Saving":
        total_saving = filtered_df[filtered_df["Category"] == "Saving"]["Amount"].sum()
        print(f"Total Emergency Savings: ${total_saving:.2f}")

      return filtered_df

def add_finance_data():
  CSV.initialize_csv()
  date = get_date("Enter the date of the transaction (dd-mm-yyyy) or press 'Enter' for today's date: ", allow_default=True)
  amount = get_amount()
  category = get_category()
  description = get_description()
  CSV.add_entry(date, amount, category, description)

def main():
  while True:
    print("\n1. Add a new transaction")
    print("2. View transactions and summary within a date range")
    print("3. View the total for a category")
    print("0. Exit")
    choice = input("Enter your choice (1, 2, 3 or 0): ")

    if choice == "1":
      add_finance_data()
    elif choice == "2":
      start_date = get_date("Enter the start date (dd-mm-yyy) or press 'Enter' to start from the first day of this month: ", use_first_day_of_month=True)
      end_date = get_date("Enter the end date (dd-mm-yyy) or press 'Enter' for today's date: ", allow_default=True)
      df = CSV.get_transactions(start_date, end_date)
    elif choice == "3":
      category = get_category()
      start_date = get_date("Enter the start date (dd-mm-yyy) or press 'Enter' to start from the first day of this month: ", use_first_day_of_month=True)
      end_date = get_date("Enter the end date (dd-mm-yyy) or press 'Enter' for today's date: ", allow_default=True)
      df = CSV.get_total_per_category(category, start_date, end_date)
    elif choice == "0":
      print("Exiting...")
      break
    else:
      print("Invalid choice, enter values 1, 2, 3 or 4")

if __name__ == "__main__":
  main()

