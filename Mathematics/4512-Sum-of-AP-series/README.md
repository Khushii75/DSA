# Sum of AP series

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

Sum of AP series
Solved

Difficulty: BasicAccuracy: 31.98%Submissions: 45K+Points: 1

A series with same common difference is known as arithmetic series. The first term of series is 'a' and common difference is d. The series looks like a, a + d, a + 2d, a + 3d, . . . Find the sum of series upto nth term.

Examples :

Input: n = 5, a = 1, d = 3
Output: 35
Explanation: Series upto 5th term is 1 4 7 10 13, so sum will be 35.

Input: n = 3, a = 1, d = 2
Output: 9
Explanation: Series upto 3rd term is 1 3 5, so sum will be 9.

Constraints:
1 ≤ n ≤ 500
0 ≤ a, d ≤ 500

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Program Sum Arithmetic Series

Discussions ( 52 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

ROHIT GHORAI3 days agoSep 08, 2026 17:05 (GMT +5:30)

class Solution {
public int sumOfAP(int n, int a, int d) {
int sum = n*a;
n--;
sum += d*(n*(n+1)/2);
return sum;
}
};

0

Reply

Sankeerthana1 week agoAug 30, 2026 22:23 (GMT +5:30)

class Solution {
public int sumOfAP(int n, int a, int d) {
// code here
int s=(n*(2*a+(n-1)*d))/2;
return s;
}
};

0

Reply

Sumit Kumar1 month agoAug 09, 2026 11:16 (GMT +5:30)

class Solution {
public int sumOfAP(int n, int a, int d) {
// code here
int sum = 0;
for (int i = 0; i < n; i++) {
int term = a + d*i;
sum += term;
}
return sum;
}
};

0

Reply

DAYAPULI SRINIVASULA RAO6 months agoFeb 26, 2026 14:43 (GMT +5:30)

User function Template for python3

class Solution:
def sum_of_ap(self, n, a, d):
# Code here
res=(n/2)*((2*a)+(n-1)*d)
return int(res)

1

Reply

Sai Vishnu Vardhan Bathini10 months agoNov 05, 2025 10:38 (GMT +5:30)

For Python3 Platform

class Solution:
def sum_of_ap(self, n, a, d):
total_sum = (n * (2*a + (n-1)*d))//2

return total_sum

0

Reply

Mukesh Kumar Pathak10 months agoNov 03, 2025 01:36 (GMT +5:30)

class Solution {
public:
long sum_of_ap(long n, long a, long d) {
long sum = (long)(n*((2*a) + ((n-1)*d)));
sum /= 2;
return sum;
}
};

0

Reply

VANSH SINGH SAINI1 year agoAug 21, 2025 18:42 (GMT +5:30)

class Solution {
//OPTIMAL APPROACH:
public long sum_of_ap(long n, long a, long d) {

return (n*(2*a+(n-1)*d))/2;
}
}

//T(n) = O(1)
//Sc = O(1)

/*class Solution {
//BRUTE FORCE APPROACH:
public long sum_of_ap(long n, long a, long d) {
long sumAP = a;
for(int i = 1;i<n;i++){
sumAP +=(a+i*d);
}
return sumAP;
}
}

//T(n) = O(n)
//Sc = O(1)*/

1

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1011 / 1011
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:180

Time Taken0.03

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

class Solution:
def sumOfAP(self, n, a, d):
# code here
s= n/2*(2*a+(n-1)*d)
return int(s)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1011 / 1011
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:180

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Sum of AP series](https://www.geeksforgeeks.org/problems/sum-of-ap-series4512/1)
