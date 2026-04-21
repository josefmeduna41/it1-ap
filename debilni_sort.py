#!/usr/bin/env python3

from random import randint

# Returns: the index and the amount of tries it took
def rand_index(arr: list[int], tries=1) -> tuple[int, int]:
    idx = randint(0, len(arr)-1)
    if arr[idx] == None:
        return rand_index(arr, tries+1)
    return idx, tries

# Returns: shuffled array and amount of tries it took
def debilni_shuffle(arr: list[int]) -> tuple[list[int], int]:
    tries = 0
    new = []
    while len(new) < len(arr):
        idx, idx_tries = rand_index(arr)

        elem = arr[idx]
        arr[idx] = None

        new.append(elem)
        tries += idx_tries

    return new, tries

# Returns: shuffled array and amount of tries it took
def debilni_shuffle_v2(original_arr: list[int]) -> tuple[list[int], int]:
    # Make a copy to prevent mutating the old list
    arr = original_arr.copy()

    new = []
    while len(new) < len(original_arr):
        idx = randint(0, len(arr)-1)

        elem = arr.pop(idx)
        new.append(elem)
    
    return new

# arr = range(1, 33)
# shuffled, tries = debilni_shuffle(list(arr))

# print('array:', '; '.join(map(str, arr)))
# print('shuffled:', '; '.join(map(str, shuffled)))
# print(f'took {tries} tries')

arr = range(1, 33)
shuffled = debilni_shuffle_v2(list(arr))
print(f'array ({len(arr)}):', '; '.join(map(str, arr)))
print(f'shuffled ({len(shuffled)}):', '; '.join(map(str, shuffled)))