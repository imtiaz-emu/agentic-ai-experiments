from crewai import Agent
from tools.file_writer_tool import FileWriterTool

def create_tester_agent(test_dir: str):
    return Agent(
        role="Test Writer",
        goal=(
            "Generate high-quality pytest unit and integration tests "
            "and save them into the specified test directory following a decent dir tree."
        ),
        backstory=(
            "You write clean and complete tests. Use the file_writer tool to save tests."
        ),
        tools=[FileWriterTool(test_dir=test_dir)],
        allow_delegation=False,
        allow_code_execution=True,
        max_retry_limit=3,
        verbose=True,
        memory=True,
        extra_instructions=f"You MUST use the file_writer tool to write test files. The tests must be written inside: {test_dir}"
    )
