from functions import *

import pytest

# ~~~~~ openFile Tests ~~~~~
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



# ~~~~~ numbers Tests ~~~~~
def test_numbers():

    # Test functin call
    assert numbers(64, 2) == 32
# ~~~~~



# ~~~~~ dist Tests ~~~~~
def test_dist():

    # Test functin call
    assert dist(-4, -3, 4, 3) == 10
# ~~~~~



# ~~~~~ isPalindrome Tests ~~~~~
def test_isPalindrome():

    # Palindrome as an array
    palArr = [9, 1, 0, 1, 9]

    # Test functin call
    assert isPalindrome(palArr) == True
# ~~~~~



# ~~~~~ divide Tests ~~~~~

# ~~~ divide Test (1) Start
# Set input numbers
def divideInputs1():
    numInputs1 = ["30", "5"]

    for num in numInputs1:
        yield num

# Save input numbers into divIn1
divIn1 = divideInputs1()

# ~~ Test (1) function call
def test_divide(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(divIn1))
    
    # Call divide function
    divide()

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Your numbers divided is: 6.0"
# ~~~ divide Test (1) End

# ~~~ divide Test (2) Start
# Set input numbers
def divideInputs2():
    numInputs2 = ["30", "0"]

    for num in numInputs2:
        yield num

# Save input numbers into divIn2
divIn2 = divideInputs2()

# ~~ Test (2) function call
def test_divide2(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(divIn2))
    
    # Call divide function
    divide()

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "ZeroDivisionError: division by zero"
# ~~~ divide Test (2) End


# ~~~ divide Test (3) Start
# Set input numbers
def divideInputs3():
    numInputs3 = ["A", "5"]

    for num in numInputs3:
        yield num

# Save input numbers into divIn3
divIn3 = divideInputs3()

# ~~ Test (3) function call
def test_divide3(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(divIn3))
    
    # Call divide function
    divide()

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "ValueError: invalid literal for int() with base 10"
# ~~~ divide Test (3) End


# ~~~ divide Test (4) Start
# Set input numbers
def divideInputs4():
    numInputs4 = ["-30", "5"]

    for num in numInputs4:
        yield num

# Save input numbers into divIn4
divIn4 = divideInputs4()

# ~~ Test (3) function call
def test_divide4(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: next(divIn4))
    
    # Call divide function
    divide()

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Your numbers divided is: -6.0"
# ~~~ divide Test (4) End
# ~~~~~



# ~~~~~ sq Tests ~~~~~
def test_sq():

    # Test functin call
    assert sq(4) == 2
# ~~~~~



# ~~~~~ greetUser Tests ~~~~~
def test_greetUser(capsys):

    # Call greetUser function
    greetUser('Linus', 'Benedict', 'Torvalds')

    # Capture output
    captured_stdout, captured_stderr = capsys.readouterr()
    
    # Test functin call
    assert captured_stdout.strip() == "Hello!\nWelcome to the program Linus Benedict Torvalds\nGlad to have you!"
# ~~~~~



# ~~~~~ displayItem Tests ~~~~~
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
