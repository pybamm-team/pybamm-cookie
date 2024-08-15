import copier
import argparse
from pathlib import Path
from colorama import Fore
import os

project_root = Path(__file__).resolve().parent.parent
TEMPLATE = str(project_root)

def pybamm_cookie_cli():
    """
    Command Line Interface (CLI) for generating PyBaMM based projects using copier.

    Parameters
    ----------
    --path: pathlib.Path

    Examples
    -------
    $ pybamm-cookie
    Generates a project in the current working directory of the terminal.
    $ pybamm-cookie --path /myproject
    Generates a project in the `myproject` directory.
    """
    try:
        parser = argparse.ArgumentParser(description = "A copier template generator for PyBaMM based projects")
        parser.add_argument(
            "--path", type = str,
            required = False,
            default = os.getcwd(),
            help = "The destination path for project generation. The default is the current working directory"
        )

        from pybamm_cookie import __version__ as version
        parser.add_argument(
            '--version',
            action='version',
            version=f'pybamm-cookie CLI Version - {version}'
        )

        parser.add_argument(
            "--defaults",
            action="store_true",
            help="Whether to use default options for generating the template"
        )
        args = parser.parse_args()
        destination_path = Path(args.path)

        with copier.Worker(src_path = TEMPLATE, dst_path = destination_path, unsafe = True, defaults = args.defaults) as worker:
            worker.run_copy()

    except KeyboardInterrupt:
        print(Fore.RED + "Execution stopped by the user" + Fore.RESET)
    except Exception as error:
        print(Fore.RED + "Error caused by an exception: " + Fore.RESET, error)
        print(Fore.CYAN + "If you are unsure what the error is, feel free to open an issue at" + Fore.YELLOW +" - https://github.com/pybamm-team/pybamm-cookie/issues" + Fore.RESET)

if __name__ == '__main__':

    pybamm_cookie_cli()
