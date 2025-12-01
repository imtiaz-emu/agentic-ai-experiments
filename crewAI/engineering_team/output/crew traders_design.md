# Crew Traders: Design Overview

This document outlines the detailed design for the backend system of a trading simulation platform named "Crew Traders." This system is intended to manage user accounts, handle trading operations, and calculate performance metrics, simulating a real-world trading environment.

## Folder Structure

```
crew_traders/
│
├── main.py
├── app/
│   ├── __init__.py
│   ├── account.py
│   ├── portfolio.py
│   ├── orders.py
│   ├── transactions.py
│   └── utils.py
│
├── models/
│   ├── __init__.py
│   ├── account_model.py
│   ├── transaction_model.py
│   ├── portfolio_model.py
│   └── order_model.py
│
├── db/
│   ├── __init__.py
│   ├── database.py
│   └── models.py
│
├── services/
│   ├── __init__.py
│   └── share_price_service.py
│
└── tests/
    ├── test_account.py
    ├── test_portfolio.py
    ├── test_orders.py
    └── test_transactions.py
```

## Module Overview

### 1. `app/`

- **`account.py`**: Contains logic for account management such as creating an account, depositing, and withdrawing funds.
- **`portfolio.py`**: Manages the user's portfolio data, calculating total value and profit/loss.
- **`orders.py`**: Handles order execution logic, including Market and Limit Orders.
- **`transactions.py`**: Logs transactions and provides reports on user transactions.
- **`utils.py`**: Contains utility functions such as error handling and calculations for fees.

### 2. `models/`

Define the data models to be used within the application, including ORM models.

- **`account_model.py`**: Defines the Account model.
- **`transaction_model.py`**: Defines the Transaction model.
- **`portfolio_model.py`**: Defines the Portfolio model.
- **`order_model.py`**: Defines the Order model.

### 3. `db/`

Handles database interactions and ORM setup.

- **`database.py`**: Manages the database connection and session.
- **`models.py`**: Contains all ORM models to map the database tables.

### 4. `services/`

- **`share_price_service.py`**: Simulates share price retrieval via `get_share_price(symbol)`.

### 5. `tests/`

Contains unit tests for each module.

## Classes and Methods

### app/account.py

```python
class AccountManager:
    def create_account(self, user_id: int) -> Account:
        """Creates a new account for a user."""

    def deposit_funds(self, user_id: int, amount: float) -> None:
        """Deposits funds into a user's account."""

    def withdraw_funds(self, user_id: int, amount: float) -> None:
        """Withdraws funds from a user's account ensuring non-negative balance."""
```

### app/portfolio.py

```python
class PortfolioManager:
    def calculate_total_value(self, user_id: int) -> float:
        """Calculates and returns the total value of a user's portfolio."""

    def calculate_profit_loss(self, user_id: int) -> float:
        """Calculates and returns the profit/loss of a user's portfolio from initial deposit."""

    def report_holdings(self, user_id: int) -> dict:
        """Reports user's holdings at any point in time."""
```

### app/orders.py

```python
class OrderManager:
    def execute_market_order(self, user_id: int, symbol: str, quantity: int) -> None:
        """Executes a Market Order for the specified quantity of shares."""

    def execute_limit_order(self, user_id: int, symbol: str, quantity: int, limit_price: float) -> None:
        """Places a Limit Order that executes if the limit price is met or better."""
```

### app/transactions.py

```python
class TransactionManager:
    def log_transaction(self, user_id: int, type: str, details: dict) -> None:
        """Logs a transaction performed by the user."""

    def list_transactions(self, user_id: int) -> list:
        """Lists all transactions made by the user over time."""
```

### Database Schema

```sql
CREATE TABLE Account (
    id SERIAL PRIMARY KEY,
    user_id INTEGER UNIQUE NOT NULL,
    balance DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Transaction (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    transaction_type VARCHAR(50) NOT NULL,
    details JSONB NOT NULL,
    timestamp TIMESTAMPTZ DEFAULT NOW()
);

CREATE TABLE Portfolio (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    quantity INTEGER NOT NULL,
    average_price DECIMAL(10, 2) NOT NULL
);

CREATE TABLE Order (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    symbol VARCHAR(10) NOT NULL,
    order_type VARCHAR(10) NOT NULL,
    quantity INTEGER,
    limit_price DECIMAL(10, 2),
    status VARCHAR(20) DEFAULT 'Pending',
    created_at TIMESTAMPTZ DEFAULT NOW()
);
```

### Scalability, Maintainability, and Performance Considerations

- **Scalability**: The system is modularized allowing easy expansion, e.g., support for more order types or new financial instruments.
- **Maintainability**: Organized code structure with clear separations of concerns, appropriate comments, and documentation.
- **Performance**: Efficient database accesses through optimized queries and appropriate data indexing.

This design provides a solid foundation for implementing a trading simulation platform using frameworks such as FastAPI or Flask. Developers are advised to use appropriate error handling and extend this design as needed to meet additional functional requirements.