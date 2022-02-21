# from ..m_choice import *
import numpy as np
import re
import os
from numpy.testing import assert_equal, assert_allclose



d_pat = r'\d+.\d*'
let_pat = r'[A-Z]'
right_answers = [
    {'A', 'B', 'E'},
    {'A', 'C', 'E', 'F'},
    {'F'},
    {'F'},
    3.139e-19,
    5.996e14,
    2,
    2,
    {"A":2, "B":3, "C":1, "D":4},
    {"A":1, "B":2}
]

i = 0
score = 0
answer = '**Answer**'

path = os.getcwd()
with open(os.path.join(path, 'problem', 'm_choice.py'), 'r') as f:
    for line in f.readlines():
        if answer in line:

            true_answer = right_answers[i]

            ind = line.find(answer) + len(answer)
            new_line = line.upper()[ind:]
            answers_digits = [float(x) for x in re.findall(d_pat, new_line)]

            if isinstance(true_answer, dict):
                answers_letters = re.findall(let_pat, new_line)
                answer_dct = dict(zip(answers_letters, answers_digits))
                if answer_dct == true_answer:
                    score += 1

            else:
                answers_letters = set(re.findall(let_pat, new_line))
                if answers_letters == right_answers[i] or\
                    (len(answers_digits) > 0 and np.allclose(answers_digits, right_answers[i])):
                    score += 1
            i += 1


print(f"Your score is {score}/{len(right_answers)}")
assert(score == len(right_answers))


