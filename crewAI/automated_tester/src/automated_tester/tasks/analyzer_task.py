from crewai import Task

def create_analyzer_task(agent):
    return Task(
        description="Analyze loaded files and identify all testable functions, classes, endpoints, and modules.",
        agent=agent,
        expected_output="A list of test targets with reasoning.",
    )
