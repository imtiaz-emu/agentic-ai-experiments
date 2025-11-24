from crewai import Task

def create_loader_task(agent, repo_path):
    return Task(
        description=f"Load all readable source code files from {repo_path} and return a clean structure.",
        agent=agent,
        expected_output="A structured list of file paths and file contents.",
    )
