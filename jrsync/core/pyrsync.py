import subprocess

DEFAULT_RSYNC_OPTS = "-aP"


def rsync(source, destination, options=None):
    if options is None:
        options = DEFAULT_RSYNC_OPTS

    # Base rsync command
    command = ["rsync", options]

    # Add source and destination to the command
    command.extend([source, destination])

    try:
        # Run the rsync command
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
