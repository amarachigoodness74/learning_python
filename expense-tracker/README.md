# CLI Finance Tracker App

A simple command-line finance tracker to log and manage income, expenses, and emergency savings. The app provides balance calculations, transaction history, and summary reports while ensuring data persistence in a CSV file.

## Features

### Core Features

- **Finance Tracking** – Log income and expenses with details like amount, category, date, and description.
- **Categories** – Categorize transactions (e.g., Income, Expense, Emergency Saving).
- **Balance Calculation** – Calculate total balance based on income, expenses, and emergency savings.
- **Transaction History** – View past transactions with filtering options by date.
- **Reports & Summaries** – Generate financial summaries (e.g., total expenses per category, savings over time).

### CLI Usability Features

- **Intuitive Commands** – Simple and clear commands like `Add a new transaction`, `View transactions and summary within a date range`, `View the total for a category`, `Exit`.
- **Search & Filters** – Find transactions by date or category.
- **Data Persistence** – Store data in a CSV file to ensure it remains available between sessions.
- **Error Handling** – Gracefully handle invalid inputs.

## Usage

### Adding a Transaction

```sh
python main.py
```

Type 1 and Follow the prompt to make a choice

### Viewing Transactions

```sh
python main.py
```

Type 2 and Follow the prompt to make a choice

### Generating a Report based on category and date range

```sh
python main.py
```

Type 3 and Follow the prompt to make a choice

### To Exot

```sh
python main.py
```

Type 0

## Data Storage

- All transactions are stored in a CSV file (`finance_data.csv`).
- The file is automatically updated when a transaction is added.

## Future Improvements

- Add recurring transactions feature.
- Implement budgeting functionality.
- Introduce goal-based savings.
- Add functionality to remove transaction.

## License

This project is licensed under the MIT License.

## Author

Developed by [Amarachi Goodness](https://github.com/amarachigoodness74/learning_python/tree/main/expense-tracker).
