import os
from pathlib import Path
from crewai.tools import BaseTool
from pydantic import Field

class FileWriterTool(BaseTool):
    name: str = "file_writer"
    description: str = "Writes content to a file at the specified path. Creates directories if they don't exist."
    
    test_dir: str = Field(..., description="Base directory where test files should be written")

    def _run(self, file_path: str, content: str, **kwargs) -> str:
        """
        Write content to a file.
        
        Args:
            file_path: Relative path from test_dir where the file should be written
            content: The content to write to the file
            
        Returns:
            Success message with the full path where file was written
        """
        try:
            # Ensure file_path is relative and construct full path
            if os.path.isabs(file_path):
                # If absolute path is provided, use it as-is
                full_path = file_path
            else:
                # Otherwise, make it relative to test_dir
                full_path = os.path.join(self.test_dir, file_path)
            
            # Create directory structure if it doesn't exist
            directory = os.path.dirname(full_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            
            # Write the file
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            
            return f"Successfully wrote file to: {full_path}"
        except Exception as e:
            return f"Error writing file: {str(e)}"
