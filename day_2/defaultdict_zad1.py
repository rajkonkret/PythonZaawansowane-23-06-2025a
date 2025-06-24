from collections import defaultdict

word_count = defaultdict(int)

tekst = "python jest super, python jest doskonały, python jest lider"

for word in tekst.split():
    # word_count[word.lower()] += 1
    word_count[word.casefold()] += 1

for word, count in word_count.items():
    print(f"{word}: {count}")
# python: 3
# jest: 3
# super,: 1
# doskonały,: 1
# lider: 1

name1 = "GROSS"
name2 = "groẞ"

print(name1.lower() == name2.lower())  # False
print(name1.casefold() == name2.casefold())  # True
# """ Return a version of the string suitable for caseless comparisons. """
