from functions import *

import pytest

# ~~~~~ openFile ~~~~~
def test_openFile(capsys):

    # Call openFile function
    openFile("testing.txt")
  
    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "File opened."

def test_openFile_fail(capsys):

    # Call openFile function
    openFile("ENOENT.txt")
  
    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "File not found."
# ~~~~~


# ~~~~~ numbers ~~~~~
def test_numbers():

    # Test functin call
    assert numbers(64, 2) == 32
# ~~~~~


# ~~~~~ dist ~~~~~
def test_dist():

    # Test functin call
    assert dist(-4, -3, 4, 3) == 10
# ~~~~~


# ~~~~~ isPalindrome ~~~~~
def test_isPalindrome():

    # Palindrome as an array
    palArr = [9, 1, 0, 1, 9]

    # Test functin call
    assert isPalindrome(palArr) == True
# ~~~~~


# ~~~~~ divide ~~~~~
# Set input numbers
def divideInputs():
    numInputs = ["30", "5"]

    for num in numInputs:
        yield num

# Save input numbers into divIn
divIn = divideInputs()

def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(divIn))
    
    # Call divide function
    divide()

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Your numbers divided is: 6.0"
# ~~~~~


# ~~~~~ sq ~~~~~
def test_sq():

    # Test functin call
    assert sq(4) == 2
# ~~~~~


# ~~~~~ greetUser ~~~~~
def test_greetUser(capsys):

    # Call greetUser function
    greetUser('Linus', 'Benedict', 'Torvalds')

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Linus Benedict Torvalds\nGlad to have you!"


# ~~~~~


# ~~~~~ displayItem ~~~~~
def test_displayItem(capsys):

    # Create a test array of "animal names"
    animals = ["Danger Noodle", "Disco Turkey", "Land Clouds", "Ocean Piglet", "Level 32: Raccoon", \
        "Bumpy Desert Llama", "Panda Whale", "Danger Floof", "Trash Panda", "Danger Water Cow"]

    # Call displayItem function
    displayItem(animals, 8)

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Your item at 8 index is Trash Panda"
# ~~~~~
