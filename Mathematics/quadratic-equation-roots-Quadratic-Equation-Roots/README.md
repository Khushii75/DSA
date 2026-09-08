# Quadratic Equation Roots

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

Quadratic Equation Roots
Solved

Difficulty: BasicAccuracy: 12.78%Submissions: 269K+Points: 1

Given a quadratic equation ax2 + bx + c = 0, find its roots. If the equation has real roots, then return floor value of each root in decreasing order, If the roots are imaginary return -1, the driver code will print Imaginary.

Examples:

Input: a = 1, b = -2, c = 1
Output: [1, 1]
Explanation: Roots of equation x2-2x+1 are 1 and 1.

Input: a = 1, b = -7, c = 12
Output: [4, 3]
Explanation: Roots of equation x2 - 7x + 12 are 4 and 3.

Constraints:
-103 ≤ a, b, c ≤ 103

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Program To Find The Roots Of Quadratic Equation

Discussions ( 112 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Noman khan1 week agoAug 30, 2026 23:55 (GMT +5:30)

can anyone tell what the error in the code ?????????????????????????? int x1,x2,x,y;
vector<int> ans;
if((b*b-(4*a*c))>=0){
x1=(-b+sqrt(b*b-4*a*c))/(2*a);
x2=(-b-sqrt(b*b-4*a*c))/(2*a);
x=max(x1,x2);
ans.push_back(x);
y=min(x1,x2);
ans.push_back(y);

return ans;

}
else{
return {-1};
}

1

Reply
(Show 1 Replies)

Noman khan1 week agoAug 30, 2026 23:54 (GMT +5:30)

int x1,x2,x,y;
vector<int> ans;
if((b*b-(4*a*c))>=0){
x1=(-b+sqrt(b*b-4*a*c))/(2*a);
x2=(-b-sqrt(b*b-4*a*c))/(2*a);
x=max(x1,x2);
ans.push_back(x);
y=min(x1,x2);
ans.push_back(y);

return ans;

}
else{
return {-1};
}

0

Reply

Kundan Kumar(Edited)21/08/2026, 07:53
2 weeks agoAug 21, 2026 07:51 (GMT +5:30)

To find D = b * b - 4 * a * c

To check Imaginary root if D < 0

To find root x1 = (-b + Math.sqrt(D))/(2 * a);
x2 = (-b - Math.sqrt(D))/(2 * a);

class Solution {
public ArrayList<Integer> quadraticRoots(int a, int b, int c) {
// code here
ArrayList<Integer> ans = new ArrayList<>();

int D = b * b - 4 * a * c;

//Imaginary roots
if(D < 0){
ans.add(-1);
return ans;
}

double x1 = (-b + Math.sqrt(D))/(2 * a);
double x2 = (-b - Math.sqrt(D))/(2 * a);

//Floor Value
int f1 = (int) Math.floor(x1);
int f2 = (int) Math.floor(x2);

//Decreasing order
if(f1 >= f2){
ans.add(f1);
ans.add(f2);
}else{
ans.add(f2);
ans.add(f1);
}
return ans;
}
}

0

Reply

scooby doo3 weeks agoAug 17, 2026 12:30 (GMT +5:30)

I can't change the language i.e. I want to code in Java or C++ or python but it is not showing

0

Reply

Abhishek Chaturvedi4 weeks agoAug 11, 2026 18:06 (GMT +5:30)

class Solution {
public:
vector<int> quadraticRoots(int a, int b, int c) {
// code here
int d= b*b - 4*a*c;
if(d<0)return {-1};
double r1= (-b + sqrt(d))/(2.0 *a);
double r2= (-b - sqrt(d))/(2.0 *a);
int root1= floor(r1);
int root2= floor(r2);
if(root1>=root2){
return {root1, root2};
}
return {root2, root1};
}
};

0

Reply

Etteja Hoque(Edited)08/08/2026, 18:08
1 month agoAug 08, 2026 18:08 (GMT +5:30)

java solution

class Solution {
public ArrayList<Integer> quadraticRoots(int a, int b, int c) {
ArrayList<Integer> ans = new ArrayList<>();

int D = b * b - 4 * a * c;

// Imaginary roots
if (D < 0) {
ans.add(-1);
return ans;
}

double root1 = (-b + Math.sqrt(D)) / (2.0 * a);
double root2 = (-b - Math.sqrt(D)) / (2.0 * a);

// Floor values
int r1 = (int) Math.floor(root1);
int r2 = (int) Math.floor(root2);

// Decreasing order
if (r1 >= r2) {
ans.add(r1);
ans.add(r2);
} else {
ans.add(r2);
ans.add(r1);
}

return ans;
}
}

0

Reply

Etteja Hoque1 month agoAug 08, 2026 18:08 (GMT +5:30)

java solution

0

Reply

Etteja Hoque1 month agoAug 08, 2026 18:08 (GMT +5:30)

java solution

0

Reply

Abhay Yadav2 months agoJun 11, 2026 16:01 (GMT +5:30)

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
vector<int> quadraticRoots(int a, int b, int c) {
int d = b*b - 4*a*c;

if (d < 0) {
return {-1};  // imaginary roots
}

// Calculate roots
double root1 = (-b + sqrt(d)) / (2.0 * a);
double root2 = (-b - sqrt(d)) / (2.0 * a);

// Floor the values
int r1 = floor(root1);
int r2 = floor(root2);

// Return in decreasing order
if (r1 >= r2) {
return {r1, r2};
} else {
return {r2, r1};
}
}
};

1

Reply

Gaurav Sharma2 years agoFeb 13, 2024 13:31 (GMT +5:30)

vector<int> quadraticRoots(int a, int b, int c) {
// code here
vector<int> out;
float r1,r2,desc;
desc=(b*b)-(4*a*c);
if(desc>0){
r1=floor((-b+sqrt(desc))/(2*a));
r2=floor((-b-sqrt(desc))/(2*a));

if(r1>r2){
out.push_back(r1);
out.push_back(r2);
}else{
out.push_back(r2);
out.push_back(r1);
}
return out;
}
else if(desc==0){
r1=-b/(2*a);
r2=r1;

if(r1>r2){
out.push_back(r1);
out.push_back(r2);
}else{
out.push_back(r2);
out.push_back(r1);
}
return out;
}
else{
cout<<"Imaginary";
}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed110 / 110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:147

Time Taken0.03

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
8
9
10
11

from math import sqrt, floor
class Solution:
def quadraticRoots(self, a, b, c):
# code here
d= b*b-4*a*c
if d<0:
return [-1]
root1= floor((-b+ sqrt(d))/(2*a))
root2= floor((-b- sqrt(d))/(2*a))

return [root1, root2]

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed110 / 110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:147

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Quadratic Equation Roots](https://www.geeksforgeeks.org/problems/quadratic-equation-roots/1)
