# Middle of Three

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

Middle of Three
Solved

Difficulty: BasicAccuracy: 54.8%Submissions: 98K+Points: 1

Given three distinct numbers a, b and c. Find the number with a value in the middle (Try to do it with minimum comparisons).

Examples :

Input: a = 978, b = 518, c = 300
Output: 518
Explanation: Since 518>300 and 518<978, so 518 is the middle element.

Input: a = 162, b = 934, c = 200
Output: 200
Exaplanation: Since 200>162 && 200<934, So, 200 is the middle element.

Input: a = 246, b = 214, c = 450
Output: 246

Constraints:
1<=a, b, c<=109
a, b, c are distinct.

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

MathematicsNumbers

Related Articles

Maximum And Minimum In An Array

Discussions ( 404 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

A C Kulkarni3 days agoSep 06, 2026 14:27 (GMT +5:30)

Simple ternary. At most 3 comparisons in any scenario.

int middle(int a, int b, int c) {
// code here
return
a < b
? (b < c ? b : (a < c ? c : a))
: (b > c ? b : (a < c ? a : c));
}

0

Reply

Sankeerthana2 weeks agoAug 26, 2026 15:30 (GMT +5:30)

class Solution {
int middle(int a, int b, int c) {
// code here
if((a>b && a<c)||(a<b && a>c))
return a;
else if((b>a && b<c)||(b>c && b<a))
return b;
else
return c;
}
}

0

Reply

Shobhit Chauhan3 weeks agoAug 17, 2026 13:52 (GMT +5:30)

class Solution {
int middle(int a, int b, int c) {
if((a>b) != (a>c)) return a;
if((b>a) != (b>c)) return b;
return c;
}
}

0

Reply

Shreyansh Kumar4 weeks agoAug 12, 2026 09:36 (GMT +5:30)

class Solution {
public:
int middle(int a, int b, int c) {
// code here
int maxi = max(a, max(b, c));
int mini = min(a, min(b, c));
if(maxi > a && a> mini) return a;
else if(maxi > b && b > mini) return b;
else return c;
}
};

0

Reply

Nischay Prasher3 months agoMay 14, 2026 23:11 (GMT +5:30)

class Solution {
int middle(int a, int b, int c) {
int max = Math.max(Math.max(a, b), c);
int min = Math.min(Math.min(a, b), c);
return (a + b + c) - max - min;
}
}

2

Reply

Ayush Adhikari4 months agoApr 28, 2026 13:50 (GMT +5:30)

// User function Template for Java

class Solution {
int middle(int a, int b, int c) {
// code here
int[] ans = new int[3];
ans[0] = a;
ans[1] = b;
ans[2] = c;

Arrays.sort(ans);

return ans[1];
}
}

0

Reply

Rohit lonkar5 months agoMar 25, 2026 16:40 (GMT +5:30)

class Solution {
int middle(int a, int b, int c) {
// code here

if( ( a > b && a < c ) || ( a < b  && a > c ) ) {
return a;
}
else if(  ( b > a && b < c  ) || (  b < a && b > c ) ) {
return b;
}
else return c;
}
}

0

Reply

Sai Vishnu Vardhan Bathini10 months agoNov 03, 2025 16:05 (GMT +5:30)

For Python3 Platform

class Solution:
def middle(self, a, b, c):
l = [a, b, c]
l.sort()

return l[1]

0

Reply

Shivam Singh10 months agoOct 22, 2025 22:37 (GMT +5:30)

Java Solution

// User function Template for Java

class Solution {
int middle(int a, int b, int c) {

if((b > a && b < c )|| (b < a && b > c)){
return b;
}else if( (b < a && a < c )|| (b > a && c < a)){
return a;
}else{
return c;
}

}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 2Accuracy : 50%

Points Scored 1 / 1Your Total Score:154

Time Taken0.04

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

class Solution:
def middle(self, a, b, c):
#code here
if (a>=b and b>=c) or (a<=b and b<=c):
return b
elif (b>=a and a>=c) or (b<=a and a<=c):
return a
else:
return c

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 2Accuracy : 50%

Points Scored 1 / 1Your Total Score:154

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Middle of Three](https://www.geeksforgeeks.org/problems/middle-of-three2926/1)
