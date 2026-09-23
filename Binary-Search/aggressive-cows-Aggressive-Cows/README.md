# Aggressive Cows

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

Aggressive Cows
Solved

Difficulty: MediumAccuracy: 59.57%Submissions: 252K+Points: 4Average Time: 30m

Given an integer array arr[], which denotes the positions of stalls. All the positions are distinct. There are k aggressive cows.
Assign the cows to the stalls such that the minimum distance between any two cows is maximized.
Examples:
Input: arr[] = [1, 2, 4, 8, 9], k = 3
Output: 3
Explanation: The first cow can be placed at arr[0], the second at arr[2], and the third at arr[3]. The minimum distance between any two cows is 3 (between arr[0] and arr[2]), which is the maximum possible among all valid arrangements.
Input: arr[] = [10, 1, 2, 7, 5], k = 3
Output: 4
Explanation: The first cow can be placed at arr[0], the second at arr[1], and the third at arr[4]. In this arrangement, the minimum distance between any two cows is 4 (between arr[1] and arr[4]), which is the maximum possible among all valid arrangements.

Constraints:
arr.size() ≤ 106
0 ≤ arr[i] ≤ 108
2 ≤ k ≤ arr.size()

Expected Complexities

Time Complexity: O(n log m)
Auxiliary Space: O(1)

Topic Tags

Binary Search

Related Articles

Assign Stalls To K Cows To Maximize The Minimum Distance Between Them

Discussions ( 304 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Anonymous_Geek5 days agoSep 18, 2026 17:16 (GMT +5:30)

jo solution post kre uske kitne baap
upvote krke btao 📈

0

Reply
(Show 1 Replies)

Hasan Kamal1 week agoSep 11, 2026 12:20 (GMT +5:30)

1552. Magnetic Force Between Two Balls

this is the leetcode equivalent for this question. they are mathematically identical

1

Reply

Mohammad Hanzala2 weeks agoSep 02, 2026 21:04 (GMT +5:30)

mid is not an index here — it represents a minimum distance between cows.

1

Reply

Gaurav Mawari(Edited)30/08/2026, 18:19
3 weeks agoAug 30, 2026 18:18 (GMT +5:30)

i dont i find this quetions littel confusing in starting

0

Reply

Moksh Kulshrestha(Edited)26/08/2026, 23:20
3 weeks agoAug 26, 2026 23:19 (GMT +5:30)

🔥🔥🔥 📚 SOLUTION IN JAVA FOR BEGINNERS 📚🔥🔥🔥

class Solution {
public int aggressiveCows(int[] arr, int k) {
// code here
Arrays.sort(arr);
int ans =0;
int n = arr.length;
int high = arr[n-1] - arr[0];
int low = 1;

while (low <= high) {
int mid = low + (high - low) / 2;
if (canPlace(arr, k, mid)) {
ans = mid;
low = mid + 1;
}
else {
high = mid - 1;
}
}
return ans;

}

private boolean canPlace(int[] arr, int k, int dist) {

int cows = 1;
int lastPosition = arr[0];

for (int i = 1; i < arr.length; i++) {

if (arr[i] - lastPosition >= dist) {
cows++;
lastPosition = arr[i];
}

if (cows >= k) {
return true;
}
}

return false;
}
}

0

Reply

Shivam Kori4 weeks agoAug 25, 2026 16:32 (GMT +5:30)

i am selecting the most rated comment still i am seeing the solution on discussions not the discussions it self..

1

Reply

SHAKTI SHANKAR1 month agoAug 03, 2026 13:31 (GMT +5:30)

import java.util.*;
class Solution {
public boolean possible(int arr[], int pos, int k) {
int cow = 1;
int laststall = arr[0];
for (int i = 1; i < arr.length; i++) {
int dist = arr[i] - laststall;
if (dist >= pos) {
cow++;
laststall = arr[i];
}
if (cow >= k) {
return true;
}
}
return false;
}
public int aggressiveCows(int[] arr, int k) {
Arrays.sort(arr);
int start = 1;
int end = arr[arr.length -1]- arr[0];
int ans = -1;
while (start <= end) {
int mid = start + (end - start) / 2;
if (possible(arr, mid, k)) {
ans = mid;
start = mid + 1;
} else {
end = mid - 1;
}
}
return ans;
}
}

0

Reply

DqnpvOBz1 month agoJul 31, 2026 14:48 (GMT +5:30)

import java.util.*;
class Solution {
public boolean possible(int arr[], int pos, int k){
int cow = 1;
int laststall = arr[0];
for(int i = 1; i<arr.length; i++){
int dist = arr[i]- laststall;
if(dist>=pos){
cow++;
laststall = arr[i];
}
if(cow>=k){
return true;
}
}
return false;
}
public int aggressiveCows(int[] arr, int k) {
Arrays.sort(arr);
int start = 1;
int end = arr[arr.length - 1] - arr[0];
int ans = -1;
while(start<=end){
int mid = (start+end)/2;
if(possible(arr,mid,k)){
ans = mid;
start = mid+1;
}
else{
end = mid-1;
}
}
return ans;
}
}

0

Reply

Karan Rathore2 months agoJul 18, 2026 00:13 (GMT +5:30)

BSOA is a word of problem which often confuses, this problem is also related to BSOA, understand the problem slowly and do not hurry, take time to solve the problem.

1

Reply
(Show 1 Replies)

Himanshu2 months agoJul 12, 2026 02:05 (GMT +5:30)

We first sort the stalls because distance calculations only make sense in order. Then we binary search on the answer, where each mid represents a candidate minimum distance between cows. Using a greedy approach, we always place the next cow in the first stall that is at least mid units away from the previous cow. If we can place all k cows, we try a larger distance. Otherwise, we reduce the distance. At the end, the last successful distance (high) is the maximum minimum distance possible.

2

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:227

Time Taken1.8

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
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26

class Solution:
def minDis(self, arr, mid):

c=1
last=arr[0]
for i in range(1,len(arr)):
if arr[i]-last>=mid:
c+=1
last=arr[i]
return c

def aggressiveCows(self, arr, k):
# code here
n=len(arr)
arr.sort()
l=1
h=arr[n-1]-arr[0]
while l<=h:
mid=(l+h)//2
cows=self.minDis(arr,mid)
if cows>=k:
l=mid+1
else:
h=mid-1
return h

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1111 / 1111
Attempts : Correct / Total1 / 3Accuracy : 33%

Points Scored 4 / 4Your Total Score:227

Time Taken1.8

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Aggressive Cows](https://www.geeksforgeeks.org/problems/aggressive-cows/1)
