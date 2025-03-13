from datetime import datetime


def main():
    # Get valid year input
    while True:
        year = input("What year were you born? ")
        if year.isdigit():
            year = int(year)
            if 1900 <= year <= datetime.today().year:
                break
            else:
                print("Please enter a valid year (1900 - current year).")
        else:
            print("Invalid input. Please enter a valid year.")

    # Get valid month input
    while True:
        month = input("What month were you born? (1 - 12): ")
        if month.isdigit():
            month = int(month)
            if 1 <= month <= 12:
                break
            else:
                print("Invalid month. Please enter a number between 1 and 12.")
        else:
            print("Invalid input. Please enter a number.")

    # Get current date
    current_year = datetime.today().year
    current_month = datetime.today().month

    # Calculate age
    age = current_year - year
    if month > current_month:
        age -= 1

    # Output result
    print(f'You are {age} years old now.')

if __name__ == "__main__":
    main()
