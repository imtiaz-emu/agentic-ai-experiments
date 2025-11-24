# pytest_task.py
from crewai import Task

def create_pytest_task(agent):
    """
    Task that instructs the pytest runner agent to execute pytest inside the repo.
    Returns a Task object that the Crew orchestration can use.
    """

    return Task(
        description=(
            "Run pytest in the repository root. Capture stdout/stderr, parse the "
            "number of passed/failed tests, and return a structured summary "
            "including any failing test names and stack traces."
        ),
        agent=agent,
        expected_output=(
            "A dict-like summary: { passed: int, failed: int, errors: list, "
            "failures: list, stdout: str, stderr: str }"
        )
    )
