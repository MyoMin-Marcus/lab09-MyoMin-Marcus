# Problem-solving practice (LeetCode / ICPC style).
#
# For EACH problem, work out your problem-solving OUTLINE first - restate the problem,
# try a small example by hand, and sketch your approach - BEFORE you write or generate
# any code. You may use an AI assistant to help implement your plan (see the README),
# but do the thinking first.
#
# Do not rename the functions - the tests use these names.


def two_sum(nums, target):
    # Outline (write your plan here first): check to see if the first two indices of the list add up to the target, 
    # if not check the next two indices and so on until you find a pair that adds up to the target.
    #   ...
    # TODO: return the indices [i, j] (i < j) of the two numbers in `nums` that add up
    #   to `target`. Assume there is exactly one answer.
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    pass


def max_profit(prices):
    # Outline: Keep track of the minimum price seen so far and the maximum profit that can be obtained by selling at the current price.
    #   ...
    # TODO: `prices[i]` is a stock price on day i. Return the most profit obtainable by
    #   buying on one day and selling on a LATER day. If no profit is possible, return 0.
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit


def max_subarray(nums):
    # Outline: check all possible subarrays and keep track of the maximum sum found. 
    #   ...
    # TODO: return the largest sum of any contiguous (in-a-row) block of numbers in
    #   `nums`. The list has at least one number.
    max_sum = nums[0]
    current_sum = nums[0]

    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)

    return max_sum


def is_balanced(s):   # Part 4 - stretch (optional)
    # Outline: Use a stack to keep track of the opening brackets and check if they match the closing brackets in the correct order.
    #   ...
    # TODO: return True if every bracket in `s` is closed correctly and in the right
    #   order. The brackets are ( ) [ ] { }. (Hint: a list used as a stack works well.)
    stack = []
    for char in s:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            if not stack:
                return False
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
    return not stack


def main():
    # Optional scratch space - try your functions here, then run: python lab09.py
    # print(two_sum([2, 7, 11, 15], 9))   # [0, 1]
    pass


if __name__ == "__main__":
    main()
    print(is_balanced("()[]{}"))   # returns True
    print(is_balanced("{[]}"))     # returns True
    print(is_balanced("([)]"))     # returns False   (closed in the wrong order)
    print(is_balanced(""))         # returns True
    print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # returns 6   (4 + -1 + 2 + 1)
    print(max_subarray([5, 4, -1, 7, 8]))                  # returns 23  (the whole list)
    print(max_profit([7, 1, 5, 3, 6, 4]))   # returns 5   (buy at 1, sell at 6)
    print(max_profit([7, 6, 4, 3, 1]))      # returns 0   (prices only fall)
    print(two_sum([2, 7, 11, 15], 9))   # returns [0, 1]   (2 + 7)
    print(two_sum([3, 2, 4], 6))        # returns [1, 2]   (2 + 4)