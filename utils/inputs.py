from os.path import join


INPUTS_DIRECTORY = "inputs"
INPUTS_FORMAT = "problem_{}.txt"


def get_input(problem_number: int) -> str:
    with open(join(INPUTS_DIRECTORY, INPUTS_FORMAT.format(problem_number)), 'r') as input_file:
        return input_file.read()
