"""
Leetcode- https://leetcode.com/problems/combination-sum/ (submitted)

TC- O(2^(Target/ min(N))), The time complexity in a binary decision tree is 2^h, where h is height of the tree.
Here, our height of the tree would be, until we reach a base condition, i.e., keep choosing the smallest number in the
numbers such that index < 0, or in other words, Target / min(N), and, since we make 2 decisions (choose and not choose),
 our total branches would be (no. of decisions ^ height of tree), ie. 2 ^ (Target/min(N)).
SC- O(1) auxiliary. We can argue to not consider TC for copying path while saving the result is a limited
event.

Challenges-Writing code for 'for loop recursion'. Thinking where no choose will happen in for loop. *refer ideation*
Lecture-https://youtu.be/ZcwpurxyIaQ
FAQ-
Will there be any duplicates in your recursion? No since we will have only unique path in our recursion tree because
it will never happen that we go to the next element and come back to previous again to add to path. So, we always move
forward. (refer lecture -  https://youtu.be/ZcwpurxyIaQ?t=810)


Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of
candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the
frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the
given input.


Example 1:
Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.

Example 2:
Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]

Example 3:
Input: candidates = [2], target = 1
Output: []


Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    """
    (Preferred solution)
    Ideation - for loop Recursion with backtracking O(2^(Target/ min(N))) TC, O(1) SC auxiliary

    At each point you have an option to choose or not choose a particular element. If you choose, that element is
    added to your path, if you don't it's not.

    In for loop recursion, our not choose is when we increment our index, which means if we don't want to choose an
    element we increment our for loop index by 1. If you want to consider it, call a recursion with, target - element's
    value. Also consider backtracking.

    We can further optimize this recursion by sorting the input and breaking recursion when one pivot element makes
    target negative, since all bigger elements to it's right will only make it more negative.
    """

    def combinationSum(self, candidates, target):
        self.result = []
        self.helper(candidates, target, 0, [])
        return self.result

    def helper(self, candidates, target, index, path):
        # base case - Our pair sum is bigger than target.
        # We don't need to check length of index because for loop can take care of it.
        if target < 0:
            return
        # we found our pair.
        if target == 0:
            self.result.append(path[:])
            return
        # logic
        for i in range(index, len(candidates)):
            # not choose happens with for loop interation
            # action
            path.append(candidates[i])
            self.helper(candidates, target - candidates[i], i, path)
            # backtrack
            del path[len(path) - 1]

    """
    (Preferred solution)
    Ideation - 01 Recursion with backtracking O(2^(Target/ min(N))) TC, O(1) SC auxiliary
    Variation 1: not choose first

    At each point you have an option to choose or not choose a particular element, if you don't choose, you can go to
    the next element and if you choose, you don't change choose index since the same element can be repeated.

    Your recursion will terminate when the current target becomes negative or if your choose index gets out of bound.

    Here we are picking not choose first and only change path when we choose that element.
    """

    def combinationSum1(self, candidates, target):
        self.result = []
        self.helper1(candidates, target, 0, [])
        return self.result

    def helper1(self, candidates, target, index, path):
        # base - if index == length or target is less than zero
        if index == len(candidates) or target < 0:
            return
        if target == 0:
            # deep copy path in result since it would change
            self.result.append(path[:])
            return
        # logic
        # No choose step
        self.helper1(candidates, target, index + 1, path)
        # choose step
        # action
        path.append(candidates[index])
        self.helper1(candidates, target - candidates[index], index, path)
        # backtrack - undo the action of adding path
        del path[len(path) - 1]


    """
    Ideation - 01 Recursion with no backtracking O(2^(Target/ min(N)) * N) TC (time N because we create fresh instance 
    of path), O(1) SC auxiliary
    
    The logic will be same as previous variation of 01 recursion.

    But here, since we are picking choose first, when we change the path by adding the current choice, we will be 
    sending the reference of same path in not choose scenario and our result will be wrong.
    We can fix it by copying the elements and sending a complete new list to choose recursion step and send original 
    path to no choose step.
    """


def combinationSum2(self, candidates, target):
    self.result = []
    self.helper2(candidates, target, 0, [])
    return self.result


def helper2(self, candidates, target, index, path):
    # base - if index == length or target is less than zero
    if index == len(candidates) or target < 0:
        return
    if target == 0:
        # deep copy path in result since it would change
        self.result.append(path[:])
        return
    # logic
    # choose
    # action
    tempPath = path[:]
    tempPath.append(candidates[index])
    self.helper2(candidates, target - candidates[index], index, tempPath)
    # no backtracking required for choose path since we are sending a new reference of path list
    # No choose
    self.helper2(candidates, target, index + 1, path)

    """
    Ideation - 01 Recursion with no backtracking O(2^(Target/ min(N)) * N) TC (time N because we create fresh instance of 
    path), O(1) SC auxiliary
    
    The logic will be same as previous variation of 01 recursion.
    
    But here, since we are not doing backtracking if we send same reference of path to our recursion calls, the changes
    in all the instances of recursion will effect all and we will get wrong answer - [[], []].
    We can fix this by sending new references of path each time recursion is called.
    """

    def combinationSum3(self, candidates, target):
        self.result = []
        self.helper3(candidates, target, 0, [])
        return self.result

    def helper3(self, candidates, target, index, path):
        # base - if index == length or target is less than zero
        if index == len(candidates) or target < 0:
            return
        if target == 0:
            # no deep copy required since each recursion call has a fresh reference to path.
            self.result.append(path)
            return
        # logic
        # No choose step
        self.helper3(candidates, target, index + 1, path[:])
        # choose step
        # action
        path.append(candidates[index])
        self.helper3(candidates, target - candidates[index], index, path[:])
