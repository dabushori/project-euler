import os

SOLUTIONS_PER_DIR = 100

def get_solution_dir(solution_number: int) -> str:
    first = solution_number - solution_number % SOLUTIONS_PER_DIR + 1
    last = first + SOLUTIONS_PER_DIR - 1
    return f'solutions_{first}_to_{last}'

def get_solution_module(solution_number: int) -> str:
    return f'{get_solution_dir(solution_number)}.solution_{solution_number}'

def get_solution_file(solution_number: int) -> str:
    return os.path.join('solutions', f'{get_solution_dir(solution_number)}', f'solution_{solution_number}.py')
