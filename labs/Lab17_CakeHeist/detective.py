"""
detective.py  -  catch the cake thief

STEP 4  sets                        senders_between(), who_mentioned(), find_culprit()
STEP 5  arguments + scope           search(), count_words(), add_drama()
"""


# -------------------------------------------------------------------
# STEP 4: sets
# -------------------------------------------------------------------
def senders_between(messages, start, end):
    """Return a SET of critters who sent a message between start and end (both included).

    start and end are (hour, minute) tuples, e.g. (15, 0) and (15, 30).
    """
    return {sender for time, sender, _ in messages if start <= time <= end}


def who_mentioned(messages, phrase):
    """Return a SET of critters whose message contains phrase (ignore upper/lower case)."""
    target = phrase.lower()
    return {sender for _, sender, text in messages if target in text.lower()}


def find_culprit(online, knew_secret, alibis):
    """Return the set of critters who were online AND knew the secret, minus anyone with an alibi."""
    return (online & knew_secret) - alibis


# -------------------------------------------------------------------
# STEP 5: arguments
# -------------------------------------------------------------------
def search(messages, word, sender=None, ignore_case=True):
    """Return a list of message tuples whose text contains word.

    sender       (default None)  -> if given, only that critter's messages
    ignore_case  (default True)  -> if True, "CAKE" also matches "cake"
    """
    results = []
    needle = word.lower() if ignore_case else word
    for message in messages:
        _, who, text = message
        if sender is not None and who != sender:
            continue
        haystack = text.lower() if ignore_case else text
        if needle in haystack:
            results.append(message)
    return results


def count_words(messages, *words):
    """Return a dictionary: for each word, how many messages contain it (ignore case).

    count_words(messages, "cake", "nap")  ->  {"cake": 6, "nap": 2}
    """
    return {word: len(search(messages, word)) for word in words}


# -------------------------------------------------------------------
# STEP 5: scope
# -------------------------------------------------------------------
total_drama = 0          # a GLOBAL variable: it lives outside every function


def add_drama(text):
    """Add drama points for one message to the global total_drama. Return the points."""
    global total_drama
    points = text.count("!")
    if text.isupper():
        points += 5
    total_drama = total_drama + points
    return points