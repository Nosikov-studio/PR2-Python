"""
Two Sum
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Дан массив целых чисел nums и целое число target, нужно вернуть индексы двух чисел из массива, 
которые в сумме образуют target.

Каждый массив точно будет иметь ровно одно решение и нельзя использовать один и тот же элемент дважды.

Вы можете вернуть ответ в любом порядке.
"""
nums = [22, 89, 2, 15, 7]
target = 9
s = 0
for i in nums:

    for j in range(nums.index(i)+1, len(nums)):
        if (i+nums[j]) == target:
            ans = (nums.index(i), j)
            print(ans)
            break
