import pytest
import random
import string
import session4
import os
import inspect
import re
import math

x = 1
num = 100
README_CONTENT_CHECK_FOR = ['__and__', '__or__', '__repr__', '__str__', '__add__',
'__eq__', '__float__', '__ge__', '__gt__', '__invertsign__', '__le__', '__lt__',
 '__mul__', '__sqrt__', '__bool__']

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme_words=[word for line in open('README.md', 'r') for word in line.split()]
    assert len(readme_words) >= 100, "Make your README.md file interesting! Add atleast 100 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", 'r')
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r",encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_decimal_used_or_not():
    code_lines = inspect.getsource(session4)
    assert 'decimal' in code_lines, 'Decimal not used! You must use fractions'
    assert 'import' in code_lines, 'You have not imported decimal!'

# def test_and():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1.__and__(r2), "error in And operation"
#
# def test_or():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(-1)
#     print(r1.__or__(r2))
#     assert r1.__or__(r2), "error in Or operation"
#
# def test_q_times():
#     r1 = float(session4.Qualean(x))
#     a = round(float(r1),10)
#     sum, num = 0, 10000
#     for _ in range(num):
#         sum = float(a) + sum
#         sum = round(float(sum),10)
#     print(float(sum))
#     z = round(float(r1.__mul__(num)),10)
#     assert z == round(float(sum,10)), "error in multiply 100 times"

def test_bool():
    r1 = session4.Qualean(x)
    print(r1.__bool__())
    assert r1.__bool__(), "error in multiply operation"

def test_add():
    r1 = session4.Qualean(x)
    r2 = session4.Qualean(x)
    assert r1.__add__(r2), "error in And operation"

def test_or_q1_q2():
    q1 = session4.Qualean(x)
    q2 = session4.Qualean(0)
    print(q1.__or__(q2))
    assert q1.__or__(q2)==False, "error in Or q1 q2 operation"

def test_and_q1_q2():
    q1 = session4.Qualean(x)
    q2 = session4.Qualean(1)
    assert q1.__and__(q2)==True, "error in And q1 q2 operation"

def test_float():
    r1 = session4.Qualean(x)
    assert r1.__float__() == float(r1), "error in float operation"

def test_invertsign():
    r1 = session4.Qualean(1)
    assert float(r1.__invertsign__()) == -float(r1), "error in invertsign operation"

# def test_lessthan():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1 < r2 == r1.__lt__(r2), "must be less than!"

# def test_leesthanequal():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1 <= r2, "must be less than or equal!"

# def test_greaterthan():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1 > r2, "must be greater than!"

# def test_greaterThanEqual():
#     r1 = session4.Qualean(x)
#     r2 = session4.Qualean(x)
#     assert r1 >= r2, "must be greater than or equal!"



