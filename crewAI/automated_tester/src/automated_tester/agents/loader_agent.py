from crewai import Agent
from tools.file_loader_tool import FileLoaderTool

def create_loader_agent(repo_path: str):
    return Agent(
        role="Repo Loader",
        goal="Load only relevant text/code files from the repository.",
        backstory="You carefully read the codebase without executing anything.",
        tools=[FileLoaderTool(repo_path=repo_path)],
        allow_delegation=False,
        verbose=True,
    )
