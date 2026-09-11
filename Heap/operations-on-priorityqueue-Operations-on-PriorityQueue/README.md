# Operations on PriorityQueue

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

Operations on PriorityQueue
Solved

Difficulty: EasyAccuracy: 75.01%Submissions: 17K+Points: 2

Given an integer array a[], your task is to add these elements to the PriorityQueue. Also, given an array b[], the task is to check if the given element is present in the PriorityQueue or not.
If the element is present, then 1 is printed by the driver code, after that the max element of priority queue is printed. Then the driver code deletes the max element.
Note: Here the driver code has implemented the PriorityQueue as a max-heap.

Example:

Input: a[] = [1, 2, 3, 4, 5, 2, 3, 1], b[] = [1, 3, 2, 9, 10]
Output: 1 5 1 4 1 3 -1 -1
Explanation: After inserting elements present in a[], when we find b[0] = 1, which is present, so 1 gets printed, and then the top element of the PriorityQueue which is 5 gets printed, and then it gets deleted. Similarly, when element is not present, just -1 is printed.

Input: a[] = [1, 2, 3, 4], b[] = [1, 10]
Output: 1 4 -1
Explanation: After inserting elements present in a[], when we find b[0] = 1, which is present, so 1 gets printed, and then the top element of the PriorityQueue which is 4 gets printed, and then it gets deleted. Similarly, when element is not present, just -1 is printed.

Constraints:
1 ≤ a.size(), b.size() ≤ 103

Expected Complexities

Time Complexity: O(n log n)
Auxiliary Space: O(n log n)

Topic Tags

JavaJava-CollectionsHeap

Related Articles

Priority Queue Set 1 Introduction

Discussions ( 23 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Arsh Agarwal1 year agoJan 18, 2025 15:59 (GMT +5:30)

Easy JAVA solution

class Geeks {

// Function to insert element into the queue
static void insert(PriorityQueue<Integer> q, int k) {

// Your code here
// Just insert k in q and don't return anything
q.add(k);
}

// Function to find an element k
static boolean find(PriorityQueue<Integer> q, int k) {

// Your code here
// If k is in q return true else return false

return q.contains(k);
}

// Function to delete the max element from queue
static int delete(PriorityQueue<Integer> q) {

// Your code here
// Delete the max element from q. The priority queue property might be useful
// here

return q.poll();
}
}

1

Reply

Vikash Kumar1 year agoDec 10, 2024 13:11 (GMT +5:30)

Simple Java Solution

class Geeks {

// Function to insert element into the queue
static void insert(PriorityQueue<Integer> q, int k) {

// Your code here
// Just insert k in q and don't return anything
q.offer(k);
}

// Function to find an element k
static boolean find(PriorityQueue<Integer> q, int k) {

// Your code here
// If k is in q return true else return false
if(q.contains(k)){
return true;
}
else{
return false;
}
}

// Function to delete the max element from queue
static int delete(PriorityQueue<Integer> q) {

// Your code here
// Delete the max element from q. The priority queue property might be useful
// here
return q.poll();
}
}

0

Reply

AWADH RAJ Patel1 year agoOct 10, 2024 12:27 (GMT +5:30)

Java Lovers

//User function Template for Java

// Helper class Geeks to implement
// insert() and findFrequency()
class Geeks{

// Function to insert element into the queue
static void insert(PriorityQueue<Integer> q, int k){

// Your code here
//Just insert k in q and don't return anything
q.add(k);
}

// Function to find an element k
static boolean find(PriorityQueue<Integer> q, int k){

// Your code here
// If k is in q return true else return false
for(int x:q){
if(x==k)
return true;
}
return false;
}

// Function to delete the max element from queue
static int delete(PriorityQueue<Integer> q){

// Your code here
//Delete the max element from q. The priority queue property might be useful here
int max =0;
for(int ele:q){
if(max<ele)
max=ele;
}
if(q.size()!=0)
q.remove(max);
return max;

}

}

0

Reply

G Vishnu Vardhan2 years agoApr 11, 2024 16:43 (GMT +5:30)

SIMPLE PYTHON SOLUTION

----------------------------------------

# Helper class Geeks to implement

# insert() and findFrequency()

class Geeks:

# Function to insert element into the queue

def insert(self, q, k):

q.append(k)

# Your code here

# Just insert k in q and don't return anything

# Function to find an element k

def find(self, q, k):

return 1 if k in q else 0

# Your code here

# If k is in q return true else return false

# Function to delete the max element from queue

def delete(self, q):

m=max(q)

q.remove(m)

return m

# Your code here

# Delete the max element from q. The priority queue property might be useful here

#{

# Driver Code Starts

import heapq

# Driver class with driver code

if __name__ == '__main__':

# Taking input using input() method

testcase = int(input())

while testcase > 0:

# Priority Queue with comparator

p_queue = []

n = int(input())

# Invoking object of Geeks class

obj = Geeks()

elements = list(map(int, input().split()))

for i in range(n):

obj.insert(p_queue, elements[i])

# Taking total number of queries

x = int(input())

lst = list(map(int, input().split()))

# If the element entered is present

# in the PriorityQueue then we print

# "1" and delete the maximum element

# else we print "-1"

for i in range(x):

k = lst[i]

f = obj.find(p_queue, k)

if f:

print("1")

print(obj.delete(p_queue))

else:

print("-1")

testcase -= 1

# } Driver Code Ends

0

Reply

Mohit Anand2 years agoMar 08, 2024 22:26 (GMT +5:30)

class Geeks{

// Function to insert element into the queue
static void insert(PriorityQueue<Integer> q, int k){
q.add(k);

}

// Function to find an element k
static boolean find(PriorityQueue<Integer> q, int k){

for(int i:q) {
if(i==k) return true;
}
return false;

}

// Function to delete the max element from queue
static int delete(PriorityQueue<Integer> q){

int maxi=0;
for(int element: q) {
if(element>maxi) {
maxi = element;
}
}
if(q.size()!=0) {
q.remove(maxi);
}
return maxi;
}

}

0

Reply

Md Rahmatullah2 years agoDec 13, 2023 14:03 (GMT +5:30)

class Geeks{
static void insert(PriorityQueue<Integer> q, int k){
q.add(k);
}

static boolean find(PriorityQueue<Integer> q, int k){
for(int x:q){
if(x==k)
return true;
}
return false;
}

static int delete(PriorityQueue<Integer> q){
int max=0;
for(int ele:q){
if(max<ele)
max=ele;
}
if(q.size()!=0)
q.remove(max);
return max;
}
}

0

Reply

Manish Shee3 years agoAug 05, 2023 10:29 (GMT +5:30)

Python Code:-

class Geeks:

# Function to insert element into the queue
def insert(self, q, k):
q.append(k)

# Function to find an element k
def find(self, q, k):
return 1 if k in q else 0

# Function to delete the max element from queue
def delete(self, q):
largest = max(q)
q.remove(largest)

return largest

0

Reply

Shourya3 years agoJul 24, 2023 17:07 (GMT +5:30)

This is java code!

static void insert(PriorityQueue<Integer> q, int k){

// Your code here
//Just insert k in q and don't return anything
q.add(k);
}

static boolean find(PriorityQueue<Integer> q, int k){

// Your code here
// If k is in q return true else return false
for(int x:q){
if(x==k) return true;
}
return false;

}

static int delete(PriorityQueue<Integer> q){

// Your code here
//Delete the max element from q. The priority queue property might be useful here
int max = 0;
for(int y:q){
if(max<y) max = y;
}
if(q.size()!=0) q.remove(max);

return max;
}

0

Reply

Madhavi Sonawane4 years agoAug 17, 2022 11:20 (GMT +5:30)

Time Taken : 0.22
class Geeks{
static void insert(PriorityQueue<Integer> q, int k){
q.add(k);
}

static boolean find(PriorityQueue<Integer> q, int k){
for(int x:q){
if(x==k)
return true;
}
return false;
}

static int delete(PriorityQueue<Integer> q){
int max=0;
for(int ele:q){
if(max<ele)
max=ele;
}
if(q.size()!=0)
q.remove(max);
return max;
}
}

1

Reply

Tanya Dalal4 years agoJun 02, 2022 12:07 (GMT +5:30)

Time taken 0.23/1.43:
class Geeks{

static void insert(PriorityQueue<Integer> q, int k)
{
q.add(k);
}

static boolean find(PriorityQueue<Integer> q, int k)
{
return q.contains(k);
}
static int delete(PriorityQueue<Integer> q)
{
return q.poll();
}

}

2

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1110 / 1110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:161

Time Taken0.48

Python3
C++ (17)
Java (21)
Python3
C#

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

import heapq
class Geeks:

# Function to insert element into the priority queue
def insert(self, q, k):
# code here

heapq.heappush(q,-k)  #max heapq
# If k is in q return true else return false
def find(self, q, k):
# code here
if -k in q:
return True
else:
return False

# delete the max element from priority queue
def delete(self, q):
# code here
return -heapq.heappop(q)

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1110 / 1110
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:161

Time Taken0.48

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Operations on PriorityQueue](https://www.geeksforgeeks.org/problems/operations-on-priorityqueue/1)
