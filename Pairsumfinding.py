def string_read(n, nums, target):
    left = 0
    right = n - 1
    nums.sort()
    pairs = []
    while left < right:
        summation = nums[left] + nums[right]
        if summation == target:
            pairs.append((nums[left], nums[right]))
            left += 1
            right -= 1
        elif summation < target:
            left += 1
        else:
            right -= 1
    if pairs:
        return pairs
    else:
        return "Pair not found."

# Example usage
nums1 = [8, 7, 2, 5, 3, 1]
target1 = 10
result1 = string_read(len(nums1), nums1, target1)
if result1 == "Pair not found.":
    print(result1)
else:
    for pair in result1:
        print(f"Pair found {pair}")

nums2 = [5, 2, 6, 8, 1, 9]
target2 = 12
result2 = string_read(len(nums2), nums2, target2)
if result2 == "Pair not found.":
    print(result2)
else:
    for pair in result2:
        print(f"Pair found {pair}")
