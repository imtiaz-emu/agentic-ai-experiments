# Engineering Team Crew

This project uses crewAI to create an engineering team that can build a simple account management system for a trading simulation platform.

## System Overview

The crew is tasked with building a system with the following features:
- User account creation, deposits, and withdrawals.
- Recording of share purchases and sales.
- Portfolio value calculation, including profit and loss.
- Reporting of user holdings, profit/loss, and transaction history.
- Prevention of negative balances, unaffordable purchases, and selling non-existent shares.
- Access to a `get_share_price(symbol)` function for real-time share prices.
- Support for Market and Limit orders.
- Simulated brokerage commissions and regulatory fees.

## Setup and Execution

This project uses Astral's `uv` for package management. All dependencies are listed in `pyproject.toml`.

### Prerequisites
- Python 3.10 or higher.
- `uv` installed. You can install it with `pip install uv`.

### Installation

1.  **Create a virtual environment and install dependencies:**
    ```bash
    uv venv
    uv pip install -r pyproject.toml
    ```

2.  **Set up your environment variables:**
    Create a `.env` file in the `engineering_team` directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY="your-openai-api-key"
    ```

### Running the Crew

To run the engineering team crew, execute the following command from the `engineering_team` directory:

```bash
uv run engineering_team
```

This will kick off the crew to start building the trading simulation system based on the defined requirements. The output will be generated in the `output` directory.
