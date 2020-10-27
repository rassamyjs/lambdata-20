""" This after_PEP8.py file follows PEP8 and should be used as a reference. """


### We should not have multiple package imports on one line
import math
import sys
# In other languages a semicolon indicates a line but in python line ends are communicated through
# indentation rules and white spaces.


# Make sure we have two blank lines between imports and the meat of our code.
# We seperate sections of code using two lines and stuff like functions with one.
def example_1():
  # Block comments should start with a single hash and be indented by a single space.
  # Each line has to below 80 characters.

  # We want white space around equal signs that are used for assignment and we dont want white space after.
  # White spaces should also be present only after our commas in list and tuples.
  some_tuple = ( 1, 2, 3, 'a')
  # white space in dictionaries should be key, colon, space, value ('key': value).
  # Indentation in dictionaries should have the keys on the same scope (number of indentations).
  some_variable = {
      "long": "LONG CODE LINES should be wrapped within 79 character",
      "other": [math.pi, 100, 200, 300, 9999292929292, 
                "This IS a long string that looks gross"],
      "more": {
          "inner": "THIS whole logical line should be wrapped", 
          "data": [444, 5555, 222, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5]}
  return (some_tuple, some_variable)

# We need to blank lines above and below this function.
def example_2(): 
  return {"has_key() is deprecated": True}

# Each class name needs to be upper camel case
class Example3(object):
  # Comments should always have a space after their hash
  def __init__   (self, bar):

    if bar: 
      bar += 1
      bar = bar*bar
      return bar

    else:
      some_string = """ 
        INDENTATION IN MULTIPLE STRINGS SHOULD NOT BE TOUCHED only actual code should be reindented,
        THIS IS MORE CODE
      """
      return some_string