def kthLargestNumber(nums, k):
    def compare(a, b):
        if len(a) != len(b):
            return len(a) - len(b)
        return (a > b) - (a < b)

    def select(nums, k):
        if len(nums) <= 5:
            nums.sort(key=lambda x: (len(x), x))
            return nums[-k]

        medians = []
        for i in range(0, len(nums), 5):
            group = nums[i:i+5]
            group.sort(key=lambda x: (len(x), x))
            medians.append(group[len(group)//2])

        pivot = select(medians, (len(medians)+1)//2)

        lows = [el for el in nums if compare(el, pivot) < 0]
        highs = [el for el in nums if compare(el, pivot) > 0]
        pivots = [el for el in nums if compare(el, pivot) == 0]

        if k <= len(highs):
            return select(highs, k)
        elif k <= len(highs) + len(pivots):
            return pivot
        else:
            return select(lows, k - len(highs) - len(pivots))

    return select(nums, k)
