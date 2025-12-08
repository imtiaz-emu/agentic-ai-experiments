# tasks/tester_task.py
from crewai import Task

def create_tester_task(agent, test_dir):
    return Task(
        name="Generate Test Cases",
        description=(
            f"Write pytest test files for all testable functions. "
            f"You MUST use the file_writer tool to save each test file. "
            f"All test files MUST be saved to this directory: {test_dir}. "
            f"Create appropriate subdirectories matching the source code structure. "
            f"For example, if testing 'src/myapp/utils.py', create '{test_dir}/test_utils.py' or '{test_dir}/myapp/test_utils.py'."
        ),
        expected_output=f"Complete test files written using file_writer tool and saved to {test_dir}. List all created file paths.",
        agent_role="Test Writer",
        agent=agent,
        inputs=["repo_path", "test_dir"],
    )
