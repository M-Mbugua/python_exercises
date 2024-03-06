# Question: Create an English to Portuguese translation program.
# The program takes a word from the user as input and translates
# it using the following dictionary as a vocabulary source.
# Expected output:
#    Enter word: earth
#    terra

d = dict(weather = "clima", earth = "terra", rain = "chuva")

def translator(word):
    return d[word]

word = input('Please enter a word that you want translated: ')
print(translator(word))






