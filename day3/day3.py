# Part 1
import re

total = 0
pattern = r"mul\(([0-9]{1,3}),([0-9]{1,3})\)"

with open('inp.txt', 'r') as f:
    for line in f:
        for match in re.finditer(pattern, line):
            total += int(match.group(1)) * int(match.group(2))

print(total)

# Part 2
total = 0
pattern2 = r"(?<=do\(\))(.*?)(?=don\'t\(\))"
inp = "do()"

with open('inp.txt', 'r') as f:
    for line in f:
        inp += line.strip()

inp += "don't()"

for valid_text in re.finditer(pattern2, inp):
    valid_text = valid_text.group()
    for match in re.finditer(pattern, valid_text):
        total += int(match.group(1)) * int(match.group(2))

print(total)
