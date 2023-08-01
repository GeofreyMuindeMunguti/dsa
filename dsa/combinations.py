"""
https://leetcode.com/problems/combinations/description/

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.
Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


Constraints:

1 <= n <= 20
1 <= k <= n

"""
import itertools
from typing import List


def combination_solution(n: int, k: int) -> List[List[int]]:
    """
        The backtrack function is a recursive function used to generate all possible combinations of k
        numbers chosen from the range [1, n].

        The function starts with the base case: when the length of path becomes equal to k, it means a
        valid combination is formed. At this point, the current path list is appended to the result list.

        If the base case is not reached, the function enters the for loop. The loop iterates over the
        numbers from start to n + 1.

        For each number i in the loop, it does the following:

        Appends i to the path list using path.append(i). This means that we are including the current
         number i in the combination.

        Makes a recursive call to the backtrack function with the updated start value, i + 1, to ensure
        we do not reuse elements in the combination.

        After the recursive call returns, the next line of code is executed, which is path.pop().
        This operation removes the last element from the path list, effectively undoing the addition
        of the current number i. This step is essential for backtracking.

        By popping the last element from the path list, the function is backtracking to the previous
         state before the recursive call. It means that we have finished exploring the current branch
         of the combination, and we need to try other possibilities.

        The loop continues to explore other numbers, and the process repeats until all valid combinations are generated.
    """
    result = []

    def backtrack(start, combination):
        if len(combination) == k:
            result.append(combination[:])
            return

        for i in range(start, n+1):
            combination.append(i)
            backtrack(i + 1, combination)

            # This is called after the backtrack function returns, essentially after the combination
            # has been added to the list.
            # Notice trick in how the recursive functions are called and the flow of execution
            combination.pop()

    backtrack(1, [])
    return result


if __name__ == "__main__":
    n = 4
    k = 2

    expected_result = [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
    res = combination_solution(n, k)
    print(res)
    assert(res == expected_result)
