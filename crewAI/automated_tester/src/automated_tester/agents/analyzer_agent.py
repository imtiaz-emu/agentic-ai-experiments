from crewai import Agent
from tools.file_analyzer_tool import FileAnalyzerTool

def create_analyzer_agent():
    return Agent(
        role="Test Analyzer",
        goal="Identify which functions, modules, or routes require unit & integration tests.",
        backstory="You analyze code for test gaps.",
        tools=[FileAnalyzerTool()],
        allow_delegation=False,
        verbose=True,
    )
