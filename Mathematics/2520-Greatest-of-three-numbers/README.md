# Greatest of three numbers

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

Greatest of three numbers
Solved

Difficulty: BasicAccuracy: 48.72%Submissions: 116K+Points: 1

Given three numbers a, b and c. Find the greatest number among them.

Examples:

Input: a = 10, b = 3, c = 2
Output: 10
Explanation: 10 is greatest among the three

Input: a = -4, b = -3, c = -2
Output: -2
Explanation: -2 is greatest among the three

Constraints:
-109≤ a, b, c ≤109

Expected Complexities

Time Complexity: O(1)
Auxiliary Space: O(1)

Topic Tags

Mathematics

Related Articles

Cpp Program To Find Largest Among Three NumbersJava Program To Find The Largest Of Three Numbers

Discussions ( 145 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Bibhu Tiwari1 day agoSep 08, 2026 08:19 (GMT +5:30)

import java.util.Scanner;

class GFG {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);

int a = sc.nextInt();
int b = sc.nextInt();
int c = sc.nextInt();

System.out.println(Math.max(Math.max(a, b), c));//just using maths function in it that make is easy
}
}

0

Reply

Sankeerthana2 weeks agoAug 26, 2026 15:28 (GMT +5:30)

import java.util.Scanner;

class GFG {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);

int a = sc.nextInt();
int b = sc.nextInt();
int c = sc.nextInt();

// code here
if(a>b && a>c)
System.out.print(a);
else if(b>c)
System.out.print(b);
else
System.out.print(c);
}
}

0

Reply

Varnit Sharma3 weeks agoAug 17, 2026 20:42 (GMT +5:30)

a = int(input())
b = int(input())
c = int(input())

# code here
if(a>b and a>c):
print (a);
if(b>a and b>c):
print (b);
if(c>a and c>b):
print (c);

0

Reply

Joselyn Reyna Contreras3 weeks agoAug 13, 2026 23:54 (GMT +5:30)

# Option 1
print(max(a,b,c))

#Option 2
if a>b:
if a>c:
print(a)
else:
print(c)
else:
print(b)

0

Reply

tolatiuk5q3 weeks agoAug 13, 2026 13:20 (GMT +5:30)

C# algorithm

using System;

class GfG {

static void Main() {

int a = int.Parse(Console.ReadLine());

int b = int.Parse(Console.ReadLine());

int c = int.Parse(Console.ReadLine());

// code here

int[] numbers = {a, b, c};

int max_number = numbers[0];

foreach(int num in numbers)

{

if( num > max_number)

{

max_number = num;

}

}

Console.WriteLine(max_number);

}

}

0

Reply

Suneetha Perugu(Edited)11/07/2026, 11:26
2 months agoJul 11, 2026 11:24 (GMT +5:30)

python code

a = int(input())

b = int(input())

c = int(input())

if a>b and a>c:

print(a)

elif  b>a and b>c:

print(b)

else:

print(c)

0

Reply

Suneetha Perugu2 months agoJul 11, 2026 11:21 (GMT +5:30)

a= int(input())

0

Reply

Anonymous_Geek2 months agoJun 19, 2026 18:57 (GMT +5:30)

a = int(input())
b = int(input())
c = int(input())
print(max(a,b,c))

0

Reply

HIMANSHU PANDEY3 months agoMay 21, 2026 20:46 (GMT +5:30)

int max1 = Math.max(a,b);
int res = Math.max(max1,c);

System.out.println(res);

0

Reply
(Show 1 Replies)

Prateek Yadav4 months agoMay 11, 2026 07:49 (GMT +5:30)

import java.util.Scanner;

class GFG {
public static void main(String[] args) {
Scanner sc = new Scanner(System.in);

int a = sc.nextInt();
int b = sc.nextInt();
int c = sc.nextInt();

// code here
if(a > b && a > c){
System.out.print(a);
}else if(b > a && b > c){
System.out.print(b);
}else{
System.out.print(c);
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

Test Cases Passed5 / 5
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:153

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

a = int(input())
b = int(input())
c = int(input())

# code here
if a>b and a>c:
print(a)
elif b>c and b>a:
print(b)
else:
print(c)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed5 / 5
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:153

Time Taken0.03

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Greatest of three numbers](https://www.geeksforgeeks.org/problems/greatest-of-three-numbers2520/1)
