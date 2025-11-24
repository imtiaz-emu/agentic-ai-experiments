import subprocess
from crewai.tools import BaseTool
from pydantic import Field

class PytestRunnerTool(BaseTool):
    name: str = "pytest_runner"
    description: str = "Runs pytest inside the repo and returns the output."
    repo_path: str = Field(..., description="Path to the repository to run the pytests")

    def _run(self, **kwargs):
        try:
            result = subprocess.run(
                ["pytest", "-q"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )
            return result.stdout + result.stderr
        except FileNotFoundError:
            return "Pytest is not installed in the environment."
