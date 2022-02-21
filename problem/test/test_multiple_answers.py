# from ..m_choice import *
import numpy as np
import re
import os
from distutils.util import strtobool


dpat_int = r'\d+'
let_pat = r'[A-Z]'
right_answers = [
    {'A', 'B', 'E'},
    {'A', 'C', 'E', 'F'},
    False,
    False,
    3.139e-19,
    5.996e14,
    2.,
    2.,
    {"A":2, "B":3, "C":1, "D":4},
    {"A":1, "B":2}
]

i = 0
score = 0
answer = '**Answer'

path = os.getcwd()
with open(os.path.join(path, 'problem', 'm_choice.py'), 'r') as f:
    for line in f.readlines():
        if answer in line:

            true_answer = right_answers[i]

            ind = line.find(answer) + len(answer)

            if isinstance(true_answer, dict):
                new_line = line.upper()[ind:]
                answers_digits = [int(x) for x in re.findall(dpat_int, new_line)]

                answers_letters = re.findall(let_pat, new_line)
                answer_dct = dict(zip(answers_letters, answers_digits))
                if answer_dct == true_answer:
                    score += 1

            elif isinstance(true_answer, set):
                new_line = line.upper()[ind:]
                answers_letters = set(re.findall(let_pat, new_line))
                if answers_letters == true_answer:
                    score += 1

            elif isinstance(true_answer, float):
                new_line = line[ind:]
                ind = re.search(dpat_int, new_line).start()
                new_line = new_line[ind:].strip()

                answer_digit = float(new_line)
                if answer_digit == true_answer:
                    score += 1

            elif isinstance(true_answer, bool):
                new_line = line[ind:]
                ind = re.search(let_pat, new_line).start()
                answer_bool = strtobool(new_line[ind:].strip())
                if answer_bool == true_answer:
                    score += 1

            i += 1


print(f"Your score is {score}/{len(right_answers)}")
assert(score == len(right_answers))


