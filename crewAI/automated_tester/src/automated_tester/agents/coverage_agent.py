from crewai import Agent
from tools.coverage_runner_tool import CoverageRunnerTool

def create_coverage_agent(repo_path: str):
    return Agent(
        role="Coverage Reporter",
        goal="Run coverage analysis and produce a clean, detailed summary.",
        backstory="You measure coverage and highlight missing parts.",
        tools=[CoverageRunnerTool(repo_path=repo_path)],
        allow_delegation=False,
        verbose=True,
    )
