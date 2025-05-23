import re

# Name regex:
# Matches 1 to 3 capitalized names,
# each may include apostrophes or hyphens (like D'Angelo or Taylor-Joy)
name = r"^[A-Z](?:[a-z]+|['-][A-Z][a-z]+)*(?: [A-Z](?:[a-z]+|['-][A-Z][a-z]+)*){0,2}$"
name_regex = re.compile(name)

# Phone regex:
# Matches:
# - 10 digits: 5555555555
# - Dashes: 555-555-5555
# - Parentheses and space: (555) 555-5555
phone = r"^(\d{10}|\d{3}-\d{3}-\d{4}|\(\d{3}\) \d{3}-\d{4})$"
phone_regex = re.compile(phone)

# Email regex:
# Matches emails starting with a letter, may contain digits and dots (not consecutively),
# with a proper domain and TLD.
email = r"^[a-zA-Z][a-zA-Z0-9]*(\.[a-zA-Z0-9]+)*@[a-zA-Z]+\.[a-zA-Z]+$"
email_regex = re.compile(email)
