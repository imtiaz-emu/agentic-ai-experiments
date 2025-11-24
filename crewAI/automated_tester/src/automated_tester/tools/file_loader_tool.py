import os
from crewai.tools import BaseTool
from pydantic import Field

class FileLoaderTool(BaseTool):
    name: str = "file_loader"
    description: str  = "Loads readable source files from a repo directory."
    repo_path: str = Field(..., description="Path to the repository to load files from")

    def _run(self, _=None):
        result = {}
        for root, _, files in os.walk(self.repo_path):
            for f in files:
                if f.endswith((".py", ".js", ".ts", ".go", ".java", ".rs", ".json", ".yaml", ".yml")):
                    abs_path = os.path.join(root, f)
                    try:
                        with open(abs_path, "r", encoding="utf-8", errors="ignore") as fp:
                            result[abs_path] = fp.read()
                    except:
                        pass
        return result
