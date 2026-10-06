# Second Largest

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Dark Mode
99+

Ask A DoubtMy Doubts

Doubt Assistance Not Available.

Back

all

articles

videos

problems

Next Track

Menu

problems (13)
Sort By
Accuracy Low to High
Accuracy High to Low
Submmision Low to High
Submmision High to Low
Difficulty Low to High
Difficulty High to Low

Second Largest

Easy
Accuracy: 26.72%

Move All Zeroes to End

Easy
Accuracy: 45.51%

Reverse Array

Easy
Accuracy: 55.32%

Rotate Array

Medium
Accuracy: 37.06%

Next Permutation

Medium
Accuracy: 40.66%

Majority Element - More Than n/3

Medium
Accuracy: 48.1%

Stock Buy and Sell – Multiple Transaction Allowed

Medium
Accuracy: 13.43%

Stock Buy and Sell – Max one Transaction Allowed

Easy
Accuracy: 49.33%

Minimize the Heights

Medium
Accuracy: 15.06%

Kadane's Algorithm

Medium
Accuracy: 36.28%

Maximum Product Subarray

Medium
Accuracy: 18.09%

Max Circular Subarray Sum

Hard
Accuracy: 29.37%

Smallest Positive Missing

Medium
Accuracy: 25.13%

Problems Solved
4 of 13 Complete. (31%)

Progress may take upto 2 hours to reflect.

ProblemEditorialSubmissions

Second Largest
Solved

Difficulty: EasyAccuracy: 26.72%Submissions: 1.6MPoints: 2Average Time: 15m

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.
Note: The second largest element should not be equal to the largest element.
Examples:
Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.
Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.
Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Company Tags

SAP LabsRockstand

Topic Tags

ArraysSearching

Related Articles

Find Second Largest Element Array

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom Input

Python3
C (gcc 5.4)
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

class Solution:
def getSecondLargest(self, arr):
# code here
l=arr[0]
sl=-1
for i in arr:
if i>l:
sl=l
l=i
elif i>sl and i!=l:
sl=i
return sl

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom Input

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Second Largest](https://www.geeksforgeeks.org/problems/second-largest3735/1)
