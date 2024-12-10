with open('inp.txt', 'r') as f:
    line = f.readline()


# Part 1

def generate_fragmented_data(line: str) -> list[int]:
    id_num: int = 0
    is_free: bool = True
    fragmented_data: list[int] = []
    free_blocks: int = 0

    for _, file_length in enumerate(line):

        is_free = not is_free

        if is_free:
            fragmented_data += [None] * int(file_length)
            free_blocks += int(file_length)

        else:
            fragmented_data += [id_num]*int(file_length)
            id_num += 1

    return fragmented_data, free_blocks


def defragmant(frag: list[int], free_blocks: int) -> list[int]:
    length = len(frag)
    l: int = 0
    r: int = length - 1

    while free_blocks > 0:

        while l < length and frag[l] is not None:
            l += 1

        while r >= 0 and frag[r] is None:
            r -= 1

        if l >= r:
            break

        frag[l], frag[r] = frag[r], frag[l]
        free_blocks -= 1

    return frag


def calculate_checksum(frag: list[int]) -> int:
    checksum = 0

    for i, elem in enumerate(frag):
        if elem is None:
            continue
        checksum += i * elem
    return checksum


# Generate fragmented data
fragmented_data: list[int] = []
free_blocks: int = 0

fragmented_data, free_blocks = generate_fragmented_data(line)

print("original", ' '.join(list(map(str, fragmented_data))))
print("free_spots: ", free_blocks)

defragmented_data: list[int] = defragmant(list(fragmented_data), free_blocks)
print(calculate_checksum(defragmented_data))
