def move_zeroes(nums):
    non_zero_count = 0

    for num in nums:
        if num != 0:
            nums[non_zero_count] = num
            non_zero_count += 1

    while non_zero_count < len(nums):
        nums[non_zero_count] = 0
        non_zero_count += 1

    return nums

input_array = input("Enter the numbers separated by commas: ").strip().split(',')
input_array = [int(num) for num in input_array]

output_array = move_zeroes(input_array)
print("Array after moving zeroes to the end:", output_array)
