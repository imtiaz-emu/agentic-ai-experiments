from crewai import Crew, Process

from agents.loader_agent import create_loader_agent
from agents.analyzer_agent import create_analyzer_agent
from agents.tester_agent import create_tester_agent
from agents.test_runner_agent import create_pytest_runner_agent
from agents.coverage_agent import create_coverage_agent

from tasks.loader_task import create_loader_task
from tasks.analyzer_task import create_analyzer_task
from tasks.tester_task import create_tester_task
from tasks.pytest_task import create_pytest_task
from tasks.coverage_task import create_coverage_task


class AutomatedTesterCrew:
    def __init__(self, repo_path: str, test_dir: str):
        self.repo_path = repo_path
        self.test_dir = test_dir
        
    def crew(self):
        # default test directory = <repo_path>/tests/
        final_test_dir = (
            self.test_dir if self.test_dir
            else f"{self.repo_path.rstrip('/')}/tests"
        )
        
        loader = create_loader_agent(self.repo_path)
        analyzer = create_analyzer_agent()
        tester = create_tester_agent(final_test_dir)
        runner = create_pytest_runner_agent(self.repo_path)
        coverage = create_coverage_agent(self.repo_path)

        t1 = create_loader_task(loader, self.repo_path)
        t2 = create_analyzer_task(analyzer)
        t3 = create_tester_task(tester)
        t4 = create_pytest_task(runner)
        t5 = create_coverage_task(coverage)
        
        return Crew(
            agents=[
                loader,
                analyzer,
                tester,
                runner,
                coverage,
            ],
            tasks=[
                t1, t2, t3, t4, t5,
            ],
            process=Process.sequential,
            verbose=True
        )

        
