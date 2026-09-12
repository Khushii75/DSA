# Modular Exponentiation

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

Modular Exponentiation
Solved

Difficulty: MediumAccuracy: 52.56%Submissions: 85K+Points: 4Average Time: 30m

Given three integers x, n, and M, compute (x^n) % M, i.e., the remainder when x raised to the power n is divided by M.

Examples:

Input: x = 3, n = 2, M = 4
Output: 1
Explanation: 32 % 4 = 9 % 4 = 1.

Input: x = 2, n = 6, M = 10
Output: 4
Explanation: 26 % 10 = 64 % 10 = 4.

Constraints:
1 ≤ x, n, M ≤ 109

Expected Complexities

Time Complexity: O(log n)
Auxiliary Space: O(1)

Company Tags

GoogleMakeMyTrip

Topic Tags

Divide and ConquerBinary SearchNumber TheoryMathematicsModular Arithmetic

Related Articles

Modular Exponentiation Power In Modular Arithmetic

Discussions ( 188 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Aanshi Lahoti1 month agoJul 15, 2026 00:53 (GMT +5:30)

Easiest JAVA solution :

class Solution {
public int powMod(int x, int n, int m) {

long ans = 1;
long base = x % m;

while(n > 0){
if(n % 2 == 1){
ans = (ans*base)%m;
}
base = (base*base) % m;
n = n/2;
}

return (int) ans;
}
}

0

Reply

Dipanshu Gupta2 months agoJun 16, 2026 11:02 (GMT +5:30)

class Solution {
public:
long long powMod(int x, int n, int M) {
if(n==0){
return 1;
}
long long ans=powMod(x,n/2,M);             //use long long because it might overflow the integer
if(n%2==0){
return (ans*ans)%M;
}
else{
return ((x%M)*((ans*ans)%M))%M;
}

}
};

0

Reply

Soumya Yadav(Edited)15/04/2026, 22:25
4 months agoApr 15, 2026 22:25 (GMT +5:30)

Python ANS

class Solution:

def powMod(self, x, n, M):

# code here

return pow(x,n,M)

0

Reply

Mukesh Kumar Pathak10 months agoNov 09, 2025 13:27 (GMT +5:30)

class Solution {
public:
int powMod(int x, int n, int M) {
long long int ans=1;
long long int xx = (long long int)x;
while(n>0){
if(n&1)
ans = (ans*xx)%M;

xx = (xx*xx)%M;
n>>=1;

}

return (int)(ans%M);
}
};

0

Reply

Sourabh Kushwaha10 months agoOct 17, 2025 20:31 (GMT +5:30)

// java solution
class Solution {
public int powMod(int x, int n, int M) {
if (n == 0) {
return 1;
}
int result = 1;
x = x % M;

while (n > 0) {
if ((n & 1) == 1) {
result = (int)(((long)result * x) % M); // Typecast to long to avoid overflow
}
x = (int)(((long)x * x) % M); // Typecast to long here too
n >>= 1;
}
return result;
}

}

0

Reply

Deepak1 year agoAug 09, 2025 10:33 (GMT +5:30)

C++ Solution ✅

class Solution {
public:
int powMod(int x, int n, int M) {
long res = 1;
x %= M;
while (n) {
if (n & 1) res = res * x % M;
x = (long)x * x % M;
n >>= 1;
}
return res;
}
};

0

Reply

Ankit Jain1 year agoMay 05, 2025 23:52 (GMT +5:30)

long long int PowMod(long long int x, long long int n, long long int M) {
// Code here
if(n==1){
return x;
}

long long int ans = PowMod(x, n/2, M) % M;
ans = (ans * ans) % M;

if(n%2!=0){
ans=(ans*x) % M;
}
return ans % M;
}

0

Reply

Văn Dương Phùng1 year agoMar 24, 2025 17:31 (GMT +5:30)

class Solution
{
public:
long long int PowMod(long long int x,long long int n,long long int M)
{
x=x%M;
long long tich=1;

while(n!=0) {
if(n%2!=0) tich=(tich*(x%M))%M;

n=n/2;
x=((x%M)*(x%M))%M;
}
return tich;
}
};

0

Reply

Chanderveer Singh Chauhan2 years agoJul 12, 2024 02:31 (GMT +5:30)

long long int PowMod(long long int x,long long int N,long long int M)
{
// Code here
long long int ans = 1;
while(N>0){
if(N%2!=0) ans = (ans*x)%M;
x = (x*x)%M;
N/=2;
}
return ans;
}

0

Reply

Rahul Kumar Maity2 years agoMay 26, 2024 14:51 (GMT +5:30)

Initialization:

ans is initialized to 1. This variable will hold the result of (𝑥𝑛)%𝑀(xn)%M.

Loop Condition:

The while loop runs as long as 𝑛n is greater than 0.

Odd Check:

if(n & 1): This checks if 𝑛n is odd. The bitwise AND operation (&) with 1 will be true if the least significant bit of 𝑛n is 1 (indicating that 𝑛n is odd).

If 𝑛n is odd, ans is updated as (ans * x) \% M`. This incorporates the current value of \(x into the result.

Squaring the Base:

x = (x * x) % M: Regardless of whether 𝑛n is odd or even, the base 𝑥x is squared, and the result is taken modulo 𝑀M. This is part of the exponentiation by squaring technique.

Right Shift:

n >>= 1: This divides 𝑛n by 2 by right shifting its bits. This operation is equivalent to integer division by 2, effectively halving 𝑛n for the next iteration.

Final Result:

After the loop ends, ans holds the value of (𝑥𝑛)%𝑀(xn)%M, which is then returned as the final result.

Example Walkthrough

Let's walk through the example with 𝑥=3x=3, 𝑛=2n=2, and 𝑀=4M=4:

Initialization:

ans = 1, x = 3, n = 2, M = 4

First Iteration:

n is even (binary 10), so skip if(n & 1).

Square x: 𝑥=(3∗3)%4=9%4=1x=(3∗3)%4=9%4=1.

Right shift n: 𝑛=2≫1=1n=2≫1=1.

Second Iteration:

n is odd (binary 01), so ans = (1 * 1) \% 4 = 1.

Square x: 𝑥=(1∗1)%4=1x=(1∗1)%4=1.

Right shift n: 𝑛=1≫1=0n=1≫1=0.

End:

Loop ends as n is now 0.

Final ans = 1.

Thus, the result of 32%432%4 is 1, which matches the expected output.

This method ensures efficiency by reducing the number of multiplications through the exponentiation by squaring technique, which is especially useful for large exponents.

#include<bits/stdc++.h>

using namespace std;

class Solution

{

public:

long long int PowMod(long long int x,long long int n,long long int M)

{

long long int ans = 1;

while(n>0){

if(n&1){ // odd

ans = (ans * x) % M;

}

x = (x * x) % M;

n>>=1;

}

return ans % M;

}

};

1

Reply
(Show 1 Replies)

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:176

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

class Solution:
def powMod(self, x, n, M):
# code here
return pow(x,n,M)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:176

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Modular Exponentiation](https://www.geeksforgeeks.org/problems/modular-exponentiation-for-large-numbers5537/1)
