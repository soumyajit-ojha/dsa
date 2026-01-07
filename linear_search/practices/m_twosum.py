def twoSum(numbers: list[int], target: int) -> list[int]:
    # taking index number as pointer
    left, right = 0, len(numbers) - 1
    print("Pointer values")
    print("left",left, "right", right)

    while left < right:
        current_sum = numbers[left] + numbers[right]
        print("left",left, "right", right)
        print("SUM", current_sum)
        if current_sum == target:
            return [left + 1, right + 1]
        elif current_sum < target:
        # shifting left pointer location towards right
            left += 1
        else:
        # shifting right pointer location towards left
            right -= 1
    print("Pointer values after iteration")
    print("left",left, "right", right)

numbers = [2,7,11,15]
target = 9
res = twoSum(numbers=numbers, target=target)
print(res)
