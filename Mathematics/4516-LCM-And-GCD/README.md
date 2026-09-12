# LCM And GCD

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

LCM And GCD
Solved

Difficulty: EasyAccuracy: 37.02%Submissions: 238K+Points: 2

Given two integers a and b, You have to compute their LCM and GCD and return an array containing their LCM and GCD.
Examples:
Input: a = 5 , b = 10
Output: [10, 5]
Explanation: LCM of 5 and 10 is 10, while their GCD is 5.
Input: a = 14 , b = 8
Output: [56, 2]
Explanation: LCM of 14 and 8 is 56, while their GCD is 2.

Input: a = 1 , b = 1
Output: [1, 1]
Explanation: LCM of 1 and 1 is 1, while their GCD is 1.

Constraints:
1 ≤ a, b ≤ 104

Expected Complexities

Time Complexity: O(log(min(a, b))
Auxiliary Space: O(1)

Company Tags

SAP Labs

Topic Tags

Mathematics

Related Articles

Program To Find Lcm Of Two Numbers

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.02

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

C++ (17)
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

class Solution {
public:
int gcd(int a, int b) {
if (b == 0) return a;
return gcd(b, a % b);
}

int lcm(int a, int b) {
return (a * b) / gcd(a, b);
}
vector<int> lcmAndGcd(int a, int b) {
// code here
vector<int> ans;
ans.push_back(lcm(a,b));
ans.push_back(gcd(a,b));
return ans;
}
};

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.02

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[LCM And GCD](https://www.geeksforgeeks.org/problems/lcm-and-gcd4516/1)
