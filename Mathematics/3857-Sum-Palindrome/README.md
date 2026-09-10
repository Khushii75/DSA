# Sum Palindrome

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

Sum Palindrome
Solved

Difficulty: BasicAccuracy: 19.13%Submissions: 52K+Points: 1Average Time: 5m

Given a number, reverse it and add it to itself unless it becomes a palindrome or return -1 if the number of iterations becomes more than 5. Return that palindrome number if it becomes a palindrome else, it returns -1.

Examples:

Input: n = 23
Output: 55
Explanation: reverse(23) = 32, then 32+23 = 55 which is a palindrome.

Input: n = 73
Output: 121
Explanation: reverse(73) = 37, then 37+73 = 110 which is not a palindrome, again reverse(110)= 011, then 110+11 = 121 which is a palindrome.

Constraints:
1 <= n <= 104

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Company Tags

Zoho

Topic Tags

Mathematicspalindrome

Related Interview Experiences

Zoho Interview Experience Set 21 Campus

Related Articles

Reverse And Add Function

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed204 / 204
Attempts : Correct / Total3 / 4Accuracy : 75%

Time Taken0.03

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

class Solution:
def isSumPalindrome (self, n):
# code here
if str(n) == str(n)[::-1]:
return n

for i in range(5):
rev= int(str(n)[::-1])
n += rev
if str(n)==str(n)[::-1]:
return n
return -1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed204 / 204
Attempts : Correct / Total3 / 4Accuracy : 75%

Time Taken0.03

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Sum Palindrome](https://www.geeksforgeeks.org/problems/sum-palindrome3857/1)
