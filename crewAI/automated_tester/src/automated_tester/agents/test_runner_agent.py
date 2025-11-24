from crewai import Agent
from tools.pytest_runner_tool import PytestRunnerTool

def create_pytest_runner_agent(repo_path: str):
    return Agent(
        role="Test Executor",
        goal="Run pytest securely in isolated environment and return results.",
        backstory="You never access internet and only execute tests.",
        tools=[PytestRunnerTool(repo_path=repo_path)],
        allow_delegation=False,
        verbose=True,
    )
