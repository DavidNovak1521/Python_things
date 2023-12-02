# Names Scores
# 871198282

file = open("names.txt")
names = sorted(file.read().strip('"').split('","'))
total = 0

def getAlphabeticalValue(name):
    return sum([ord(ch) - 64 for ch in name])

for index, name in enumerate(names):
    total += (index+1) * getAlphabeticalValue(name)

print(total)