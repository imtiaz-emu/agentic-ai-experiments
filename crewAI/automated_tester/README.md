# 🧪 Automated Test Generator (CrewAI)

An autonomous multi-agent application built with **CrewAI** to automatically:

1. Load a project repository (local path or Git URL)  
2. Analyze source files to identify testable units  
3. Generate unit and integration tests  
4. Execute the tests using `pytest`  
5. Generate coverage reports  
6. Deliver complete results locally

Everything runs **locally** and can be executed via **Docker**, ensuring privacy and security.

---

## 🚀 Features

### ✔️ Multi-agent architecture
The system uses a sequential pipeline of specialized agents:

| Agent | Purpose |
|-------|---------|
| **Loader Agent** | Loads repo files into memory. |
| **Analyzer Agent** | Identifies testable modules/functions. |
| **Tester Agent** | Generates pytest test files. |
| **Test Runner Agent** | Executes tests using `pytest`. |
| **Coverage Agent** | Generates coverage reports using `coverage.py`. |

---

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv: check guides

```bash
pip install uv
```

The parent folder of this repository already have a `uv.lock` file. So, once you've installed the UV locally, just run `uv sync` from the parent repository. The virual env will be created. Select the virtualenv as this project's Project interpreter.

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

Create a `.env` file in the root directory of this repo. It'll be served as the config file for all the projects. Add additional key/secrets in here.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ python crew.py --repo git@github.com:BaseMax/SimpleFastPyAPI.git --branch main --test-dir ~/tests
# or if you want to generate tests for your local repo
$ python crew.py --repo /path/to/your/project/ --test-dir ~/tests
```

This command initializes the automated-tester Crew, assembling the agents and assigning them tasks as defined in your configuration.

## Using Docker

1. Step 1 — Build the image

`docker build -t qa-crew .`

2. Step 2 — Run using docker-compose

`docker compose up`

3. Step 3 — Passing CLI args manually

```bash
docker run \
  -e OPENAI_API_KEY=$OPENAI_API_KEY \
  -v /path/to/your/repo:/repo \
  qa-crew \
  --repo /repo \
  --branch main \
  --test_dir /repo/mytests \
```


## Enhancements

1. Now the test cases will be generated, but it'll fail to execute the pytests if the required libraries are not installed. Same goes for coverage. We'll add Automatic detection of missing test dependencies.
2. Support for multi-language test generation (JS, Go, C#)
