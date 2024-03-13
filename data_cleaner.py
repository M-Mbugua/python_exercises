# Question: Please download the attached countries-raw.txt file.
# The file contains the list of country names, but it also contains
# some unnecessary text among the countries.
# Please clean the list with Python by generating a new text file
# that contains a flawless list of country names without any other
# text or brake lines in it. The new file content should look like
# in the expected output.

with open('countries_raw.txt', 'r') as f:
    countries_raw = list(f.readlines())

countries = [c.strip('\n') for c in countries_raw if '\n' in c]
countries = [c for c in countries if c != ""]
countries = [c for c in countries if len(c) > 1]
countries = [c for c in countries if c != 'Top of Page']

print(countries)


with open('countries_cleaned.txt', 'w') as file:
    for c in countries:
        file.write(c + '\n')




