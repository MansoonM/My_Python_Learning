words=["moon","sun","planets","mercury","earth","galaxy","meteroids","blackholes"]

numbers=[23, 43, 32, 9, 0, 15, 27, 41]


# method 1 easy
x = words + numbers
print(x)

# method 2 moderate
words.extend(numbers)
print(words)

# method 3 hard
for x in words:
    numbers.append(x)
print(numbers)