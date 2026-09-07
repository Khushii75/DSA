# Second Largest

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

Second Largest
Solved

Difficulty: EasyAccuracy: 26.72%Submissions: 1.6MPoints: 2Average Time: 15m

Given an array of positive integers arr[], return the second largest element from the array. If the second largest element doesn't exist then return -1.

Note: The second largest element should not be equal to the largest element.

Examples:

Input: arr[] = [12, 35, 1, 10, 34, 1]
Output: 34
Explanation: The largest element of the array is 35 and the second largest element is 34.

Input: arr[] = [10, 5, 10]
Output: 5
Explanation: The largest element of the array is 10 and the second largest element is 5.

Input: arr[] = [10, 10, 10]
Output: -1
Explanation: The largest element of the array is 10 and the second largest element does not exist.

Constraints:
2 ≤ arr.size() ≤ 105
1 ≤ arr[i] ≤ 105

Expected Complexities

Time Complexity: O(n)
Auxiliary Space: O(1)

Company Tags

SAP LabsRockstand

Topic Tags

ArraysSearching

Related Articles

Find Second Largest Element Array

Discussions ( 2298 Threads )

Commenting as Khushi KunwarComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

shivam mourya4 days agoSep 03, 2026 12:26 (GMT +5:30)

int largest = arr[0];
int secondLargest = -1;

for (int i = 1; i < n; i++) {
if (arr[i] > largest) {
secondLargest = largest;
largest = arr[i];
}
else if (arr[i] > secondLargest && arr[i] < largest) {
secondLargest = arr[i];
}
}

return secondLargest;
}

0

Reply

Raman Singh6 days agoSep 01, 2026 17:03 (GMT +5:30)

class Solution:
def getSecondLargest(self, arr):
# code here
st = nd = -1
for ch in arr:
if ch > st:
nd = st
st = ch
elif st > ch > nd:
nd = ch
return nd

1

Reply

Anonymous_Geek6 days agoSep 01, 2026 11:47 (GMT +5:30)

class Solution {
public int getSecondLargest(int[] arr) {
// code here
int n = arr.length;
int max = -1;

for (int i = 0; i < n ; i++){
if (arr[i] > max){
max = arr[i];
}
}
int Smax = -1;
for (int i = 0; i < n; i++){
if (arr[i] > Smax && arr[i] != max){
Smax = arr[i];
}
}

return Smax;
}
}

0

Reply

Sarika Kumar1 week agoAug 25, 2026 20:46 (GMT +5:30)

class Solution:
def getSecondLargest(self, arr):
# code here
arr.sort(reverse = True)
t = arr
# return t
if max(arr) == t[1]:
return -1
else:
return t[1]
s = Solution()
s.getSecondLargest([12, 35, 1, 10, 34, 1])

0

Reply

Gaming Boyah boss2 weeks agoAug 24, 2026 10:59 (GMT +5:30)

class Solution:
def getSecondLargest(self, arr):
largest = -1
second_largest = -1

for num in arr:
if num > largest:
second_largest = largest
largest = num
elif num > second_largest and num < largest:
second_largest = num

return second_largest

0

Reply

Mohammad Imran Idrishi2 weeks agoAug 18, 2026 15:23 (GMT +5:30)

Solution 1:

class Solution {
public int getSecondLargest(int[] arr) {

int largest=0, secondLargest=0;

for(int i=0; i<arr.length; i++) {

if(arr[i] > largest) {
secondLargest = largest;
largest = arr[i];
}
else if(arr[i] < largest && arr[i] > secondLargest) {
secondLargest = arr[i];
}
}

if(secondLargest == 0) {
return -1;
}

return secondLargest;
}
}

Solution 2:

class Solution {
public int getSecondLargest(int[] arr) {

int largest=arr[0], secondLargest=Integer.MIN_VALUE;

for(int i=0; i<arr.length; i++) {

if(arr[i] > largest) {
secondLargest = largest;
largest = arr[i];
}
else if(arr[i] < largest && arr[i] > secondLargest) {
secondLargest = arr[i];
}
}

if(secondLargest == Integer.MIN_VALUE) {
return -1;
}

return secondLargest;
}
}

1

Reply

Surya Prakash3 weeks agoAug 17, 2026 15:55 (GMT +5:30)

int getSecondLargest(vector<int> &arr) {
int sz=arr.size();
int max1=arr[0];
int max2=arr[1];
if (max2>max1) {
swap(max1, max2);
}
for (int i=2; i<sz; i++) {
if (arr[i]>max2 && arr[i]<max1) {
max2=arr[i];
} else if (arr[i]>max1) {
max2=max1;
max1=arr[i];
} else if (max1==max2 && arr[i]<max2) {
max2=arr[i];
}
}
if (max1==max2) {
return -1;
}
return max2;
}

2

Reply

Anonymous_Geek3 weeks agoAug 14, 2026 15:48 (GMT +5:30)

class Solution {
public:
int getSecondLargest(vector<int> &arr) {
int n = arr.size();

int max = -1;

for (int i = 0; i < n; i++) {
if (arr[i] > max) {
max = arr[i];
}
}

int Smax = -1;

for (int i = 0; i < n; i++) {
if (arr[i] > Smax && arr[i] != max) {
Smax = arr[i];
}
}

return Smax;
}
};

0

Reply

Laxmikant Hatkar4 weeks agoAug 08, 2026 19:31 (GMT +5:30)

class Solution {
public:
int getSecondLargest(vector<int> &arr) {
// code here
int n = arr.size();
sort(arr.begin(),arr.end());
for(int i=n-2;i>=0;i--){
if(arr[i]!=arr[n-1]){
return arr[i];
}
}
return -1;
}
};

0

Reply

Keshab Kumar1 month agoAug 07, 2026 10:06 (GMT +5:30)

class Solution {
public int getSecondLargest(int[] arr) {
// code here
return Arrays.stream(arr).distinct().boxed().sorted(Comparator.reverseOrder()).skip(1).findFirst().orElse(-1);
}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.18

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

C++ (17)
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
12
13
14
15
16
17

class Solution {
public:
int getSecondLargest(vector<int> &arr) {
int first = -1, second = -1;

for(int x : arr){
if(x > first){
second = first;
first = x;
} else if(x > second && x != first){
second = x;
}
}

return second;
}
};

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total2 / 2Accuracy : 100%

Time Taken0.18

You get marks only for the first correct submission if you solve the problem without viewing the full solution.

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Second Largest](https://www.geeksforgeeks.org/problems/second-largest3735/1)
