#corpora project
#https://github.com/dariusk/corpora/tree/master/data
#use the modifiers

#tracery
import time
import sys
import tracery
from tracery.modifiers import base_english

rules = {
    'origin': '#hello.capitalize#, in, #location#!',
    'hello': ['hello', 'greetings', 'howdy', 'hey'],
    'location': ['world', 'solar system', 'galaxy', 'universe']
}

grammar = tracery.Grammar(rules)
grammar.add_modifiers(base_english)
#python -m tracery grammar.json

loop = 1

while loop == 1:
    flat = grammar.flatten("#origin#"), #prints, e.g., "Hello, world!"
    for l in flat:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.1)
    print " ",
