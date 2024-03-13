# Question: This list has three items which are missing from 'countries_missing.txt'.
# ["Portugal", "Germany", "Spain"]
# Create a new file containing all of these countries including Portugal, Germany,
# and Spain.

missing = ["Portugal", "Germany", "Spain"]

with open('countries_missing.txt', 'r') as f:
    countries = list(f.readlines())

missing = [c + '\n' for c in missing]

countries_added = sorted(countries + missing)

with open('countries.added.txt', 'w') as file:
    for c in countries_added:
        file.write(c)

