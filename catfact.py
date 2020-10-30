#!/bin/python
import requests
import json
import os
import sys


def getCatFact():
    url = 'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=2'
    page = requests.get(url)
    if page.status_code != 200:
        return ""
    catfacts = json.loads(page.text)
    catfact = catfacts[0]
    return catfact["text"]


def getCommandLine():
    args = sys.argv
    del args[0]
    return ' '.join([v for v in args])


fact = getCatFact()
if fact == "":
    print("Could not find a cat fact. Cat fact site is probably taking a cat nap")
else:
    print("First a cat fact: " + fact)
print("")
print("-------")
print("")
os.system('cat ' + getCommandLine())
