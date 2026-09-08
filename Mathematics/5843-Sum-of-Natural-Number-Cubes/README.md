# Sum of Natural Number Cubes

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

Sum of Natural Number Cubes
Solved

Difficulty: BasicAccuracy: 23.17%Submissions: 211K+Points: 1

Given an integer n, calculate the sum of series 13 + 23 + 33 + 43 + … till n-th term.

Examples:

Input: n = 5
Output: 225
Explanation: 13 + 23 + 33 + 43 + 53 = 225

Input: n = 7
Output: 784
Explanation: 13 + 23 + 33 + 43 + 53 + 63 + 73 = 784

Constraints:
1 <= n <= 200

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Program Cube Sum First N Natural Numbers

Discussions ( 390 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Kundan Kumar2 weeks agoAug 21, 2026 08:11 (GMT +5:30)

Java Program

0

Reply

Sachin Kumar1 month agoAug 06, 2026 02:43 (GMT +5:30)

class Solution {
public:
int sumOfSeries(int n) {
// code here
int sum = 0;
for (int i=1; i<=n; i++) {
int power = pow(i, 3);  // pow is by default library function in c++ which help to calculate power a to the b easily .
sum = sum + power;
}
return sum;
}
};

0

Reply

Ayush Mishra1 month agoAug 01, 2026 02:28 (GMT +5:30)

class Solution {
int sumOfSeries(int n) {
// code here
int i=1;
int sum=0;
while(i<=n){
sum= sum+i*i*i;
i++;
}
return sum;
}
}

0

Reply

chirag bhargava2 months agoJul 02, 2026 14:29 (GMT +5:30)

#Best approach using maths formula with TC/SC -> O(1)
class Solution:
def sumOfSeries(self, n: int) -> int:
return (n * (n + 1) // 2) ** 2

0

Reply

Ashu2 months agoJul 02, 2026 10:48 (GMT +5:30)

class Solution:
def sumOfSeries(self,n):
#code here
res = n+1
res = int((n*res)/2)
return res**2

0

Reply

Ishwar Inamdar2 months agoJun 29, 2026 10:29 (GMT +5:30)

class Solution:
def sumOfSeries(self,n):
#Python code here
num = 0
for i in range (1, n+1):
num += i*i*i
return num

1

Reply

Am I Om3 months agoJun 04, 2026 19:58 (GMT +5:30)

int sumOfSeries(int n) {
if(n==0){return 0;}
return (pow(n,3) + sumOfSeries(n-1));
}

Most simple code that you'll ever find! Hope it helps! Thanks!

0

Reply

Hemasri Reddy(Edited)24/05/2026, 19:15
3 months agoMay 24, 2026 19:15 (GMT +5:30)

Recursion
// User function Template for Java

class Solution {
int sumOfSeries(int n) {
// code here
if(n==0){
return 0;
}
if(n==1){
return 1;
}
return (n*n*n)+sumOfSeries(n-1);
}
}

0

Reply

KEYUR NANDVANA3 months agoMay 21, 2026 03:11 (GMT +5:30)

// User function Template for Java

class Solution {
int sumOfSeries(int n) {
int ans = 0;
for (int i = 1 ; i<=n ;i++){
ans += Math.pow(i,3);
}
return ans ;

}
}

1

Reply

Adithya Gugloth5 months agoApr 07, 2026 09:54 (GMT +5:30)

class Solution {
int sumOfSeries(int n) {
// code here
int sum = n * (n + 1)/2;
return sum*sum;
}
}

2

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:149

Time Taken0.03

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

class Solution:
def sumOfSeries(self,n):
#code here
return (n*(n+1)//2)**2

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:149

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Sum of Natural Number Cubes](https://www.geeksforgeeks.org/problems/sum-of-first-n-terms5843/1)
