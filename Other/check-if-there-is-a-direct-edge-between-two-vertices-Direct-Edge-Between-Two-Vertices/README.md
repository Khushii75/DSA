# Direct Edge Between Two Vertices

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

Discussions ( 5 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ravikant Kumar7 months agoFeb 13, 2026 08:58 (GMT +5:30)

class Solution {
public:
bool checkEdge(vector<vector<int>>& adj, int u, int v)
{
queue<int>q;
q.push(u);
int neighbour = q.front();
q.pop();
for(int i=0;i<adj[neighbour].size();i++)
{
q.push(adj[neighbour][i]);
}

while(!q.empty())
{
if(q.front()==v) return 1;
q.pop();

}
return 0;
}
};

0

Reply

Shubham Vishwakarma8 months agoFeb 02, 2026 20:04 (GMT +5:30)

class Solution {
public boolean checkEdge(ArrayList<ArrayList<Integer>> adj, int u, int v) {
//   code here
return adj.get(u).contains(v);
}
}

0

Reply

MOHITH NAIDU SANAPATI9 months agoDec 25, 2025 15:26 (GMT +5:30)

class Solution {
public:
int checkEdge(vector<vector<int>>& adj, int u, int v) {
for(auto it:adj[u]){
if(it==v){
return 1;
}
}
return 0;
}
};

0

Reply

Alok Jain11 months agoNov 01, 2025 22:32 (GMT +5:30)

class Solution {
public:
int checkEdge(vector<vector<int>>& adj, int u, int v) {

for(auto node: adj[u]){
if(node==v) return true;
}
return false;
}
};

0

Reply

Varuni Desai11 months agoOct 28, 2025 17:05 (GMT +5:30)

int checkEdge(vector<vector<int>>& adj, int u, int v) {
// code here
int i,j;
for(i=0;i<adj[u].size();i++)
{
if(adj[u][i] == v)
return 1;
}
return 0;

}

0

Reply

No more comments to load

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:262

Time Taken0.07

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
14
15
16
17
18
19
20
21
22

class Solution {
public:
bool checkEdge(vector<vector<int>>& adj, int u, int v)
{
queue<int>q;
q.push(u);
int neighbour = q.front();
q.pop();
for(int i=0;i<adj[neighbour].size();i++)
{
q.push(adj[neighbour][i]);
}

while(!q.empty())
{
if(q.front()==v) return 1;
q.pop();

}
return 0;
}
};

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 1 / 1Your Total Score:262

Time Taken0.07

Custom Input

## Problem Link

[Direct Edge Between Two Vertices](https://www.geeksforgeeks.org/problems/check-if-there-is-a-direct-edge-between-two-vertices/1)
