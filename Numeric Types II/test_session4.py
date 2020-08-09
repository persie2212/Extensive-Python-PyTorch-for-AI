import pytest
import random
import string
import session4
import os
import inspect
import re
import math

x = 1
README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"
# def test_readme_contents():
#     readme_words=[word for line in open('README.md', 'r',encoding="utf-8") for word in line.split()]
#     assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 500 words"
#
# def test_readme_proper_description():
#     READMELOOKSGOOD = True
#     f = open("README.md", "r",encoding="utf-8")
#     content = f.read()
#     f.close()
#     for c in README_CONTENT_CHECK_FOR:
#         if c not in content:
#             READMELOOKSGOOD = False
#             pass
#     assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"
#
# def test_readme_file_for_formatting():
#     f = open("README.md", "r",encoding="utf-8")
#     content = f.read()
#     f.close()
#     assert content.count("#") >= 10
#
# def test_indentations():
#     ''' Returns pass if used four spaces for each level of syntactically \
#     significant indenting.'''
#     lines = inspect.getsource(session4)
#     spaces = re.findall('\n +.', lines)
#     for space in spaces:
#         assert len(space) % 4 == 2, "Your script contains misplaced indentations"
#         assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"
#
# def test_function_name_had_cap_letter():
#     functions = inspect.getmembers(session4, inspect.isfunction)
#     for function in functions:
#         assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"
#
#
# def test_decimal_used_or_not():
#     code_lines = inspect.getsource(session3)
#     assert 'decimal' in code_lines, 'Decimal not used! You must use fractions'
#     assert 'import' in code_lines, 'You have not imported decimal!'
#
# def test_fourspace_equal():
#     assert fourspace(session4) == False, 'Not all spaces before lines are a multiple of 4!'
#
# def test_function_names():
#     assert function_name_had_cap_letter(session4) == False, "One of your function has a capitalized alphabet!"
#
# def test_and():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1.and(r2), "error in and operation"
#
# def test_or():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     print(r1.or(r2))
#     assert r1.or(r2), "error in or operation"
#
# def test_q_times():
#     r1 = session4.Qualean(x)
#     a = r1.value
#     sum, num = 0, 10000
#     for _ in range(num):
#         sum = sum + a
#     print(sum)
#     assert r1.__mul__(num) == sum, "error in multiply 100 times"


