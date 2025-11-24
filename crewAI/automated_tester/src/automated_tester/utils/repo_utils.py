import os
import shutil
import tempfile
import subprocess


def is_git_url(s: str) -> bool:
    return s.startswith("http://") or s.startswith("https://") or s.endswith(".git")


def prepare_repo_path(repo: str, branch: str) -> str:
    """
    If repo is local: return absolute path.
    If repo is a Git URL: clone it into a temp directory and return that path.
    """

    # Case 1: Local directory
    if os.path.exists(repo) and os.path.isdir(repo):
        return os.path.abspath(repo)

    # Case 2: Remote Git URL
    if is_git_url(repo):
        tmp = tempfile.mkdtemp(prefix="repo_")
        clone_cmd = ["git", "clone", "--branch", branch, repo, tmp]

        try:
            subprocess.check_output(clone_cmd, stderr=subprocess.STDOUT)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Git clone failed:\n{e.output.decode()}")

        return tmp

    raise ValueError("Invalid repo input. Must be a local folder or Git URL.")
