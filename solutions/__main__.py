import argparse
from solutions.utils.solutions import get_solution_module
from solutions.template.generate_challenge import generate_solution

def parse_args():
    parser = argparse.ArgumentParser('Run Project Euler Solution')
    parser.add_argument('challenge_number', type=int)
    parser.add_argument('-g', '--generate', required=False, action='store_true')
    parser.add_argument('-d', '--description', required=False)
    return parser.parse_args()

def main():
    args = parse_args()
    if args.generate:
        generate_solution(args.challenge_number, args.description)
    else:
        solution_module = get_solution_module(args.challenge_number)
        exec('\n'.join((
            f"from .{solution_module} import main",
            "main()"
        )))

if __name__ == '__main__':
    main()
