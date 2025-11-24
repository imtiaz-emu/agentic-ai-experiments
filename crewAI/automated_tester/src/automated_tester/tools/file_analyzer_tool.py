from crewai.tools import BaseTool
import ast

class FileAnalyzerTool(BaseTool):
    name: str = "file_analyzer"
    description: str = "Analyzes Python files and identifies functions/classes to test."

    def _run(self, file_dict: dict):
        results = []

        for path, content in file_dict.items():
            if not path.endswith(".py"):
                continue

            try:
                tree = ast.parse(content)
            except SyntaxError:
                continue

            functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
            classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]

            if functions or classes:
                results.append({
                    "file": path,
                    "functions": functions,
                    "classes": classes
                })

        return results
