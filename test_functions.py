from functions import openFile, numbers, dist, \
    isPalindrome, divide, sq, greetUser, displayItem

import pytest

# ~~~~~ openFile ~~~~~
def test_openFile():

    assert openFile("testing.txt") == None
# ~~~~~


# ~~~~~ numbers ~~~~~
def test_numbers():

    assert numbers(64, 2) == 32
# ~~~~~


# ~~~~~ dist ~~~~~
def test_dist():

    assert dist(-4, -3, 4, 3) == 10
# ~~~~~


# ~~~~~ isPalindrome ~~~~~
def test_isPalindrome():
    input = [9, 1, 0, 1, 9]
    assert isPalindrome(input) == True
# ~~~~~


# ~~~~~ divide ~~~~~
def test_divide():

    assert divide(128, 32) == 4
# ~~~~~


# ~~~~~ sq ~~~~~
def test_sq():

    assert sq(4) == 2
# ~~~~~


# ~~~~~ greetUser ~~~~~
def test_greetUser():

    assert greetUser('Linus', 'Benedict', 'Torvalds') == None
# ~~~~~


# ~~~~~ displayItem ~~~~~
def test_displayItem():
    animals = ["Danger Noodle", "Disco Turkey", "Land Clouds", "Ocean Piglet", "Level 32: Raccoon", \
        "Bumpy Desert Llama", "Panda Whale", "Danger Floof", "Trash Panda", "Danger Water Cow"]
    assert displayItem(animals, 8) == None
# ~~~~~
