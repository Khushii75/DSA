# Alternates in an Array

## Problem

Courses

Tutorials

Practice

Jobs

Switch to Dark Mode
99+

Menu

Back to Explore Page

Ask A DoubtMy Doubts

FREQUENTLY ASKED QUESTIONS

ProblemEditorialSubmissionsComments

Discussions ( 609 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Charles1 day agoSep 14, 2026 15:58 (GMT +5:30)

class Solution:
def getAlternates(self, arr):
return arr[::2]

solution = Solution()
solution.getAlternates([60, 63, 55, 41, 22, 11, 57])

0

Reply

Ishan Dahake3 days agoSep 13, 2026 13:53 (GMT +5:30)

class Solution {
public:
vector<int> getAlternates(vector<int> &arr) {
// code here
vector<int> ans;

for (int i = 0; i < arr.size(); i += 2)
{
ans.push_back(arr[i]);
}

return ans;
}
}; lol

0

Reply

Abhishek5 days agoSep 11, 2026 09:03 (GMT +5:30)

class Solution:
def getAlternates(self, arr):
# Code Here
arrs =[]
for i in range(len(arr)):
if i % 2 ==0:
arrs.append(arr[i])
return arrs

0

Reply

Sumit sharma1 week agoSep 09, 2026 13:33 (GMT +5:30)

i have simple solution of this question in c++                                                                         class Solution {
public:
vector<int> getAlternates(vector<int> &arr) {

for (int i = 0; i < arr.size(); i+=2) {
cout << arr[i] << " ";
}

// code here

}
};

0

Reply

Sankeerthana2 weeks agoAug 26, 2026 20:50 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {
// Code Here
ArrayList<Integer> ans=new ArrayList<>();
for(int i=0;i<arr.length;i++){
if(i%2==0)
ans.add(arr[i]);
}
return ans;
}
}

1

Reply
(Show 1 Replies)

Shrey Upadhyaya3 weeks agoAug 26, 2026 11:51 (GMT +5:30)

I checked for alternate elements through index mod 2 equal zero or not check and achieved time of completion of 0.17-0.18 second.

0

Reply

harsh1 month agoAug 12, 2026 15:41 (GMT +5:30)

Just Use Inbuilt array indexing function and return a list
like arr[0: len(arr): 2]

1

Reply

DpdUaQOc1 month agoAug 12, 2026 12:16 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {
ArrayList<Integer>array=new ArrayList<>();
// Code Here
for(int i=0;i<arr.length;i+=2){
array.add(arr[i]);
}
return array;
}

}

2

Reply

kusum kumari1 month agoAug 08, 2026 16:46 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {
// Code Here
ArrayList<Integer>list = new ArrayList<>();
int n = arr.length;
for(int i = 0; i<n; i++){
if(i%2==0){
list.add(arr[i]);
}

}
return list;
}
}

0

Reply

Mamidi Dhanalakshmi1 month agoJul 21, 2026 22:36 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {
// Code Here
ArrayList<Integer> res=new ArrayList<>();
for(int i=0;i<arr.length;i+=2){
res.add(arr[i]);
}
return res;
}
}

1

Reply

Narendra Babu2 months agoJul 01, 2026 15:44 (GMT +5:30)

import java.util.ArrayList;

class Solution {

public ArrayList<Integer> getAlternates(int[] arr) {

ArrayList<Integer> result = new ArrayList<>();

for (int i = 0; i < arr.length; i += 2) {
result.add(arr[i]);
}

return result;
}
}

1

Reply

Sailesh Mahar2 months agoJun 30, 2026 10:18 (GMT +5:30)

/**

* @param {number[]} arr

*/

class Solution {

getAlternates(arr) {

const res = []

// code here

for (let i = 0; i<arr.length; i=i+2) {

res.push(arr[i])

}

return res

}

}

0

Reply

Anonymous_Geek3 months agoJun 04, 2026 00:36 (GMT +5:30)

class Solution {
public:
vector<int> getAlternates(vector<int> &arr) {
// code here
vector <int> p;
for(int i=0;i<arr.size();i++){
if(i%2==0){
p.push_back(arr[i]);
}
}
return p;
}
};

1

Reply

Amodinee Nagrale3 months agoJun 04, 2026 00:35 (GMT +5:30)

class Solution {
public:
vector<int> getAlternates(vector<int> &arr) {
// code here
vector <int> p;
for(int i=0;i<arr.size();i=i+2){
p.push_back(arr[i]);
}
return p;
}
};

0

Reply

Kothacheruvu Devasena3 months agoMay 30, 2026 09:01 (GMT +5:30)

ans=[]
for i in range(0,len(arr),2):
ans.append(arr[i])
return ans

1

Reply

Tarun P3 months agoMay 27, 2026 14:29 (GMT +5:30)

class Solution:
def getAlternates(self, arr):
# Code Here
result=[]
for i in range(len(arr)):
if (i%2==0):
result.append(arr[i])
else:
continue
return result

0

Reply

Ishika Kokane4 months agoMay 10, 2026 21:53 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {

ArrayList<Integer> list=new ArrayList<>();

for(int i=0;i<arr.length;i++){ // if i+=2 is not used we can use if condition also
if(i%2==0){
list.add(arr[i]);
}
}

return list;
}
}

1

Reply

Swagger4 months agoMay 01, 2026 23:31 (GMT +5:30)

class Solution:
def getAlternates(self, arr):

output=[]
for i in range(len(arr)):
if(i%2==0):
output.append(arr[i])
else:
continue

return output

0

Reply

Subhash Chandra Teli5 months agoApr 04, 2026 22:31 (GMT +5:30)

class Solution {
public ArrayList<Integer> getAlternates(int arr[]) {
// Code Here
ArrayList<Integer> list = new ArrayList<>(arr.length/2);

for(int i=0 ; i<arr.length; i+=2){
list.add(arr[i]);
}

return list;
}
}

0

Reply

Kurapati   Bhargavi5 months agoApr 01, 2026 18:59 (GMT +5:30)

class Solution:
def getAlternates(self, arr):
# Code Here
return arr[::2]

0

Reply

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 2Accuracy : 50%

Points Scored 1 / 1Your Total Score:195

Time Taken0.14

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

class Solution:
def getAlternates(self, arr):
# Code Here
ans=[]
for i in range(0, len(arr), 2):
ans.append(arr[i])
return ans

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 2Accuracy : 50%

Points Scored 1 / 1Your Total Score:195

Time Taken0.14

Custom Input

## Problem Link

[Alternates in an Array](https://www.geeksforgeeks.org/problems/print-alternate-elements-of-an-array/1)
