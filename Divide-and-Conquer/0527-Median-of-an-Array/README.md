# Median of an Array

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Light Mode
99+

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

Median of an Array
Solved

Difficulty: BasicAccuracy: 44.57%Submissions: 169K+Points: 1

Given an array arr[] of integers, calculate the median.

Examples:

Input: arr[] = [90, 100, 78, 89, 67]
Output: 89
Explanation: After sorting the array middle element is the median

Input: arr[] = [56, 67, 30, 79]
Output: 61.5
Explanation: In case of even number of elements, average of two middle elements is the median.

Input: arr[] = [1, 2]
Output: 1.5
Explanation: The average of both elements will result in 1.5.

Constraints:
1 <= arr.size() <= 105
1 <= arr[i] <= 105

Expected Complexities

Time Complexity: O(n log n)
Auxiliary Space: O(1)

Company Tags

AccoliteAmazonSamsungFactSet

Topic Tags

MathematicalDivide and ConquerAlgorithms

Related Articles

Median Of An Unsorted Array In Liner Time On

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total2 / 4Accuracy : 50%

Time Taken0.27

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Python3
C++ (17)
Java (21)
Python3
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

class Solution:
def findMedian(self, arr):
arr.sort()
n= len(arr)
for i in range(n):
if n%2!=0:
return arr[n//2]
else:
return (arr[n//2-1]+arr[n//2])/2
#code here.

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total2 / 4Accuracy : 50%

Time Taken0.27

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Median of an Array](https://www.geeksforgeeks.org/problems/find-the-median0527/1)
