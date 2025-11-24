# Agentic AI Experiments

This repository is a collection of hands-on experiments and prototypes exploring the latest in **agentic AI**—autonomous, multi-agent, and tool-using systems. Here, you'll find projects and code samples that leverage leading frameworks and techniques for building, orchestrating, and evaluating AI agents.

## What You'll Find

- **Multi-Agent Systems**: Experiments with frameworks like [CrewAI](https://github.com/joaomdmoura/crewAI), [Autogen](https://github.com/microsoft/autogen), [LangGraph](https://github.com/langchain-ai/langgraph), and the [OpenAI SDK](https://github.com/openai/openai-python) to build collaborative, specialized AI agents.
- **Automated Testing Agents**: A full-featured, multi-agent pipeline (see `crewAI/automated_tester/`) that loads codebases, analyzes for test targets, generates and runs tests, and produces coverage reports—all autonomously.
- **Retrieval-Augmented Generation (RAG)**: Prototypes and utilities for combining LLMs with external knowledge, using retrieval and context injection to improve factuality and reasoning.
- **Model Context Protocol (MCP)**: Early explorations and utilities for the emerging MCP standard, enabling more robust, interoperable agent workflows.
- **Jupyter Notebooks & Demos**: Interactive notebooks for deep research, rapid prototyping, and sharing insights.

## Frameworks & Technologies

- **CrewAI**: Multi-agent orchestration and task pipelines
- **OpenAI SDK**: Direct LLM and tool API access
- **Autogen**: Automated agent conversations and workflows
- **LangGraph**: Graph-based agent orchestration
- **RAG**: Retrieval-augmented generation patterns
- **MCP**: Model Context Protocol for agent interoperability

## Example: Automated Test Generator (CrewAI)

A highlight of this repo is the [Automated Test Generator](./crewAI/automated_tester/), a multi-agent system that:

1. Loads a project repository (local or remote)
2. Analyzes source files for testable units
3. Generates unit/integration tests
4. Runs tests and collects results
5. Produces coverage reports

All agents run locally, and the system is Docker-ready for privacy and reproducibility.

## Getting Started

- Each experiment or project has its own folder and README with setup instructions.
- Most projects require Python 3.10+ and an OpenAI API key (see `.env` setup).
- For the automated tester, see [`crewAI/automated_tester/README.md`](./crewAI/automated_tester/README.md).

## Why Agentic AI?

Agentic AI is about building systems where multiple AI agents—each with specialized roles, tools, and autonomy—work together to solve complex tasks. This repo is a playground for:

- Testing new agent frameworks and orchestration patterns
- Exploring RAG, tool use, and context management
- Prototyping real-world agent workflows (testing, research, automation, etc.)
- Contributing to the open agentic AI ecosystem

---

**This repository is a living lab.** New experiments, frameworks, and ideas will be added over time. Contributions and suggestions are welcome!
