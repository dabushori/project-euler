"""
Generate a challenge solution script from the template

@author Ori Dabush
"""
from argparse import ArgumentParser
from os.path import join, dirname


SOLUTION_FILE_NAME = 'solution.py'
SOLUTION_TEMPLATE_FILE_NAME = join(dirname(__file__), 'template.py')


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('challenge_number', type=int)
    parser.add_argument('challenge_description', type=str)
    return parser.parse_args()


def main():
    args = parse_args()
    with open(SOLUTION_TEMPLATE_FILE_NAME, 'r') as template_file:
        template = template_file.read()
    with open(f'problem_{args.challenge_number}.py', 'w') as solution_script:
        solution_script.write(template.format(args.challenge_number, args.challenge_description))


if __name__ == '__main__':
    main()
