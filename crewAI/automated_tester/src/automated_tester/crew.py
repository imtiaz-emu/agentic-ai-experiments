import typer
from crew.automated_tester_crew import AutomatedTesterCrew
from utils.repo_utils import prepare_repo_path

app = typer.Typer(help="Automated Tester Crew Runner")

@app.command()
def run(
    repo: str = typer.Option(..., "--repo", "-r", help="Git URL or local path to repository"),
    branch: str = typer.Option("main", "--branch", "-b", help="Branch to clone if using a Git URL"),
    test_dir: str = typer.Option(None, "--test-dir", "-td", help="Directory where to save the tests. If not specified, tests will be saved to <repo>/tests/")
):
    """
    Run the automated tester crew on either a local repository or a Git repository URL.
    """

    # Determine if it's local or remote, clone if required
    repo_path = prepare_repo_path(repo, branch)

    typer.echo(f"Repository location prepared: {repo_path}")

    crew_instance = AutomatedTesterCrew(repo_path, test_dir)
    crew = crew_instance.crew()
    result = crew.kickoff(inputs={
        "repo_path": repo_path,
        "test_dir": crew_instance.final_test_dir
    })

    typer.echo("\n=== FINAL OUTPUT ===")
    typer.echo(result)


if __name__ == "__main__":
    app()
