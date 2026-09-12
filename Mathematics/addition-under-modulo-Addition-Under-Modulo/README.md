# Addition Under Modulo

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

Addition Under Modulo
Solved

Difficulty: BasicAccuracy: 65.19%Submissions: 67K+Points: 1Average Time: 10m

Given three integers a, b, and M, compute the result of the modular addition operation: (a+b) mod M

Note: Modular operations returns the remainder when divided by M. The result will always lie in the range 0 and M - 1.

Examples :

Input: a = 10, b = 20, M = 3
Output: 0
Explanation: (10 + 20) mod 3 = 0

Input: a = 100, b = 13, M = 107
Output: 6
Explanation: (100 + 13) mod 107 = 6

Constraints:
1 ≤ a, b , M ≤ 109

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Sum Of Two Numbers Modulo M

Discussions ( 55 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana2 weeks agoAug 28, 2026 22:49 (GMT +5:30)

class Solution {
public int sumUnderModulo(int a, int b, int M) {
// code here
return (a+b)%M;
}
}

0

Reply

GANESH KUMAR GANI2 months agoJun 18, 2026 00:29 (GMT +5:30)

//C++ Solution

class Solution {
public:
int sumUnderModulo(int a, int b, int M) {
// code here
int sum  = a+b;
return sum%M;

}
};

0

Reply

Tanmay Ritesh Kanhed2 years agoFeb 16, 2024 18:29 (GMT +5:30)

********java*******
class Solution {
public static long sumUnderModulo(long a, long b){
// code here
int mod =(int)(Math.pow(10,9) + 7);
return ((a%mod)+(b%mod))%mod;

}
}

0

Reply

Ganesh Sidar2 years agoFeb 10, 2024 18:24 (GMT +5:30)

JAVA EASY SOLUTION

int mod = 1000000007;
return ((a%mod)+(b%mod))%mod;

1

Reply

David Adu Tenkorang2 years agoFeb 10, 2024 13:29 (GMT +5:30)

class Solution:
def sumUnderModulo(self,a,b):
# code here
q = a + b
return q % (10 ** 9 +7)

0

Reply

Rachit Dani2 years agoFeb 01, 2024 23:50 (GMT +5:30)

class Solution:
def sumUnderModulo(self,a,b):
# code here
return (a+b) % (10**9+7)

0

Reply

Ipshita Karmakar2 years agoDec 15, 2023 13:28 (GMT +5:30)

//User function Template for Java

//code in java

class Solution {
public static long sumUnderModulo(long a, long b){
/*long c=a+b;
long d=10^9+7;
return c%d;*/

//double m=Math.pow(10,9)+7;
//long m=Math.pow(10,9)+7;
long m=1000000007L;
long c= (a%m+b%m)%m;

return c;
}

}

0

Reply

Rajeev H R2 years agoNov 25, 2023 15:10 (GMT +5:30)

long long c = pow(10,9)+7;
return ((a%c)+(b%c))%c;

0

Reply

Ajay CS2 years agoOct 20, 2023 10:41 (GMT +5:30)

class Solution{
public:
long long sumUnderModulo(long long a,long long b)
{
// code here
const int MOD = 1000000007;
return (a % MOD + b % MOD) % MOD;
}
};

0

Reply

Anmol2 years agoOct 14, 2023 22:08 (GMT +5:30)

Code in Python

def sumUnderModulo(self,a,b):
# code here
mod = 10**9 + 7
add = a+b
res = add % mod
return res

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1110 / 1110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:178

Time Taken0.04

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

class Solution:
def sumUnderModulo(self, a, b, M):
# code here
sum= a+b
res= sum%M
return res

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1110 / 1110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:178

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Addition Under Modulo](https://www.geeksforgeeks.org/problems/addition-under-modulo/1)
