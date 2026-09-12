# Rotate Array by One

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

Rotate Array by One
Solved

Difficulty: BasicAccuracy: 69.6%Submissions: 391K+Points: 1Average Time: 20m

Given an array arr, rotate the array by one position in clockwise direction.
Examples:
Input: arr[] = [1, 2, 3, 4, 5]
Output: [5, 1, 2, 3, 4]
Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
Input: arr[] = [9, 8, 7, 6, 4, 2, 1, 3]
Output: [3, 9, 8, 7, 6, 4, 2, 1]
Explanation: After rotating clock-wise 3 comes in first position.

Constraints:
1 ≤ arr.size() ≤ 105
0 ≤ arr[i] ≤ 105

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Topic Tags

Arraysimplementation

Related Articles

C Program Cyclically Rotate Array One

Discussions ( 1555 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Rishabh(Edited)12/09/2026, 17:01
1 hour agoSep 12, 2026 17:01 (GMT +5:30)

class Solution {
public void rotate(int[] arr) {
int [] arrc=Arrays.copyOf(arr,arr.length);

int temp=arr[arr.length-1];

for(int i=1;i<arr.length;i++){
arr[i]=arrc[i-1];
}

arr[0]=temp;

return;

// code here

}
}

0

Reply

HARSH MALIK1 day agoSep 11, 2026 11:34 (GMT +5:30)

class Solution {
public void rotate(int[] arr) {
// code here
int temp = arr[ arr.length - 1 ];
for( int i = arr.length - 1  ; i>0 ; i-- ){
arr[i] = arr[i-1];
}
arr[0] = temp ;
return  ;
}
}

1

Reply

ADITYA RAJ1 week agoSep 04, 2026 12:37 (GMT +5:30)

class Solution:
def rotate(self, arr):
n=len(arr)
last=arr[-1]
for i in range(n-1,0,-1):
arr[i]=arr[i-1]

arr[0]=last
return arr

0

Reply

A Tarun2 weeks agoAug 25, 2026 23:06 (GMT +5:30)

int main()

{

int a[100],n;

cout<<"Enter the size of the array:";

cin>>n;

for(int i=0;i<n;i++)

{

cout<<"Enter the value given by the user:";

cin>>a[i];

}

int rotate_right=a[n-1];

for(int i=n-1;i>0;i--)

{

a[i]=a[i-1];

}

a[0]=rotate_right;

cout<<"the display of right rotate:"<<endl;

for(int i=0;i<n;i++)

{

cout<<a[i]<<" ";

}

return 0;

}

1

Reply

Anonymous_Geek2 weeks agoAug 23, 2026 23:25 (GMT +5:30)

class Solution {
public:
void rotate(vector<int> &arr) {
// code here
int size = arr.size();
int lastElement = arr[size-1];

for (int i= arr.size() - 1; i > 0; i--) {
arr[i] = arr[i-1];
}

arr[0] = lastElement;

}
};

0

Reply

ANURAG PATEL3 weeks agoAug 19, 2026 22:40 (GMT +5:30)

Java

class Solution {
public void rotate(int[] arr) {
// code here
int n = arr.length;

int start = n-2;
int end = n-1;
while(end>=0 && start>=0){
int temp = arr[end];
arr[end] = arr[start];
arr[start] = temp;
end --;
start = end-1;
}
return;
}
}

1

Reply

Sai Vishnu Vardhan Bathini3 weeks agoAug 19, 2026 19:40 (GMT +5:30)

#For Python3 Platform

class Solution:
def rotate(self, arr):
last = arr[-1]

for i in range(len(arr)-1, 0, -1):
arr[i] = arr[i-1]

arr[0] = last

0

Reply

Gagan Kumar1 month agoAug 10, 2026 19:31 (GMT +5:30)

class Solution {
public:
void rotate(vector<int> &arr) {
// code here
int temp1=arr[0];
int temp2=arr[1];
int temp3=arr[arr.size()-1];
for(int i=1;i<arr.size();i++){
arr[i]=temp1;
temp1=temp2;
temp2=arr[i+1];
}
arr[0]=temp3;
}
};

0

Reply

DAYAPULI SRINIVASULA RAO1 month agoAug 10, 2026 10:25 (GMT +5:30)

class Solution:
def rotate(self, arr):
lastelement=arr.pop()
arr.insert(0,lastelement)

0

Reply

Balaji Vinothkumar1 month agoAug 05, 2026 12:42 (GMT +5:30)

class Solution:
def rotate(self, arr):
# check array exists or not
if not arr:
return 1
# list sclicing method
arr[:] = arr[-1:] + arr[:-1]

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:189

Time Taken0.15

C++ (17)
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

class Solution {
public:
void rotate(vector<int> &arr) {
int n = arr.size();
int last = arr[n - 1];

for (int i = n - 1; i > 0; i--) {
arr[i] = arr[i - 1];
}

arr[0] = last;
}
};

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1115 / 1115
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:189

Time Taken0.15

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Rotate Array by One](https://www.geeksforgeeks.org/problems/cyclically-rotate-an-array-by-one2614/1)
