with open('inp.txt', 'r') as f:
    line = f.readline()


# Part 1
is_free: bool = True
i: int = 0
free_blocks: int = 0
fragmented: str = ""

# Generate fragmented data
for idx, file in enumerate(line):
    is_free = not is_free
    if is_free:
        free_space = int(file)
        fragmented += "." * free_space
        free_blocks += free_space
    else:
        fragmented += str(i)*int(file)
        i += 1

print("original", fragmented)
print("free_spots: ", free_blocks)


def defragmant(frag: list[str], free_blocks: int) -> list[str]:
    length = len(frag)
    l: int = 0
    r: int = length - 1

    while free_blocks > 0:

        while l < length and frag[l] != '.':
            l += 1

        while r >= 0 and frag[r] == '.':
            r -= 1

        if l >= r:
            break

        frag[l], frag[r] = frag[r], frag[l]
        print(''.join(frag))
        free_blocks -= 1

    return frag


def calculate_checksum(frag: list[str]) -> int:
    checksum = 0

    for i, elem in enumerate(frag):
        if elem == '.':
            continue
        checksum += i * int(elem)
    return checksum


defrag: list[str] = defragmant(list(fragmented), free_blocks)
print(calculate_checksum(defrag))
