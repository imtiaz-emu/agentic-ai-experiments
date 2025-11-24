# tasks/tester_task.py
from crewai import Task

def create_tester_task(agent):
    return Task(
        name="Generate Test Cases",
        description=(
            "Write pytest test files for all testable functions. "
            "The test directory is provided in the inputs as 'test_dir'."
        ),
        expected_output="Complete test files saved to the target directory.",
        agent_role="Test Writer",
        agent=agent,
        inputs=["repo_path", "test_dir"],
    )
