import copier
import argparse
from pathlib import Path
from colorama import Fore
import os

project_root = Path(__file__).resolve().parent.parent
TEMPLATE = str(project_root)

def pybamm_cookiecutter_cli():
    """
    Command Line Interface (CLI) for generating PyBaMM based projects using copier.

    Parameters
    ----------
    --path: pathlib.Path

    Examples
    -------
    $ pybamm-cookiecutter
    Generates a project in the current working directory of the terminal.
    $ pybamm-cookiecutter --path /myproject
    Generates a project in the `myproject` directory.
    """
    try:
        parser = argparse.ArgumentParser(description = "A copier template generator for PyBaMM based projects")
        parser.add_argument("--path", type = str, required = False, default = os.getcwd(),
                            help = "The destination path for project generation. The default is the current working directory")

        args = parser.parse_args()
        destination_path = Path(args.path)

        copier.run_copy(src_path = TEMPLATE, dst_path = destination_path, unsafe=True)

    except KeyboardInterrupt:
        print("Execution stopped by the user")
    except Exception as error:
        print(Fore.RED + "Error caused by an exception: " + Fore.RESET, error)
        print(Fore.CYAN + "If you are unsure what the error is, feel free to open an issue at" + Fore.YELLOW +" - https://github.com/pybamm-team/pybamm-cookiecutter/issues" + Fore.RESET)

if __name__ == '__main__':

    pybamm_cookiecutter_cli()
