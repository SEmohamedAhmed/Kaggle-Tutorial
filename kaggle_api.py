"""
    DO NOT FORGET TO
        - pip install kaggle
        - download your json auth token from your kaggle account settings
        - put kaggle.json in the directory like:  "C:\Users\MrMody\.kaggle"
    For more details see this kaggle doc "https://github.com/Kaggle/kaggle-api/blob/main/docs/README.md"
"""

import subprocess

project_path = r'WRITE_YOUR_PROJECT_PATH_HERE'
nb_id = 'WRITE_YOUR_NOTEBOOK_ID_HERE'


def execute_terminal_command(command):
    # Execute the command
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    # Print the output of the command
    return result.stdout


def init_kaggle_dataset():
    command = fr'kaggle datasets init -p {project_path}\dataset'
    return execute_terminal_command(command)


def create_kaggle_dataset():
    command = fr'kaggle datasets create -p {project_path}\dataset -r tar'
    return execute_terminal_command(command)


def pull_kaggle_dataset(dataset_id):
    command = fr'kaggle datasets metadata -p {project_path}\dataset {dataset_id}'
    return execute_terminal_command(command)


def update_kaggle_dataset():
    command = fr'kaggle datasets version -p {project_path}\dataset -m "Updated dataset using kaggle API 2024" -r tar'
    return execute_terminal_command(command)


def pull_kaggle_notebook(notebook_id):
    command = fr'kaggle kernels pull {notebook_id} -p {project_path}\notebook -m'
    return execute_terminal_command(command)


def push_kaggle_notebook():
    command = fr'kaggle kernels push -p {project_path}\notebook'
    return execute_terminal_command(command)


def get_notebook_status(notebook_id):
    command = fr'kaggle kernels status {notebook_id}'
    return execute_terminal_command(command)


def get_notebook_output(notebook_id):
    command = fr'kaggle kernels output {notebook_id} -p {project_path}\nb_output'
    return execute_terminal_command(command)
