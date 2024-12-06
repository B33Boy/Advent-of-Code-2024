
# Day 1

proceeds = {}  # vals come after key
preceeds = {}  # vals come before key

valid_rows = []
invalid_rows = []

with open('inp.txt', 'r') as f:
    first_half = True
    for line in f:
        if line == '\n':
            first_half = False
            continue

        if first_half:
            first, second = map(int, line.strip().split('|'))

            # Proceeding values
            if first not in proceeds:
                proceeds[first] = []
            proceeds[first].append(second)

            if second not in preceeds:
                preceeds[second] = []
            preceeds[second].append(first)

        else:
            update = list(map(int, line.rstrip().split(',')))
            is_valid = True
            for i, val in enumerate(update):

                if i == 0:
                    subarr = update[1:]
                    if not all([val not in proceeds.get(el, []) for el in subarr]):
                        is_valid = False
                        break

                elif i == len(update)-1:
                    subarr = update[:-1]
                    if not all([val not in preceeds.get(el, []) for el in subarr]):
                        is_valid = False
                        break

                else:
                    left_subarr = update[:i]
                    right_subarr = update[i+1:]

                    if not all([val not in proceeds.get(el, []) for el in right_subarr]) and not all([val not in preceeds.get(el, []) for el in left_subarr]):
                        is_valid = False
                        break

            if is_valid:
                valid_rows.append(update)
            else:
                invalid_rows.append(update)

total = 0
for row in valid_rows:
    total += row[len(row)//2]
print(total)

# Part 2
# [print(row) for row in invalid_rows]
new_valid = []

for row in invalid_rows:

    index_length = len(row)-1
    new_arr = [0]*(index_length+1)

    for i, val in enumerate(row):
        if i == 0:
            subarr = row[1:]
            count = sum(1 for key in subarr if val in proceeds.get(key, []))
            new_arr[count] = val

        elif i == index_length:
            subarr = row[:-1]
            count = sum(1 for key in subarr if val in proceeds.get(key, []))
            new_arr[count] = val
        else:
            left_subarr = row[:i]
            right_subarr = row[i+1:]

            count = sum(1 for key in left_subarr if val in proceeds.get(key, [])) + \
                sum(1 for key in right_subarr if val in proceeds.get(key, []))
            new_arr[count] = val

    new_valid.append(new_arr)

total = 0
for row in new_valid:
    total += row[len(row)//2]
print(total)
