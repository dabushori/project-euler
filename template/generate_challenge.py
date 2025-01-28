"""
Generate a challenge solution script from the template

@author Ori Dabush
"""

from argparse import ArgumentParser
from os.path import join, dirname
from bs4 import BeautifulSoup
import requests

SOLUTION_FILE_NAME = 'solution.py'
SOLUTION_TEMPLATE_FILE_NAME = join(dirname(__file__), 'template.py')


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('challenge_number', type=int)
    parser.add_argument('-d', '--description', type=str, required=False)
    args = parser.parse_args()
    if args.description is None:
        # Fetch the description from the website if not given
        url = f'https://projecteuler.net/problem={args.challenge_number}'
        response = requests.get(url, allow_redirects=False)
        if response.status_code != 200:
            raise Exception(f'Failed fetching challenge description: {response} ({response.content})')
        html_parser = BeautifulSoup(response.content.decode(), 'html.parser')
        args.description = html_parser.find('h2').text
    return args


def main():
    args = parse_args()
    with open(SOLUTION_TEMPLATE_FILE_NAME, 'r') as template_file:
        template = template_file.read()
    with open(f'problem_{args.challenge_number}.py', 'w') as solution_script:
        solution_script.write(template.format(args.challenge_number, args.description))


if __name__ == '__main__':
    main()
