# Perfect Numbers

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

Perfect Numbers
Solved

Difficulty: EasyAccuracy: 17.21%Submissions: 266K+Points: 2

Given a number n, check if the number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.
Examples:
Input: n = 6
Output: true
Explanation: Factors of 6 are 1, 2, 3 and 6. Excluding 6 their sum is 6 which is equal to n itself. So, it's a Perfect Number.
Input: n = 10
Output: false
Explanation: Factors of 10 are 1, 2, 5 and 10. Excluding 10 their sum is 8 which is not equal to n itself. So, it's not a Perfect Number.

Input: n = 15
Output: false
Explanation: Factors of 15 are 1, 3, 5, 15. Excluding 15 their sum is 9 which is not equal to n itself. So, it's not a Perfect Number.

Constraints:
1 ≤ n ≤ 109

Expected Complexities

Time Complexity: O(sqrt(n))
Auxiliary Space: O(1)

Company Tags

Wipro

Topic Tags

Mathematics

Related Articles

Perfect Number

Discussions ( 234 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

598-KONDABOYANA GOWTHAM1 week agoSep 02, 2026 11:26 (GMT +5:30)

class Solution:
def isPerfect(self, n):
if n<=1:
return False
res=1
i=2
#the condition i*i<=n is gives half of divisors
while i*i<=n:
if n%i==0:
res+=i
if i!=n//i:# avoiding the same divisor at twice
res+=n//i# adding the both pair of divisors
i+=1
return res==n

0

Reply

Bibhu Tiwari2 weeks agoAug 23, 2026 13:14 (GMT +5:30)

class Solution {
static boolean isPerfect(int n) {
if (n <= 1) {
return false;
}

int sum = 1;

for (int i = 2; i * i <= n; i++) {
if (n % i == 0) {
sum += i;

if (i != n / i) {
sum += n / i;
}
}
}

return sum == n;
}
}

0

Reply

HqDlJezC1 month agoAug 07, 2026 00:31 (GMT +5:30)

class Solution {
public:
bool isPerfect(int n) {
int sum=0;
for(int i=1;i<=sqrt(n);i++){
if(n%i==0){
sum+=i;
if(i!=n/i){
sum+=(n/i);
}
}
}
sum-=n;
if(sum==n){
return true;

}
return false;
}
};

1

Reply

Nikhil(Edited)28/07/2026, 21:41
1 month agoJul 28, 2026 21:40 (GMT +5:30)

Python Code

class Solution:
def isPerfect(self, n):

if n <= 1:
return False

sum = 1

for i in range(2, int(n**0.5) + 1):
if n % i == 0:
sum += i

if i != n // i:
sum += n // i

return sum == n

2

Reply

Keshav Kundra1 month agoJul 24, 2026 15:18 (GMT +5:30)

class Solution {
public:
bool isPerfect(int n) {
int sum=0;
for(int i=1;i<n;i++){
if(n%i==0){
sum+=i;
}
}
if(sum==n){
return true;

}
return false;
}
};

0

Reply

GANESH KUMAR GANI5 months agoApr 02, 2026 14:41 (GMT +5:30)

// C++ Solution

class Solution {
public:
bool isPerfect(int n) {
if(n == 1) return false;

int sum = 1;

for(int i = 2; i * i <= n; i++) {
if(n % i == 0) {
sum += i;

if(i != n / i) {
sum += n / i;
}
}
}

return (sum == n);
}
};

0

Reply

priyal   gupta7 months agoJan 15, 2026 10:58 (GMT +5:30)

class Solution {
static boolean isPerfect(int n) {
if(n==1)return false;
int sum=1;
for(int i=2;i*i<=n;i++){
if(n%i==0){
sum+=i;
if(i!=n/i){
sum+=n/i;
}
}
}
return sum==n;
}
}

1

Reply

Amnipriya Sowrirajan8 months agoJan 05, 2026 05:05 (GMT +5:30)

import math
class Solution:

def isPerfect(self, n):

# code here

if n == 1:
return False

total = 1

for i in range(2, int(math.sqrt(n)) + 1):

if n % i ==0:
total +=i

if i != n//i:
total+=n//i

return total == n

0

Reply

Hemasree Nallani9 months agoNov 29, 2025 22:02 (GMT +5:30)

class Solution:
def isPerfect(self, n):
# code here

# Method 2

# factSum=list(filter(lambda x: n%x==0 ,range(1,n)))
# return sum(factSum)==n

# Method 1

# for i in range(1,n):

#     if n%i==0:

#         factSum.append(i)

# return sum(factSum)==n

# Method 3

if n <= 1:
return False

total = 1

i = 2
while i * i <= n:
if n % i == 0:
total += i
if i != n // i:
total += n // i
i += 1

return total == n

0

Reply

MEHER SURYA9 months agoNov 21, 2025 11:13 (GMT +5:30)

class Solution {
static boolean isPerfect(int n) {
int ans = sumofdiv(n);
return ans == n;
}

static int sumofdiv(int n){
int sum = 1;
for(int i = 2;i<=Math.sqrt(n);i++){
if(n%i==0){
sum = sum + i;
if( (n/i) != i){
sum = sum + n/i;
}
}

}
return sum;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 2 / 2Your Total Score:166

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
11
12
13
14

class Solution:
def isPerfect(self, n):
# code here
if n<=1:
return False
sum=1
for i in range(2, int(n**0.5)+1):
if n%i==0:
sum += i

if i != n//i:
sum+= n//i
return sum == n

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 2 / 2Your Total Score:166

Time Taken0.04

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Perfect Numbers](https://www.geeksforgeeks.org/problems/perfect-numbers3207/1)
