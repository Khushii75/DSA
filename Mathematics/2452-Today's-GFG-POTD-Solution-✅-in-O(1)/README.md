# Today's GFG POTD Solution ✅ in O(1)

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

Sum of Natural Numbers
Solved

Difficulty: BasicAccuracy: 61.45%Submissions: 398K+Points: 1Average Time: 5m

Given an integer n, compute the sum of all natural numbers from 1 to n (inclusive). If n is 0, the sum should be 0.

Examples:

Input: n = 6
Output: 21
Explanation: The sum of natural numbers up to 6 is: 1 + 2 + 3 + 4 + 5 + 6 = 21.

Input: n = 4
Output: 10
Explanation: The sum of natural numbers up to 4 is: 1 + 2 + 3 + 4 = 10.

Input: n = 0
Output: 0
Explanation: Since n is 0, the sum is 0.

Constraints:
0 ≤ n ≤ 104

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Program Find Sum First N Natural Numbers

Discussions ( 244 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Gurmeet Singh3 years agoJun 21, 2023 11:34 (GMT +5:30)

Today's GFG POTD Solution ✅ in O(1)

Simple Mathematical Formula ????
1+2+3+ --- +n =n*(n+1)/2

But n is in 10^7 so when we multiply n*(n+1) -> so it will be in long range so, multiply 1LL to handle that and at the end just do %mod

So, Sum=((n*1LL*(n+1))/2)%mod

I hope you get it ????

For More Such Solutions , Join Our Community⬇️

https://telegram.me/FastForward_Coders

Code :

#define mod (int)(1e9 + 7)
int sumOfNaturals(int n)
{
return ((n*1LL*(n+1))/2)%mod;
}

9

Reply
(Show 2 Replies)

Vidit Jain3 years agoJun 21, 2023 11:07 (GMT +5:30)

CORRECT SOLUTION WITH OR WITHOUT EXPANDING USING MODULUS PROPERTIES

Sum of the first 'n' natural numbers is calculated using the formula: 1 + 2 + 3 + ... + 'n' = (n * (n + 1)) / 2.

It's important to handle the value of (n*(n+1))/2 for larger values of n by casting the result to a long data type.

(a*b)%mod = ((a%mod)*(b%mod))%mod

(a/b)%mod = ((a%mod)*((modular inverse of b)%mod))%mod

WITH EXPANDING :

int sumOfNaturals(int n) {
// code here
int mod=1e9+7;
int ans = ((((long)n*(long)(n+1))%mod)*500000004)%mod;
// 500000004 -> Modular Inverse of 2
return ans;
}

WITHOUT EXPANDING :

int sumOfNaturals(int n) {
// code here
int mod=1e9+7;
long ans=(long)n*(long)(n+1);
ans/=2;
return ans%mod;
}

Follow my telegram channel for more such daily POTD solutions with approach

https://t.me/leetcodegfgdailysolution

10

Reply

GeeksforGeeks3 years agoJun 21, 2023 10:44 (GMT +5:30)

Hi Everyone,

Thank you for reporting the fault with the test cases.
As a result, we have updated the test cases accordingly in order to avoid any ambiguity.
Please try now.

Keep Coding :)

Regards
Practice Team
GeeksforGeeks

16

Reply
(Show 3 Replies)

Sylvester1 week agoAug 31, 2026 17:21 (GMT +5:30)

n = int(input())

# code here
sum = 0
for i in range(1, n + 1):
sum += i

print(sum)

0

Reply

JAYPRATAP SINGH DOLIYA(Edited)19/08/2026, 23:26
2 weeks agoAug 19, 2026 23:25 (GMT +5:30)

n = int(input())
print(n*(n+1)//2)

0

Reply

Siddhant   Patel1 month agoJul 26, 2026 16:07 (GMT +5:30)

Time for a recursive approach:
class GFG {
public static int Sum(int n){
if(n == 0) return 0;
if(n == 1) return 1;

return n + Sum(n-1);
}
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
System.out.print(Sum(n));
}
}

0

Reply

KK1 month agoJul 12, 2026 16:20 (GMT +5:30)

identify pattern and solve it by using loop it's take O(n) time but using formula n*(n+1)/2 it will take O(1) time

0

Reply

Aryan Kumar2 months agoJul 08, 2026 12:10 (GMT +5:30)

#include <iostream>
using namespace std;

int main() {
int n;
cin >> n;

// code here

int sum = 0;

for(int i=1; i<=n; i++){
sum += i;
}
cout<<sum;

return 0;
}

0

Reply

saipadmasri yadavalli2 months agoJun 12, 2026 21:15 (GMT +5:30)

import java.util.Scanner;

class GFG {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
int sum=0;
// code here
for(int i=1;i<=n;i++){
sum=sum+i;

}
System.out.println(sum+"");
}
}

0

Reply

Basavaraj Belur2 months agoJun 12, 2026 08:55 (GMT +5:30)

// code here
int sum = 0;
if(n == 0) {
sum = 0;
}
else {
for(int i=n; i>0; i--) {
sum += i;
}
}
System.out.println(sum);

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed5 / 5
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:145

Time Taken0.02

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

n = int(input())

# code here
def Nsum(n):
sum = n*(n+1)//2
return sum
print(Nsum(n))

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed5 / 5
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:145

Time Taken0.02

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Today's GFG POTD Solution ✅ in O(1)](https://www.geeksforgeeks.org/problems/reverse-coding2452/1)
