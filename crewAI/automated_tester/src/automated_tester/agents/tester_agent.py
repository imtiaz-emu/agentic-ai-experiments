from crewai import Agent

def create_tester_agent(test_dir: str):
    return Agent(
        role="Test Writer",
        goal=(
            "Generate high-quality pytest unit and integration tests "
            "and save them into the specified test directory following a decect dir tree."
        ),
        backstory=(
            "You write clean and complete tests. Use the provided test directory."
        ),
        allow_delegation=False,
        verbose=True,
        memory=True,
        extra_instructions=f"The tests must be written inside: {test_dir}"
    )
