# Allocate Minimum Pages

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

Allocate Minimum Pages
Solved

Difficulty: MediumAccuracy: 35.51%Submissions: 468K+Points: 4Average Time: 35m

Given an array arr[] of integers, where each element arr[i] represents the number of pages in the i-th book. You also have an integer k representing the number of students. The task is to allocate books to each student such that:

Each student receives atleast one book.

Each student is assigned a contiguous sequence of books.

No book is assigned to more than one student.

All books must be allocated.

The objective is to minimize the maximum number of pages assigned to any student. In other words, out of all possible allocations, find the arrangement where the student who receives the most pages still has the smallest possible maximum. If it is not possible to allocate books to all students, return -1;

Examples:

Input: arr[] = [12, 34, 67, 90], k = 2
Output: 113
Explanation: Allocation can be done in following ways:
=> [12] and [34, 67, 90] Maximum Pages = 191
=> [12, 34] and [67, 90] Maximum Pages = 157
=> [12, 34, 67] and [90] Maximum Pages = 113.
The third combination has the minimum pages assigned to a student which is 113.

Input: arr[] = [15, 17, 20], k = 5
Output: -1
Explanation: Since there are more students than total books, it's impossible to allocate a book to each student.

Constraints:
1 ≤ arr.size() ≤ 106
1 ≤ arr[i], k ≤ 104

Expected Complexities

Time Complexity: O( n × log(sum(arr)))
Auxiliary Space: O(1)

Company Tags

InfosysAmazonMicrosoftGoogleCodenationUberNPCI

Topic Tags

SearchingDivide and Conquer

Related Interview Experiences

Amazon Interview Experience On Campus For Sde 1 5

Related Articles

Allocate Minimum Number Pages

Discussions ( 559 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

shubhkumar kachhadiya(Edited)10/09/2026, 16:47
1 week agoSep 10, 2026 16:05 (GMT +5:30)

use long long as a data type here the constraint are so high that they forget to use long long in there own declartion of integer variable

0

Reply
(Show 1 Replies)

Anonymous_Geek(Edited)30/08/2026, 00:46
2 weeks agoAug 30, 2026 00:45 (GMT +5:30)

This is the simplified explanation. Every time I think about "minimum of maximum," my mind gets into a loop the second time.

The Intuitive Analogy: Fairness in a Group Project

Imagine a teacher gives a stack of 4 contiguous textbooks to 2 students.

Books: [12, 34, 67, 90]

The teacher wants to divide the books as fairly as possible.

"Fair" means we don't want any single student to have too much workload.

So, we want to reduce the workload of the student who gets the most pages.

Let's look at all the possible ways we can split these contiguous books.

Option 1: Student 1 gets 1 book, Student 2 gets 3 books

Student 1 gets: [12] → 12 pages

Student 2 gets: [34, 67, 90] → 34 + 67 + 90 = 191 pages

The student with the highest workload has 191 pages.

So, the maximum workload for this split is 191.

Option 2: Student 1 gets 2 books, Student 2 gets 2 books

Student 1 gets: [12, 34] → 12 + 34 = 46 pages

Student 2 gets: [67, 90] → 67 + 90 = 157 pages

The student with the highest workload has 157 pages.

So, the maximum workload for this split is 157.

Option 3: Student 1 gets 3 books, Student 2 gets 1 book

Student 1 gets: [12, 34, 67] → 12 + 34 + 67 = 113 pages

Student 2 gets: [90] → 90 pages

The student with the highest workload has 113 pages.

So, the maximum workload for this split is 113.

Now compare all the splits

Split Option
Student 1 Load
Student 2 Load
Maximum Load

Option 1
12
191
191

Option 2
46
157
157

Option 3
113
90
113

Look at the last column:

191, 157, 113

For every possible split, we first found the maximum workload.

Now we choose the smallest value among those maximums.

So:

Minimum of maximum workloads = 113

Therefore, Option 3 is the fairest allocation.

The important idea

This is all "minimum of maximum" means:

First, for every possible plan, find the maximum workload.

Then, compare all those maximum workloads.

Finally, choose the smallest one.

In simple words:

Find the worst-off student in each plan, then choose the plan where the worst-off student has the smallest workload.

That's why it is called minimize the maximum.

0

Reply

Anonymous_Geek2 weeks agoAug 30, 2026 00:44 (GMT +5:30)

The Intuitive Analogy: Fairness in a Group Project

Imagine a teacher gives a stack of 4 contiguous textbooks to 2 students.

Books: [12, 34, 67, 90]

The teacher wants to divide the books as fairly as possible.

"Fair" means we don't want any single student to have too much workload.

So, we want to reduce the workload of the student who gets the most pages.

Let's look at all the possible ways we can split these contiguous books.

Option 1: Student 1 gets 1 book, Student 2 gets 3 books

Student 1 gets: [12] → 12 pages

Student 2 gets: [34, 67, 90] → 34 + 67 + 90 = 191 pages

The maximum workload for this split is 191.

Option 2: Student 1 gets 2 books, Student 2 gets 2 books

Student 1 gets: [12, 34] → 12 + 34 = 46 pages

Student 2 gets: [67, 90] → 67 + 90 = 157 pages

The maximum workload for this split is 157.

Option 3: Student 1 gets 3 books, Student 2 gets 1 book

Student 1 gets: [12, 34, 67] → 12 + 34 + 67 = 113 pages

Student 2 gets: [90] → 90 pages

The maximum workload for this split is 113.

Now compare all the splits

Split Option
Student 1 Load
Student 2 Load
Maximum Load

Option 1
12
191
191

Option 2
46
157
157

Option 3
113
90
113

<button aria-label="Copy table" data-icon-only="" data-oai-tooltip="" data-radius="full" data-size="small" data-table-copy-state="idle" data-variant="ghost" data-w-component="button" type="button"></button>

Look at the last column:

191, 157, 113

For every possible split, we first find the maximum workload.

Then, we choose the smallest value among those maximums.

So:

Minimum of maximum workloads = 113

Therefore, Option 3 is the fairest allocation.

The important idea

"Minimum of maximum" simply means:

First, find the maximum workload for every possible plan.

Then, choose the smallest maximum.

In simple words:

Find the worst-off student in each plan, then choose the plan where the worst-off student has the smallest workload.

That's why it is called "minimize the maximum."

0

Reply

VIGNESHWARA S3 weeks agoAug 29, 2026 11:49 (GMT +5:30)

class Solution {
public int findPages(int[] arr, int k) {
// code here
int n = arr.length;
if (k > n) {
return -1;
}
long low = 0;
long high = 0;
for (int pages : arr) {
low = Math.max(low, pages);
high += pages;
}
long answer = high;
while (low <= high) {
long mid = low + (high - low) / 2;
if (ispossible(arr, k, mid)) {
answer = mid;
high = mid - 1;
}
else {
low = mid + 1;
}
}
return (int) answer;
}
static boolean ispossible(int[] arr, int k, long maxpages) {
int student = 1;
long curpages = 0;
for (int pages : arr) {
if (curpages + pages > maxpages) {
student++;
curpages = pages;
if (student > k) {
return false;
}
}
else {
curpages += pages;
}
}
return true;
}
}

1

Reply

Daksh Raut3 weeks agoAug 22, 2026 19:31 (GMT +5:30)

// The limit can be large, so accept it as long long
bool helper(vector<int>& books, long long limit, int stud){
int k = 1;
long long pages = 0;

for(int i = 0; i < books.size(); i++){
if(pages + books[i] <= limit){
pages = pages + books[i];
}
else{
k++;
pages = books[i];
if(k > stud){
return false;
}
}
}
return true;
}

int findPages(vector<int> &arr, int k) {
int n = arr.size();
if(n < k){
return -1;
}

// FIX: Use long long to prevent integer overflow during summation
long long low = 0;
long long high = 0;

for(int i = 0; i < n; i++){
low = max(low, (long long)arr[i]);
high += arr[i];
}

long long res = -1;
while(low <= high){
long long guess = low + (high - low) / 2;

if(helper(arr, guess, k)){
res = guess;
high = guess - 1;
}
else{
low = guess + 1;
}
}
// Cast back to int as required by the function signature
return (int)res;
}

easy c++ code

0

Reply

Rishabh Shukla1 month agoAug 18, 2026 18:08 (GMT +5:30)

why tf people posting answer here?

4

Reply

harshalshxtgc1 month agoAug 13, 2026 15:56 (GMT +5:30)

class Solution {
public:
int chkfxn(vector<int>&arr,long long mid){
int std=1,pg=0;;
for(int i=0;i<arr.size();i++){
if(pg+arr[i]<=mid){
pg+=arr[i];
}else{
std++;
pg=arr[i];
}
}
return std;
}

int findPages(vector<int> &arr, int k) {
if (k>arr.size()){
return -1;
}
int low=arr[0];
double high=0;
for(int i=0;i<arr.size();i++){
if (arr[i]>low){
low=arr[i];
}
high+=arr[i];
}
while(low<=high){
long long mid=low+(high-low)/2;
if (chkfxn(arr,mid)>k){
low=mid+1;
}else{
high=mid-1;
}
}
return low;
}

}; tf is this throwing TLE

0

Reply
(Show 1 Replies)

harshalshxtgc1 month agoAug 13, 2026 15:56 (GMT +5:30)

class Solution {
public:
int chkfxn(vector<int>&arr,long long mid){
int std=1,pg=0;;
for(int i=0;i<arr.size();i++){
if(pg+arr[i]<=mid){
pg+=arr[i];
}else{
std++;
pg=arr[i];
}
}
return std;
}

int findPages(vector<int> &arr, int k) {
if (k>arr.size()){
return -1;
}
int low=arr[0];
double high=0;
for(int i=0;i<arr.size();i++){
if (arr[i]>low){
low=arr[i];
}
high+=arr[i];
}
while(low<=high){
long long mid=low+(high-low)/2;
if (chkfxn(arr,mid)>k){
low=mid+1;
}else{
high=mid-1;
}
}
return low;
}

}; tf is throwing T

0

Reply

Anonymous_Geek1 month agoAug 13, 2026 13:16 (GMT +5:30)

can someone point out bug in my code? 1111/1112, last one is getting runtime error.

class Solution {
public:
bool check(vector<int> &arr, int k, int n, int mid){
int needed=1;
long long int left=0;
for(int i=0;i<n;i++){
if(left+arr[i]<=mid){
left+=arr[i];
}
else{
needed++;
if(needed>k || arr[i]>mid) return 0;
left=arr[i];
}
}
if(needed<=k) return 1;
else return 0;
}
int findPages(vector<int> &arr, int k) {
// code here
int n = arr.size();
if(n<k) return -1;
int lo=0,mid,ans;
long long int hi=0;
for(auto v:arr){
lo=max(lo,v);
hi+=v;
}
while(lo<=hi){
mid=lo+(hi-lo)/2;
if(check(arr,k,n,mid)){
ans=mid;
hi=mid-1;
}
else lo=mid+1;
}
return ans;
}
};

1

Reply
(Show 1 Replies)

Anonymous_Geek1 month agoAug 01, 2026 19:47 (GMT +5:30)

class Solution {

static boolean isValidAnswer(int[] arr,int k,long mid){
long pages=0;
int studentCount = 1;
for(int i=0;i<arr.length;i++){
if(pages+arr[i]<=mid){
pages+=arr[i];
}else{
studentCount++;
if(studentCount>k || arr[i]>mid){
return false;
}else{
pages=0;
pages+=arr[i];
}
}
}
return true;
}

public int findPages(int[] arr, int k) {
// code here

int n = arr.length;

if(n<k){
return -1;
}

long s=1;
long e=0;
for(int i=0;i<n;i++){
e+=arr[i];
}

long ans = -1;

while(s<=e){
long mid = s+(e-s)/2;

if(isValidAnswer(arr,k,mid)){
ans=mid;
e=mid-1;
}
else{
s=mid+1;
}
}
return (int)ans;
}
}

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:211

Time Taken4.68

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
27
28
29
30
31

class Solution:
def studentCnt(self, arr, pages):
pageStu=0
stuCnt=1
for i in range(len(arr)):
if (pageStu + arr[i]<=pages):
pageStu+=arr[i]
else:
stuCnt+=1
pageStu=arr[i]
return stuCnt

def findPages(self, arr, k):
n=len(arr)
if(n<k):
return -1
# code here
low= max(arr)
high=sum(arr)
while low<=high:
mid= (low+high)//2
student=self.studentCnt(arr,mid)
if student > k:
low= mid+1
else:
high=mid-1

return low

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1112 / 1112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:211

Time Taken4.68

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Allocate Minimum Pages](https://www.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1)
