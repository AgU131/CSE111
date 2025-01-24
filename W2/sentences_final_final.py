"""
CSE111
W02 Project: Sentences
Agustin Heredia
"""

import random

def main():
    # Generate six sentences with different characteristics
    print(make_sentence(1, "past"))
    print(make_sentence(1, "present"))
    print(make_sentence(1, "future"))
    print(make_sentence(2, "past"))
    print(make_sentence(2, "present"))
    print(make_sentence(2, "future"))

def make_sentence(quantity, tense):
    """Generate and return a sentence."""
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    verb = get_verb(quantity, tense)
    prepositional_phrase = get_prepositional_phrase(quantity)
    sentence = f"{determiner.capitalize()} {noun} {verb} {prepositional_phrase}."
    return sentence

def get_determiner(quantity):
    """Return a determiner based on the quantity."""
    if quantity == 1:
        determiners = ["a", "one", "the"]
    else:
        determiners = ["some", "many", "the"]
    return random.choice(determiners)

def get_noun(quantity):
    """Return a noun based on the quantity."""
    if quantity == 1:
        nouns = ["bird", "child", "dog", "girl", "man", "rabbit"]
    else:
        nouns = ["birds", "children", "dogs", "girls", "men", "rabbits"]
    return random.choice(nouns)

def get_verb(quantity, tense):
    """Return a verb based on the quantity and tense."""
    if tense == "past":
        verbs = ["drank", "ate", "ran", "slept", "talked", "walked"]
    elif tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "runs", "sleeps", "talks", "walks"]
        else:
            verbs = ["drink", "eat", "run", "sleep", "talk", "walk"]
    elif tense == "future":
        verbs = ["will drink", "will eat", "will run", "will sleep", "will talk", "will walk"]
    return random.choice(verbs)

def get_preposition():
    """Return a randomly chosen preposition."""
    prepositions = [
        "about", "above", "across", "after", "along", "around", "at", "before", 
        "behind", "below", "beyond", "by", "despite", "except", "for", "from", 
        "in", "into", "near", "of", "off", "on", "onto", "out", "over", "past", 
        "to", "under", "with", "without"
    ]
    return random.choice(prepositions)

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase."""
    preposition = get_preposition()
    determiner = get_determiner(quantity)
    noun = get_noun(quantity)
    return f"{preposition} {determiner} {noun}"

main()