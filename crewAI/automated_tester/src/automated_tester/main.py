# main.py

import argparse
import sys
from utils.repo_utils import prepare_repo_path
from crew.automated_tester_crew import AutomatedTesterCrew

def main():
    """
    Entrypoint for running the automated test generator pipeline.
    """

    parser = argparse.ArgumentParser(
        description="Automated Test Generator using CrewAI"
    )

    parser.add_argument(
        "--repo",
        required=True,
        help="Local repo path OR Git repo URL. Example: /Users/me/myapp OR https://github.com/user/app.git"
    )

    args = parser.parse_args()
    repo_input = args.repo

    print("🔍 Resolving repository location...")
    try:
        repo_path = prepare_repo_path(repo_input)
    except Exception as e:
        print(f"❌ Failed to resolve repository: {e}")
        sys.exit(1)

    print(f"📁 Repository ready at: {repo_path}")

    print("🚀 Initializing automated test generation crew...")
    crew = AutomatedTesterCrew(repo_path)

    print("🤖 Running the Crew pipeline...")
    try:
        result = crew.run()
    except Exception as e:
        print(f"❌ Crew execution failed: {e}")
        sys.exit(1)

    print("\n✅ Completed. Final Output:\n")
    print(result)


if __name__ == "__main__":
    main()
