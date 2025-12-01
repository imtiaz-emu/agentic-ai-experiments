from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class EngineeringTeam():
    """EngineeringTeam crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def engineering_lead(self) -> Agent:
        return Agent(
            config=self.agents_config['engineering_lead'], # type: ignore[index]
            verbose=True
        )

    @agent
    def backend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['backend_developer'], # type: ignore[index]
            verbose=True,
            allow_file_access=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_retry_limit=3,
        )
        
    @agent
    def frontend_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['frontend_developer'], # type: ignore[index]
            verbose=True,
            allow_file_access=True,
        )
        
    @agent
    def test_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['test_engineer'], # type: ignore[index]
            verbose=True,
            allow_file_access=True,
            allow_code_execution=True,
            code_execution_mode="safe",
            max_retry_limit=3,
        )
        
    @agent
    def devops_engineer(self) -> Agent:
        return Agent(
            config=self.agents_config['devops_engineer'], # type: ignore[index]
            verbose=True,
            allow_tool_use=True,
            allow_file_access=True,
        )

    @task
    def design_task(self) -> Task:
        return Task(
            config=self.tasks_config['design_task'], # type: ignore[index]
        )

    @task
    def code_task(self) -> Task:
        return Task(
            config=self.tasks_config['code_task'], # type: ignore[index]
            # TODO: Let's do a callback to verify the code via Enginnering Lead agent
            # callback=
        )
        
    @task
    def frontend_task(self) -> Task:
        return Task(
            config=self.tasks_config['frontend_task'], # type: ignore[index]
        )
    
    @task
    def test_task(self) -> Task:
        return Task(
            config=self.tasks_config['test_task'], # type: ignore[index]
        )
        
    @task
    def devops_task(self) -> Task:
        return Task(
            config=self.tasks_config['devops_task'], # type: ignore[index]
        )

    @crew
    def crew(self) -> Crew:
        """Creates the EngineeringTeam crew"""

        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
