# int_research.py - Researching the int() function on strings.
# Predictions and Results:
# int(" 22 "): Works. Strips leading and trailing whitespace.
# int("+22"): Works. Accepts leading positive/negative signs.
# int("0022"): Works. Parses numbers with leading zeros as standard integers.
# int("2_2"): Works. Underscores are valid separators in numeric literals (Python 3.6+).
# Output testing:
print(int(" 22 "))
print(int("+22"))
print(int("0022"))
print(int("2_2"))
# Documentation URL used:
# https://docs.python.org/3/library/functions.html#int