from crewai import Task

def create_coverage_task(agent):
    return Task(
        description="Run coverage commands and return a detailed, human-readable report.",
        agent=agent,
        expected_output="Coverage summary + missing lines per file."
    )
