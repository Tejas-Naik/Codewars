def two_sum(nums, target):
    prev_map = {}
    for index, number in enumerate(nums):
        diff = target - number
        if diff in prev_map:
            return [prev_map[diff], index]
        prev_map[number] = index
    return


print(two_sum([2, 7, 3, 4, 9], 9))
