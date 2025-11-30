import warnings
import os

from engineering_team.crew import EngineeringTeam

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# Create output directory if it doesn't exist
os.makedirs('output', exist_ok=True)

requirements = """
A simple account management system for a trading simulation platform.
The system should allow users to create an account, deposit funds, and withdraw funds.
The system should allow users to record that they have bought or sold shares, providing a quantity.
The system should calculate the total value of the user's portfolio, and the profit or loss from the initial deposit.
The system should be able to report the holdings of the user at any point in time.
The system should be able to report the profit or loss of the user at any point in time.
The system should be able to list the transactions that the user has made over time.
The system should prevent the user from withdrawing funds that would leave them with a negative balance, or
 from buying more shares than they can afford, or selling shares that they don't have.
 The system has access to a function get_share_price(symbol) which returns the current price of a share, 
 and includes a test implementation that returns random but realistic prices for AAPL, GOOGL, NVDA, AMZN, MSFT, ORCL.
The system should have 2 basic types of Orders: Market Orders and Limit Orders.
Market Order: Execute a trade immediately at the current market price.
Limit Order: Execute a trade only if the price reaches a specified or better level.
Transactions must incorporate simulated brokerage commissions and regulatory fees to reflect real-world trading costs and impact performance metrics. For now, use some fixed prices.
"""
service_name = "crew traders"


def run():
    """
    Run the research crew.
    """
    inputs = {
        'requirements': requirements,
        'service_name': service_name,
    }

    # Create and run the crew
    result = EngineeringTeam().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()
    