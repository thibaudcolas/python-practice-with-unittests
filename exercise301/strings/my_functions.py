import re


def find_year(filename):
    with open(filename) as fn:
        years = re.findall(r"\d{4}", fn.read())
    return years


def find_email(filename):
    with open(filename) as fn:
        emails = re.findall(r"[a-zA-Z0-9-.]*@[a-zA-Z-.]*\.[a-zA-Z]+", fn.read())
    return emails


def find_initial_caps(filename):
    pass
