# Smallest Divisor

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Dark Mode
99+

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

Smallest Divisor
Solved

Difficulty: MediumAccuracy: 50.74%Submissions: 33K+Points: 4Average Time: 25m

Given an integer array arr[] and an integer k (where k ≥ arr.length), find the smallest positive integer divisor such that the sum of the ceiling values of each element in arr[] divided by this divisor is less than or equal to k.
Examples:
Input: arr[] = [1, 2, 5, 9], k = 6
Output: 5
Explanation: 5 is the smallest divisor having sum of quotients (1 + 1 + 1 + 2 = 5) less than or equal to 6.

Input: arr[] = [1, 1, 1, 1], k = 4
Output: 1
Explanation: 1 is the smallest divisor having sum of quotients (1 + 1 + 1 + 1 = 4) less than or equal to 4.

Constraints:
1 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 106
arr.size() ≤ k ≤ 106

Expected Complexities

Time Complexity: O(n * log(max(arr[i])))
Auxiliary Space: O(1)

Topic Tags

Binary SearchArrays

Related Articles

Smallest Divisor For Sum Constraint In Array Division

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total2 / 3Accuracy : 66%

Time Taken1.95

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Python3
C++ (17)
Java (21)
Python3
C#
Javascript (Node v22)

Editor Settings
Font Size
Theme

Choose Your Preferred font For The Code Editor
12px13px14px15px16px18px20px22px

1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22

import math
class Solution:
def div(self, arr, mid):
s=0
for i in arr:
s+=math.ceil(i/mid)
return s

def smallestDivisor(self, arr, k):
# Code here
l=1
h=max(arr)
while l<=h:
mid=(l+h)//2
sum=self.div(arr, mid)
if sum>k:
l=mid+1
else:
h=mid-1
return l

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total2 / 3Accuracy : 66%

Time Taken1.95

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Smallest Divisor](https://www.geeksforgeeks.org/problems/smallest-divisor/1)
