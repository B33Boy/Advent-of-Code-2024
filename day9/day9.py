with open('inp.txt', 'r') as f:
    line = f.readline()


# Part 1
is_free: bool = True
id_num: int = 0
free_blocks: int = 0
fragmented_data: list[int] = []

# Generate fragmented data
for _, file_length in enumerate(line):

    is_free = not is_free

    if is_free:
        free_space = int(file_length)
        fragmented_data += [None] * free_space  # -1 will be empty spaces
        free_blocks += free_space

    else:
        fragmented_data += [id_num]*int(file_length)
        id_num += 1

# print("original", ' '.join(list(map(str, fragmented_data))))
print("free_spots: ", free_blocks)


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
        # print(' '.join(list(map(str, frag))))

    return frag


def calculate_checksum(frag: list[int]) -> int:
    checksum = 0

    for i, elem in enumerate(frag):
        if elem is None:
            continue
        checksum += i * elem
    return checksum


defrag: list[int] = defragmant(list(fragmented_data), free_blocks)
print(calculate_checksum(defrag))
