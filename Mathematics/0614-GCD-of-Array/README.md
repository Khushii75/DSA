# GCD of Array

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

GCD of Array
Solved

Difficulty: BasicAccuracy: 38.32%Submissions: 52K+Points: 1

Given an array of n positive integers, find the GCD of all the array elements.

Example :

Input: n = 3, arr = [1, 2, 3]
Output: 1
Explanation: GCD of 1,2,3 is 1.

Input: n = 4, arr = [2, 4, 6, 8]
Output: 2
Explanation: Greatest common divisor of all the numbers is 2.

Constraints:
1 ≤ N, arr[i] ≤ 105

Expected Complexities

Time Complexity: O(n log n)
Auxiliary Space: O(1)

Company Tags

WiproSAP Labs

Topic Tags

Mathematics

Related Articles

Gcd Two Array Numbers

Discussions ( 126 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Sankeerthana1 week agoAug 31, 2026 19:17 (GMT +5:30)

class Solution {
public int gcd(int n, int arr[]) {
// code here.
int gcd=arr[0];
for(int i=0;i<n-1;i++){
gcd=gcd(gcd,arr[i+1]);
}

return gcd;

}
static int gcd(int a,int b){
if(b==0)
return a;
return gcd(b,a%b);
}
}

0

Reply

Anonymous_Geek1 month agoAug 04, 2026 17:02 (GMT +5:30)

class Solution {
public:
int gcd(int n, vector<int> arr) {
// Your code goes here
int g = accumulate(arr.begin()+1,arr.end(),arr[0],
std::gcd<int,int>);
return g;
}
};

0

Reply

Hemal Bhatt1 month agoJul 15, 2026 09:36 (GMT +5:30)

class Solution {
public:
int get_gcd(int a,int b){
if(a==0){
return b;
}
return get_gcd(b%a,a);
}
int gcd(int n, vector<int> arr) {
int res=arr[0];
for(int i=1;i<arr.size();i++){
res=get_gcd(arr[i],res);
if(res==1){
return 1;
}
}
return res;
}
};
T.C: O(nlog(x))

0

Reply

Tobi8 months agoJan 02, 2026 15:11 (GMT +5:30)

class Solution {
public:
int gcd(int n, vector<int> arr) {
// Your code goes here
int res=arr[0];
for(int i=1;i<arr.size();i++)
res=__gcd(res,arr[i]);
return res;
}
};

1

Reply

Sai Vishnu Vardhan Bathini10 months agoNov 14, 2025 12:11 (GMT +5:30)

For Python3 Platform

from math import gcd
from functools import reduce

class Solution:
def gcd(self, n, arr):
return reduce(gcd, arr)

0

Reply

Karthik Patel1 year agoJun 07, 2025 16:17 (GMT +5:30)

TC: o(n)  IN C++

int gcd(int a, int b) {
// code here
if(a==0){return b;}
if(b==0){return a;}
return gcd(b,a%b);
}
int gcd(int n, vector<int> arr) {
// Your code goes here
int ans = arr[0];
for(int i = 1;i < n;i++){
ans = gcd(ans,arr[i]);
}
return ans;
}

1

Reply

MYTHRI PERNI1 year agoFeb 22, 2025 20:57 (GMT +5:30)

class Solution
{
public int gcd(int N , int arr[])
{
int gcd_val=arr[0];
for(int i=1;i<N;i++)
{
gcd_val=Gcd(arr[i],gcd_val);
if(gcd_val==1)
return 1;
}
return gcd_val;
}

int Gcd(int a,int b)
{
while(b!=0)
{
int temp=b;
b=a%b;
a=temp;
}
return a;
}

}

0

Reply

Victor Sankar Ghosh1 year agoJan 29, 2025 22:12 (GMT +5:30)

Python One-Liner Solution:

from math import gcd
from functools import reduce
class Solution:
def gcd(self, n, arr):
return reduce(gcd, arr)

0

Reply

niv as1 year agoJan 29, 2025 03:09 (GMT +5:30)

JAVA:

public int gcd(int N , int arr[])
{
//code here.
int gcd=arr[0];
for(int i=0;i<N-1;i++){
gcd=gcd(gcd,arr[i+1]);
}
return gcd;
}
static int gcd(int a,int b){
if (b==0) return a;
return gcd(b,a%b);
}

1

Reply

Abhishek Kumar1 year agoDec 29, 2024 22:28 (GMT +5:30)

def findgcd(self,a,b):
while a and b:
if a>b:
a=a%b
else:
b=b%a
return a if not b else b
def gcd(self, n, arr):
if n==1:
return arr[0]
curr=self.findgcd(arr[0],arr[1])
for i in range(2,n):
curr=self.findgcd(curr,arr[i])
return curr

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:179

Time Taken0.19

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

import math
class Solution:
def gcd(self, n, arr):
# code here
g=arr[0]
for i in range(1,len(arr)):
g = math.gcd(g, arr[i])
return g

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed200 / 200
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:179

Time Taken0.19

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[GCD of Array](https://www.geeksforgeeks.org/problems/gcd-of-array0614/1)
