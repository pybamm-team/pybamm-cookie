import subprocess

from pathlib import Path

def prepare_git() -> None:

    git_author_name = "{{cookiecutter.full_name}}"
    git_author_email = "{{cookiecutter.email}}"
    git_branch = "{{cookiecutter.branch}}"

    # Initialise git
    subprocess.call(
        ["git", "init", "-b", git_branch]
    )
    subprocess.call(
        ["git", "config", "user.name", git_author_name]
    )
    subprocess.call(
        ["git", "config", "user.email", git_author_email]
    )

if __name__ == "__main__":
    print("Executing script!!")
    prepare_git()
