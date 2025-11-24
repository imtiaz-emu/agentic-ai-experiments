import subprocess
from crewai.tools import BaseTool
from pydantic import Field

class CoverageRunnerTool(BaseTool):
    name: str = "coverage_runner"
    description: str = "Generates coverage report using 'coverage run' and 'coverage report'."

    repo_path: str = Field(..., description="Path to the repository to collect the coverage report")

    def _run(self, **kwargs):
        try:
            run_cmd = subprocess.run(
                ["coverage", "run", "-m", "pytest"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            report_cmd = subprocess.run(
                ["coverage", "report"],
                cwd=self.repo_path,
                capture_output=True,
                text=True
            )

            return run_cmd.stdout + run_cmd.stderr + "\n\n" + report_cmd.stdout
        except FileNotFoundError:
            return "Coverage is not installed in the environment."
