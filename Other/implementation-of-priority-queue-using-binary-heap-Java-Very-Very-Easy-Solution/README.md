# Java Very Very Easy Solution

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

Discussions ( 39 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Prem Kumar7 months agoJan 15, 2026 15:08 (GMT +5:30)

// User function Template for Java

//  public static int H[]=new int[10009];
//  public static int s=-1;
// 1. parent(i): Function to return the parent node of node i
// 2. leftChild(i): Function to return index of the left child of node i
// 3. rightChild(i): Function to return index of the right child of node i
// 4. shiftUp(int i): Function to shift up the node in order to maintain the
// heap property
// 5. shiftDown(int i): Function to shift down the node in order to maintain the
// heap property.
// int s=-1, current index value of the array H[].

// You have to make a class of GFG to access the above functionalities like this - GFG
// obj=new GFG(); You can check the driver code for better understanding.
class Solution {

public int extractMax() {
// your code here
GFG obj = new GFG();
int m = obj.H[0];
int replacable = obj.s;
obj.H[0] = obj.H[replacable];
obj.s = obj.s-1;
obj.shiftDown(0);
return m;

}
};

0

Reply

Anonymous_Geek8 months agoDec 29, 2025 00:49 (GMT +5:30)

So bad Explaination for functions templates.

3

Reply

priyal   gupta10 months agoOct 16, 2025 10:17 (GMT +5:30)

GFG obj=new GFG();
int maxi=obj.H[0];     //Get the top-most element or max-elememt
obj.H[0]=obj.H[obj.s]; //The rest is deletion process of max-heap
obj.s--;
obj.shiftDown(0);
return maxi;

0

Reply

Mohammed Yaseen1 year agoSep 06, 2025 14:44 (GMT +5:30)

Whoever wrote the driver code is a clown

0

Reply

Mr Ahtasham ul haq1 year agoSep 04, 2025 21:41 (GMT +5:30)

Please fix python driver code, array  H  isn't any atribute of object

0

Reply

krishhh16(Edited)26/06/2025, 19:23
1 year agoJun 26, 2025 19:23 (GMT +5:30)

who wrote the driver code comments for python :clown:

4

Reply

Raja Kunal Pandit1 year agoApr 27, 2025 20:21 (GMT +5:30)

Easy C++ Sol :

class Solution {
public:
int extractMax() {
// your code here
swap(H[0],H[s]);
s--;
shiftDown(0);
return H[s+1];
}
};

0

Reply

Gunaganti Revan Kumar1 year agoApr 02, 2025 18:13 (GMT +5:30)

Java Very Very Easy Solution
class Solution {
public int extractMax() {
GFG obj=new GFG();
int largest=obj.H[0];
obj.H[0]=obj.H[obj.s];
obj.s--;
obj.shiftDown(0);
return largest;
}
};

2

Reply

Parinika Kath1 year agoFeb 27, 2025 23:37 (GMT +5:30)

🚀EASY C++ SOLN:- (ACCEPTED) 🚀

class Solution {
public:
int extractMax() {
//max heap so root is the max element
int largest=H[0];
H[0]=H[s];
s--;
shiftDown(0);//chk for correct pos in heap
return largest;
}
};

✅ CONSIDER UPVOTING IF U LIKE :)

6

Reply

Daniel Reich1 year agoFeb 13, 2025 20:46 (GMT +5:30)

This question is severely underspecified and would greatly benefit from more detail.

33

Reply

Akash gite1 year agoJan 01, 2025 23:39 (GMT +5:30)

simple solution in cpp

// steps store the max element is maxi

// swap heap root node with last node

// decrease the size so its will no more pointing the

last swaped node

// called the given shiftDown(0) function for sending the root node to its correct position and making the max heap structure back since in max heap the max element is always in root postion since we replaced with the last smallest element so we have to comapared it with its child left and right node and if they are bigger then him we swap it one of them unit the its child node become smaller then him shiftDown did this for us it takes node index in out case its 0 so we just give him index 0 and it will modify the heap for us

// return the maxi element

// upvotes if like the explanation .............!

int extractMax() {
// your code here

// her 0th element is largest since it a max heap
int maxi = H[0]; // storing the arr[0] element as max since the root node start from 0th element

// replace the root node with last node which pointed by size or s
swap(H[0] , H[s]);

// decrease the size so size is no more pointing the last element
s--;
// correct the strucuture of the heap by sending the root node to its correct position
shiftDown(0); // takes the position of node and insert the node to its correct position

// returning the maximun element form the heap
return maxi;
}

6

Reply

Kartek Jadhav1 year agoNov 18, 2024 17:35 (GMT +5:30)

For python the driver code doesnt include H array. @GeeksforGeeks please fix this.

6

Reply

Pitabash Behera1 year agoOct 30, 2024 09:02 (GMT +5:30)

JAVA

GFG obj=new GFG();
int maxi=obj.H[0];     //Get the top-most element or max-elememt
obj.H[0]=obj.H[obj.s]; //The rest is deletion process of max-heap
obj.s--;
obj.shiftDown(0);
return maxi;

0

Reply

Ritesh Kumar(Edited)27/10/2024, 23:46
1 year agoOct 27, 2024 23:45 (GMT +5:30)

in cpp

int extractMax() {
//   0th index element is the maximum in the heap H,so extract H[0]
int maxi = H[0];

// cout<<"s:"<<s<<endl;

// after extracting max element, last one will occupy first place
// and decrease size by one
swap(H[0], H[s]);
s--;

// Now we will try to make heap valid again by sending thye 0th index element to its correct position
shiftDown(0);

return maxi;
}

0

Reply

JAGANNATH NAYAK1 year agoOct 03, 2024 08:58 (GMT +5:30)

JAVA

class Solution {

public int extractMax() {
// your code here
GFG gfg=new GFG();
int maxi=gfg.H[0];
gfg.H[0]=gfg.H[gfg.s];
gfg.s--;
gfg.shiftDown(0);
return maxi;
}
};

0

Reply

Upputuri Harsha vardhan2 years agoAug 08, 2024 21:20 (GMT +5:30)

Hint:

we need to get max element from priorityqueue so we store the max in some variable .where the max in priorityqueue is root of tree. then we update the 1st ele (max) with last ele in tree .and decrease size ,shiftdown the 1st ele

1

Reply

PREMVED DHOTE2 years agoJul 14, 2024 20:26 (GMT +5:30)

CPP

int x = H[0];
swap(H[0],H[s--]);
shiftDown(0);
return x;

2

Reply

ramu2 years agoJul 10, 2024 20:14 (GMT +5:30)

note : s is the current element index which is being inserted into the heap it means that it the the last elments index since H size is declared as 1009 but only few spaces are filled by the elements and rest have some garbage value so the best technique is that

: take the H[0] top element of the heap and swap it with the last element which is at the index s and then decrese that last element index so index is gone hence the value is removed from the heap and H array

but before returning we should check that if the last element is swapped with the top so i need to fix the heap property again to ensure that the element at the top is always be greater than the rest of all so i need to shiftDown the top element now which is the last element of the heap what this function does is that swap the parent element the index having the maximum element by comparing its childs

code :

class Solution {
public:
int extractMax() {
// your code here
int top = H[0];
swap(H[0],H[s--]);
shiftDown(0);
return top;

}
};

3

Reply
(Show 1 Replies)

Abhimanyu2 years agoJul 04, 2024 15:06 (GMT +5:30)

class Solution {
public:
int extractMax() {
int res = H[0];
H[0]=H[s];
s--;
shiftDown(0);
return res;
}
};

1

Reply

Chopade Ketan Suresh2 years agoJun 29, 2024 14:09 (GMT +5:30)

int extractMax() {
// your code here
int maxi = H[0];

// cout<<"s:"<<s<<endl;

// after extracting max element, last one will occupy first place
// and decrease size by one
swap(H[0], H[s]);
s--;

// Now we will try to make heap valid again
shiftDown(0);

return maxi;
}

3

Reply

Akshay yadav2 years agoJun 25, 2024 06:44 (GMT +5:30)

class Solution {
public:
int extractMax() {
// your code here
int r=H[0];
H[0]=H[s];
s--;
int i=0;
while(i<s)
{
shiftDown( i);
i++;
}
return r;
}

};

0

Reply

Pranjal Dhar Dwivedi2 years agoJun 24, 2024 11:08 (GMT +5:30)

Simple C++ solution using given functions-

int extractMax() {
// your code here
int ans = H[0];
H[0]=H[s];
s--;
shiftDown(0);
return ans;
}

0

Reply

Ritik Koshta2 years agoJun 05, 2024 17:50 (GMT +5:30)

JAVA CODE

class Solution {
public int extractMax() {
GFG obj=new GFG();
int xx= obj.H[0];
obj.H[0]=obj.H[obj.s];
obj.s--;
obj.shiftDown(0);
return xx;
}
};

1

Reply

Aatish Jain2 years agoMay 22, 2024 14:01 (GMT +5:30)

// For Python

class Solution:
def extractMax(self):
# Code here
global s
ans = H[0]
H[0] = H[s]
s -= 1
shiftDown(0)
return ans

4

Reply

Isha2 years agoMay 21, 2024 17:51 (GMT +5:30)

// Just in 5 Lines
class Solution {
public:
int extractMax() {
int x = H[0];
swap(H[0], H[s]);
s--;
shiftDown(0);
return x;
}
};

2

Reply

Benny Sweetson2 years agoNov 21, 2023 19:12 (GMT +5:30)

public int extractMax() {

// The array GFG.H contains the element. We can access directly from here. (GFG in driver code)
// The int GFG.s is the current index or last index value of the array GFG.H

// System.out.printf("GFG.s: %d\n", GFG.s);
// System.out.println(Arrays.toString(GFG.H));

// And the GFG class implemented with PriorityQueue with Binary Max Heap and some helper methods for Binary Heap

// Todo: Fetch the max element from that and satisfies the Binary Max Heap

// The top element of Binary Max Heap holds the max element
// Polling will remove the top element

// Steps to poll and element from Binary Max Heap
// # Swap the top element and last element (first index 0 and last index)
// # Remove the last element after backup. Because this is the element we should return
// # Sink swapped top element to satisfies the Binary Map Heap invarients

// # Swap the top element and last element (first index 0 and last index)
int temp = GFG.H[0];
GFG.H[0] = GFG.H[GFG.s];
GFG.H[GFG.s] = temp;

// # Remove the last element after backup. Because this is the element we should return
int maxEl = GFG.H[GFG.s];
GFG.H[GFG.s] = 0;
GFG.s--;

// # Sink swapped top element to satisfies the Binary Max Heap invarients
// Sink when array has elements
if (GFG.s >= 0)
new GFG().shiftDown(0);

return maxEl;
}

0

Reply

Teja Jasti2 years agoNov 08, 2023 22:24 (GMT +5:30)

Understanding this problem is harder than writing the solution.

35

Reply
(Show 1 Replies)

Saurabh Pandey2 years agoOct 01, 2023 13:22 (GMT +5:30)

C++ ✅ Easy Understanding ✅ Best Optimized | Beats 100 % Log(n) Solution

int extractMax() {

int ans = H[0];
H[0] = H[s]; // Because 0 based, example if 1 element present size is 0, 2 element present size is 1.
s--;

int i = 0;
while(i <= s)
{
int currentMax = i; // Current Value Stored;

int l = 2 * i + 1;
/// Check Krlo Left kya bada hai currentMax se;
if(l <= s && H[l] > H[currentMax])
{
currentMax = l;
}

int r = 2 * i + 2;
// Ab Dekh Lo Agar r, currentMax se b bda hai to update krdo;
if(r <= s && H[r] > H[currentMax])
{
currentMax = r;
}

// Now We Have Our Max Child If Present;
// agar i == currentMax mtlb koi bada ni nikla to simply break kr jao kyoki yhi tmhra parent hai which is greatest of all its child;
// else swap krdo abi k parent ko maximum wle child se; which is stored in currentMax;
if(i != currentMax)
{
swap(H[i], H[currentMax]);
i = currentMax;
}
else break;
}

return ans;
}

// Time Complexity Be 2 * i everytime so I would say Log(n);
// Sc -> O(1) We Have Not Used any Extra Space;

3

Reply
(Show 1 Replies)

Rushikesh Vaishnav3 years agoJul 29, 2023 23:39 (GMT +5:30)

// CPP solution

int extractMax() {

int res=H[0];

H[0]=H[s];
s--;

int i=0;

while(i<=s)
{
int lid=2*i + 1;
int rid=2*i + 2;

if(H[lid]>=H[rid])
{
if(H[lid]>H[i])
{
swap(H[lid],H[i]);
i=lid;
}
else
{
break;
}
}
else
{
if(H[rid]>H[i])
{
swap(H[rid],H[i]);
i=rid;
}
else
{
break;
}
}
}
return res;
}

1

Reply

Lakshya3 years agoJul 14, 2023 19:40 (GMT +5:30)

Had there not been an option to look at the driver code I wouldn't be able to solve this question even with a gun to my head.

13

Reply

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed120 / 120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:163

Time Taken0.18

Python3
C++ (17)
Java (21)
Python3

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

# 1. parent(i): Function to return the parent node of node i
# 2. leftChild(i): Function to return index of the left child of node i
# 3. rightChild(i): Function to return index of the right child of node i
# 4. shiftUp(int i): Function to shift up the node in order to maintain the
# heap property
# 5. shiftDown(int i): Function to shift down the node in order to maintain the
# heap property.
# int s=-1, current index value of the array H[].

class Solution:
def extractMax(self):
# Code here
global s
ans = H[0]
H[0] = H[s]
s -= 1
shiftDown(0)
return ans

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed120 / 120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:163

Time Taken0.18

Custom Input

## Problem Link

[Java Very Very Easy Solution](https://www.geeksforgeeks.org/problems/implementation-of-priority-queue-using-binary-heap/1)
