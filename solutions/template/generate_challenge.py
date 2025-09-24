"""
Generate a challenge solution script from the template

@author Ori Dabush
"""

from argparse import ArgumentParser
from os.path import join, dirname, exists
from bs4 import BeautifulSoup
import requests
from ..utils.solutions import get_solution_file

SOLUTION_TEMPLATE_FILE_NAME = join(dirname(__file__), 'template.py')

def generate_solution(challenge_number, description):
    if description is None:
        # Fetch the description from the website if not given
        url = f'https://projecteuler.net/problem={challenge_number}'
        response = requests.get(url, allow_redirects=False)
        if response.status_code != 200:
            raise Exception(f'Failed fetching challenge description: {response} ({response.content})')
        html_parser = BeautifulSoup(response.content.decode(), 'html.parser')
        description = html_parser.find('h2').text
    with open(SOLUTION_TEMPLATE_FILE_NAME, 'r') as template_file:
        template = template_file.read()
    solution_file = get_solution_file(challenge_number)
    assert not exists(solution_file), f"Solution file already exists ({solution_file})"
    with open(get_solution_file(challenge_number), 'w') as solution_script:
        solution_script.write(template.format(challenge_number, description))
