# Implementation of Priority Queue using Binary Heap

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

Implementation of Priority Queue using Binary Heap
Solved

Difficulty: EasyAccuracy: 67.41%Submissions: 17K+Points: 2Average Time: 30m

Given a binary heap implementation of Priority Queue. Extract the maximum element from the queue i.e. remove it from the Queue and return it's value.
Examples :
Input: 4 2 8 16 24 2 6 5
Output: 24
Priority Queue after extracting maximum: 16 8 6 5 2 2 4
Input: 64 12 8 48 5
Output: 64
Priority Queue after extracting maximum: 48 12 8 5

Expected Time Complexity: O(logn)
Expected Space Complexity: O(n)

Constraints:
1<=n<=500

Topic Tags

Heap

Related Articles

Priority Queue Using Binary Heap

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed120 / 120
Attempts : Correct / Total3 / 3Accuracy : 100%

Time Taken0.29

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Python3
C++ (17)
Java (21)
Python3

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

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].

class Solution:
def extractMax(self):
# Code here
global s
maxval = H[0]
H[0] = H[s]
s -= 1
shiftDown(0)
return maxval

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed120 / 120
Attempts : Correct / Total3 / 3Accuracy : 100%

Time Taken0.29

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Implementation of Priority Queue using Binary Heap](https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/1)
