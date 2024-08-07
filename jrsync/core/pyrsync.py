import subprocess
from pathlib import Path

from jrsync.utils import str_validator

DEFAULT_RSYNC_OPTS = "-aP"


def rsync(
    src_path: Path,
    dst_path: Path,
    options=None,
    src_address: str = None,
    dst_address: str = None,
) -> None:
    if options is None:
        options = DEFAULT_RSYNC_OPTS

    # Base rsync command
    command = ["rsync", options]

    # add remote if present
    if str_validator.is_valid_address(src_address):
        src_path = f"{src_address}:{src_path}"
    if str_validator.is_valid_address(dst_address):
        dst_path = f"{dst_address}:{dst_path}"

    # Add source and destination to the command
    command.extend([src_path, dst_path])

    try:
        # Run the rsync command
        print(f"Running: {command}")
        exit(0)
        result = subprocess.run(command, check=True)

        # Print the output and return code
        print("Rsync command executed successfully.")
        print("Return code:", result.returncode)
        print("Output:", result.stdout)
        print("Errors:", result.stderr)

    except subprocess.CalledProcessError as e:
        # Handle errors in rsync command execution
        print("Error during rsync execution.")
        print("Return code:", e.returncode)
        print("Output:", e.output)
        print("Errors:", e.stderr)
    except Exception as e:
        # Handle other exceptions
        print("An unexpected error occurred:", str(e))
