# DFS of Graph

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

DFS of Graph
Solved

Difficulty: EasyAccuracy: 63.07%Submissions: 431K+Points: 2Average Time: 5m

Given a connected undirected graph containing V vertices represented by a 2-d adjacency list adj[][], where each adj[i] represents the list of vertices connected to vertex i. Perform a Depth First Search (DFS) traversal starting from vertex 0, visiting vertices from left to right as per the given adjacency list, and return a list containing the DFS traversal of the graph.

Note: Do traverse in the same order as they are in the given adjacency list.

Examples:

Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]

Output: [0, 2, 4, 3, 1]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 2 (the first neighbor of 0) → Output: 0, 2
Visit 4 (the first neighbor of 2) → Output: 0, 2, 4
Backtrack to 2, then backtrack to 0, and visit 3 → Output: 0, 2, 4, 3
Finally, backtrack to 0 and visit 1 → Final Output: 0, 2, 4, 3, 1

Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]

Output: [0, 1, 2, 3, 4]
Explanation: Starting from 0, the DFS traversal proceeds as follows:
Visit 0 → Output: 0
Visit 1 (the first neighbor of 0) → Output: 0, 1
Visit 2 (the first neighbor of 1) → Output: 0, 1, 2
Visit 3 (the first neighbor of 2) → Output: 0, 1, 2, 3
Backtrack to 2 and visit 4 → Final Output: 0, 1, 2, 3, 4

Constraints:
1 ≤ V = adj.size() ≤ 104
0 ≤ adj[i][j] ≤ 104

Expected Complexities

Time Complexity: O(V + E)
Auxiliary Space: O(V + E)

Company Tags

AccoliteAmazonSamsungIntuit

Topic Tags

DFSGraph

Related Articles

Depth First Search Or Dfs For A Graph

Discussions ( 657 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Anonymous_Geek1 day agoSep 24, 2026 02:35 (GMT +5:30)

class Solution {
private:
int dfs(int node, vector<vector<int>>& adj, vector<int>&vis,
vector<int>& ans ) {
vis[node] = 1;
ans.push_back(node);
for(auto it : adj[node]){
if(!vis[it]){
dfs(it, adj, vis,ans);
}
}
}

public:
vector<int> dfs(vector<vector<int>>& adj) {
// Code here
int v = adj.size();
vector<int>vis(v, 0);
vector<int>ans;
int st = 0;

dfs(st, adj, vis, ans);

return ans;
}
};

0

Reply

Jahir Rahaman2 days agoSep 22, 2026 21:59 (GMT +5:30)

class Solution {
public:
void fun(vector<vector<int>>& adj,int node,vector<int>& res,vector<bool>& vin){
res.push_back(node);
vin[node]=true;
for(int i=0;i<adj[node].size();i++)
{
int neigh=adj[node][i];
if(vin[neigh]==false)
{
fun(adj,neigh,res,vin);
}
}
return;
}
vector<int> dfs(vector<vector<int>>& adj) {
// Code here
int n=adj.size();
vector<int>res;
vector<bool>vin(n,0);
fun(adj,0,res,vin);
return res;
}
};

0

Reply

Ronak Mulani4 weeks agoAug 26, 2026 10:52 (GMT +5:30)

class Solution {

void findDFS(int node, ArrayList<ArrayList<Integer>> adj,boolean[] visited,ArrayList<Integer> ans){
ans.add(node);
visited[node] = true;
for(int i=0;i<adj.get(node).size();i++){
if(!visited[adj.get(node).get(i)]){
findDFS(adj.get(node).get(i),adj,visited,ans);
}
}
}

public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
// code here
ArrayList<Integer> ans = new ArrayList<>();
int size = adj.size();
boolean[] visited = new boolean[size];
findDFS(0,adj,visited,ans);
return ans;
}
}

//TC : O(V + E)
//SC : O(V)

0

Reply

Adada Surya Kumari1 month agoAug 22, 2026 23:01 (GMT +5:30)

# class Solution:
#     def dfs(self, adj):
#         # n=size
#         n=len(adj);
#         vis=[False]*n;
#         ans=[]
#         stack=[0]
#         while stack:
#             node=stack.pop()
#             if vis[node]:
#                 continue
#             vis[node]=True
#             ans.append(node);
#             for nei in adj[node]:
#                 if not vis[nei]:
#                     stack.append(nei)
#         return ans

# Input: adj[][] = [[2, 3, 1], [0], [0, 4], [0], [2]]
# for this the o/p is 0 1 3 2 4 (its also one of the dfs traversal)

# Input: adj[][] = [[1, 2], [0, 2], [0, 1, 3, 4], [2], [2]]
# for this the o/p is 0 2 4 3 1 (its also one of the dfs traversal)

# But, in que
# Note: Do traverse in the same order as they are in the given adjacency list.

# so take reverse order of stack. follow below code.

class Solution:
def dfs(self, adj):
# n=size
n=len(adj);
vis=[False]*n;
ans=[]
stack=[0]
while stack:
node=stack.pop()
if vis[node]:
continue
vis[node]=True
ans.append(node);
for i in range(len(adj[node])-1,-1,-1):
nei=adj[node][i]
if not vis[nei]:
stack.append(nei)
return ans

0

Reply

Mahak Kushwaha1 month agoAug 01, 2026 16:54 (GMT +5:30)

class Solution {
ArrayList<Integer> res = new ArrayList<>();
ArrayList<ArrayList<Integer>> adjacencyList = new ArrayList<>();

public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
// code here
int vertices = adj.size();
boolean[] visited = new boolean[vertices];

this.res = new ArrayList<>();
this.adjacencyList = adj;

DFS(0, visited);
return res;
}

private void DFS(int node, boolean[] visited) {
visited[node] = true;
res.add(node);

for (int neighbor : adjacencyList.get(node)) {
if (!visited[neighbor]) {
DFS(neighbor, visited);
}
}
}
}

0

Reply

BODDU NEHRU2 months agoJul 23, 2026 12:15 (GMT +5:30)

class Solution {
public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
// code here
int V = adj.size();
boolean[] visited = new boolean[V];
ArrayList<Integer> result = new ArrayList<>();
dfsHelper(0, adj, visited, result);
return result;
}
public void dfsHelper(int node, ArrayList<ArrayList<Integer>> adj,
boolean[] visited, ArrayList<Integer> result) {

visited[node] = true;
result.add(node);

for (int neighbor : adj.get(node)) {
if (!visited[neighbor]) {
dfsHelper(neighbor, adj, visited, result);
}
}
}
}

2

Reply

Himanshu Sharma2 months agoJul 02, 2026 21:48 (GMT +5:30)

class Solution {
void dfs(ArrayList<ArrayList<Integer>> adj, ArrayList<Integer> ans, int[] visited, int node) {
visited[node] = 1;
ans.add(node);
for (int nbn: adj.get(node)) {
if (visited[nbn] != 1) {
dfs(adj, ans, visited, nbn);
}
}
}
public ArrayList<Integer> dfs(ArrayList<ArrayList<Integer>> adj) {
// code here
int n = adj.size();
ArrayList<Integer> ans = new ArrayList<>();
int visited[] = new int[n];
for (int i = 0; i < n; i++) {
if (visited[i] != 1) {
dfs(adj, ans, visited, i);
}
}
return ans;
}
}

0

Reply

Sai Surekha Pulagam2 months agoJul 01, 2026 07:44 (GMT +5:30)

class Solution:
def bfs(self, adj):
# code here

visited=[False]*len(adj)
result=[]
q=deque([0])
visited[0]=True
while q:
node=q.popleft()
result.append(node)
for n in adj[node]:
if not visited[n]:
visited[n]=True
q.append(n)
return result

0

Reply

Anonymous_Geek3 months agoJun 22, 2026 14:53 (GMT +5:30)

@mohit yadav11

1

Reply

Pulkit Gupta4 months agoMay 14, 2026 19:15 (GMT +5:30)

class Solution {
public:
void check(vector<vector<int>>& adj,vector<int>&ans,int index,vector<bool>&visited){
//   if(visited[index]){
//       return;
//   }
//   visited[index]=true;
ans.push_back(index);
for(auto c:adj[index]){
if(!visited[c]){
visited[c]=true;
check(adj,ans,c,visited);
}
}

}
vector<int> dfs(vector<vector<int>>& adj) {
// Code here
int n=adj.size();
vector<int>ans;
vector<bool>visited(n,false);

visited[0]=true;
check(adj,ans,0,visited);

return ans;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:239

Time Taken0.06

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

class Solution:
def dfs(self, adj):
# code here
n=len(adj)
vis=[0]*n
res=[]
#node is current node from n
def dfs1(node):
vis[node]=1
res.append(node)

for i in adj[node]:
if vis[i]==0:
dfs1(i)
dfs1(0)
return res

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1120 / 1120
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 2 / 2Your Total Score:239

Time Taken0.06

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[DFS of Graph](https://www.geeksforgeeks.org/problems/depth-first-traversal-for-a-graph/1)
