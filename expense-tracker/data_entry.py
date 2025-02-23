from datetime import datetime

date_format = "%d-%m-%Y"
CATEGORIES = { "I": "Income", "E": "Expense", "S": "Emergency Saving" }

def get_date(prompt, allow_default=False, use_first_day_of_month=False):
  date_str = input(prompt)
  if allow_default and not date_str:
    return datetime.today().strftime(date_format)

  if use_first_day_of_month and not date_str:
    today = datetime.today()
    first_day = f"01-{today.month:02d}-{today.year}"
    return first_day

  try:
    valid_date = datetime.strptime(date_str, date_format)
    return valid_date.strftime(date_format)
  except ValueError:
    print("Invalid date format. Enter the date in dd-mm-yyyy format")
    return get_date(prompt, allow_default)

def get_amount():
  try:
    amount = float(input("Enter the amount: "))
    if amount <= 0:
      raise ValueError("Amount must be a non-negative non-zero value")
    return amount
  except ValueError as e:
    print(e)
    return get_amount()

def get_category():
  category = input("Enter the category ('I' for income or 'E' for expense or 'S' for emergency saving): ").upper()
  if category in CATEGORIES:
    return CATEGORIES[category]
  
  print("Invalid category. Enter 'I' for Income or 'E' for Expense or 'S' for emergency saving.")
  return get_category()

def get_description():
  return input("Enter a description (optiional): ")
