import re

email = 'jose@tecladocode.com'
expression = '[a-z\.]+'

matches = re.findall(expression, email)
print(matches)

name = matches[0]
domain = matches[1]

print(name)
print(domain)


# Another method
parts = email.split('@')

name = parts[0]
domain = parts[1]

print(name)
print(domain)


# Another example
price = 'Price: $18,649.50'
expression = 'Price: \$([0-9,]*\.[0-9]*)'

matches = re.search(expression, price)
print(matches.group(0))  # Entire match
print(matches.group(1))  # First thing in parenthesis

price_number = float(matches.group(1).replace(',', ''))  # Remove comma with replace
print(price_number)
