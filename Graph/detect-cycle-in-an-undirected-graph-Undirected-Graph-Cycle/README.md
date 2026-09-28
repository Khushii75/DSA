# Undirected Graph Cycle

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

Undirected Graph Cycle
Solved

Difficulty: MediumAccuracy: 30.13%Submissions: 778K+Points: 4Average Time: 20m

Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

Note: The graph can have multiple component.

Examples:

Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
Output: true
Explanation:

1 -> 2 -> 0 -> 1 is a cycle.

Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
Output: false
Explanation:

No cycle in the graph.

Constraints:
1 ≤ V, E ≤ 105
0 ≤ edges[i][0], edges[i][1] < V

Expected Complexities

Time Complexity: O(V + E)
Auxiliary Space: O(V)

Company Tags

FlipkartAmazonMicrosoftSamsungMakeMyTripOracleAdobe

Topic Tags

DFSGraphunion-find

Related Interview Experiences

Makemytrip Interview Experience Set 13 On Campus For Full Time

Related Articles

Detect Cycle In An Undirected Graph Using BfsDetect Cycle Undirected Graph

Discussions ( 1030 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ronak Mulani1 month agoAug 26, 2026 15:32 (GMT +5:30)

//DFS Approach
class Pair{
int first;
int second;

Pair(int node, int parent){
first = node;
second = parent;
}
}

class Solution {

boolean checkCycle(ArrayList<ArrayList<Integer>> adj, boolean[] visited, int start){
Queue<Pair> q = new LinkedList<>();
visited[start] = true;
q.offer(new Pair(start,-1));
while(!q.isEmpty()){
Pair p = q.poll();
int node = p.first;
int parent = p.second;
for(int j=0;j<adj.get(node).size();j++){
if(adj.get(node).get(j)==parent){
continue;
}
if(visited[adj.get(node).get(j)]){
return true;
}
q.offer(new Pair(adj.get(node).get(j),node));
visited[adj.get(node).get(j)] = true;
}
}
return false;
}

public boolean isCycle(int V, int[][] edges) {
// Code here
boolean[] visited = new boolean[V];
ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
for(int i=0;i<V;i++){
adj.add(new ArrayList<Integer>());
}
for(int i=0;i<edges.length;i++){
int u = edges[i][0];
int v = edges[i][1];
adj.get(u).add(v);
adj.get(v).add(u);
}
for(int i=0;i<V;i++){
if(!visited[i]){
if(checkCycle(adj,visited,i)){
return true;
}
}
}
return false;
}
}

0

Reply

Ronak Mulani(Edited)26/08/2026, 15:31
1 month agoAug 26, 2026 15:31 (GMT +5:30)

//BFS Approach

class Solution {

boolean checkCycle(int node, int parent, ArrayList<ArrayList<Integer>> adj, boolean[] visited) {

visited[node] = true;

for (int j=0;j<adj.get(node).size();j++) {

// Ignore the edge through which we came
if (adj.get(node).get(j) == parent) {
continue;
}

// Already visited -> cycle
if (visited[adj.get(node).get(j)]) {
return true;
}

// DFS
if (checkCycle(adj.get(node).get(j), node, adj, visited)) {
return true;
}
}

return false;
}

public boolean isCycle(int V, int[][] edges) {

boolean[] visited = new boolean[V];

// Create adjacency list
ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

for (int i = 0; i < V; i++) {
adj.add(new ArrayList<>());
}

// Convert edge list -> adjacency list
for (int i=0;i<edges.length;i++) {

int u = edges[i][0];
int v = edges[i][1];

adj.get(u).add(v);
adj.get(v).add(u);
}

// Handle disconnected graph
for (int i = 0; i < V; i++) {

if (!visited[i]) {

if (checkCycle(i, -1, adj, visited)) {
return true;
}
}
}

return false;
}
}

0

Reply

Anonymous_Geek(Edited)11/08/2026, 22:21
1 month agoAug 11, 2026 22:13 (GMT +5:30)

### Raw Intuition:

==> USING BFS

- adj list is required to build first as edges are given
- vis array can be used to mark visited nodes
- going through each vertex if its not visited as there might be connected components. Otherwise if it would have been single graph then we can just start with first vertices and go through its neighbours using bfs
- so while traversing we will encounter a neighbour node which is already visited and is not a parent node for the current node so thats when it will detect as cycle

==> USING DFS

- go through each vertices
- while going through dfs calls there will be a adj node for which we will call the dfs call where that adj node is not parent of curr node and is not parent of node then from that point we will return true and at the end it will be detected as cycle

0

Reply

Rupali Goyal1 month agoAug 11, 2026 11:40 (GMT +5:30)

class Solution {
public:
void dfs(vector<vector<int>> &adj_lst, int node, int parent, bool &cycle, vector<bool> &vis){
vis[node]=1;
for(int i=0; i<adj_lst[node].size(); i++){
int neigh=adj_lst[node][i];
if (vis[neigh]==1 && neigh!=parent){
cycle=true;
return;
}
if (vis[neigh]==0){
dfs(adj_lst, neigh, node, cycle, vis);
}
}
return ;
}
bool isCycle(int V, vector<vector<int>>& edges) {
// Code here
vector<bool> vis(V, 0);
bool cycle=false;
vector<vector<int>> adj_lst(V);
for(int i=0; i<edges.size(); i++){
int src=edges[i][0];
int dest=edges[i][1];
adj_lst[src].push_back(dest);
adj_lst[dest].push_back(src);
}
for(int i=0; i<V; i++){
if (vis[i]==0){
dfs(adj_lst, i, -1, cycle, vis);
if (cycle==true){
return true;
}
}
}
return cycle;
}
};

0

Reply

Aditi Tiwari1 month agoAug 01, 2026 17:39 (GMT +5:30)

class Solution {
public:
bool dfs(int src,int parent,vector<vector<int>>&adj,vector<int>&vis){
vis[src]=1;
int node=src;

for(auto it:adj[node]){
if(!vis[it]){
vis[it]=1;
if(dfs(it,node,adj,vis)){
return true;
}
}
else if(it!=parent){
return true;
}

}

return false;
}

bool isCycle(int V, vector<vector<int>>& edges) {

vector<vector<int>>adj(V);

for(auto it:edges){
int x=it[0];
int y=it[1];
adj[x].push_back(y);
adj[y].push_back(x);
}
vector<int>vis(V,0);

for(int i=0;i<V;i++){
if(!vis[i]){
if(dfs(i,-1,adj,vis)){
return true;
}
}
}
return false;

}
};

by dfs

0

Reply

Aditi Tiwari1 month agoAug 01, 2026 17:28 (GMT +5:30)

class Solution {
public:
bool detect(int src,vector<vector<int>>&adj,vector<int>&vis){
vis[src]=1;
queue<pair<int,int>>q;
q.push({src,-1});
while(!q.empty()){
int node=q.front().first;
int parent=q.front().second;
q.pop();

for(auto it:adj[node]){
if(!vis[it]){
vis[it]=1;
q.push({it,node});
}
else if(it!=parent){
return true;
}

}
}
return false;
}

bool isCycle(int V, vector<vector<int>>& edges) {

vector<vector<int>>adj(V);

for(auto it:edges){
int x=it[0];
int y=it[1];
adj[x].push_back(y);
adj[y].push_back(x);
}
vector<int>vis(V,0);

for(int i=0;i<V;i++){
if(!vis[i]){
if(detect(i,adj,vis)){
return true;
}
}
}
return false;

}
};

1

Reply

Shivam2 months agoJul 29, 2026 18:07 (GMT +5:30)

- DFS

class Solution {
public:
bool dfs(int node,int Parent,vector<vector<int>>&adjList,vector<int>&visited)
{
visited[node]=1;

for(auto it : adjList[node])
{
if(!visited[it])
{
if(dfs(it,node,adjList,visited))
return true;
}
else if(it!=Parent)
{
return true;
}

}
return false;
}
bool isCycle(int V, vector<vector<int>>& edges)
{
vector<vector<int>>adjList(V);
vector<int>visited(V,0);
for(auto &edge : edges)
{
int u=edge[0];
int v=edge[1];

adjList[u].push_back(v);
adjList[v].push_back(u);
}

for(int i=0;i<V;i++)
{
if(!visited[i] && dfs(i,-1,adjList,visited))
return true;
}
return false;
}
};

0

Reply

Shivam2 months agoJul 29, 2026 17:41 (GMT +5:30)

class Solution {
public:
bool bfs(int node,int Parent,vector<vector<int>>&adjList,vector<int>&visited)
{
queue<pair<int,int>>q;
visited[node]=1;
q.push({node,Parent});
while(!q.empty())
{
auto curr=q.front();
q.pop();

int child=curr.first;
int Par=curr.second;

for(auto it : adjList[child])
{
if(!visited[it])
{
visited[it] = 1;
q.push({it, child});
}
else if(it!=Par)
{
return true;
}

}
}
return false;
}
bool isCycle(int V, vector<vector<int>>& edges)
{
vector<vector<int>>adjList(V);
vector<int>visited(V,0);
for(auto &edge : edges)
{
int u=edge[0];
int v=edge[1];

adjList[u].push_back(v);
adjList[v].push_back(u);
}

for(int i=0;i<V;i++)
{
if(!visited[i] && bfs(i,-1,adjList,visited))
return true;
}
return false;
}
};

0

Reply

vijayakumar2 months agoJul 15, 2026 11:04 (GMT +5:30)

class Solution {
bool dfs(vector<int> adj[], int sv, vector<bool>& vis, int parent){
vis[sv] = true;

for(int neighbor: adj[sv]){
if(!vis[neighbor]){
bool ans = dfs(adj, neighbor, vis, sv);
if(ans == true){
return true;
}
}else if(neighbor != parent){
return true;
}
}
return false;
}
public:
bool isCycle(int V, vector<vector<int>>& edges) {
vector<int> adj[V];

for(int i = 0; i < edges.size(); i++){
int u = edges[i][0];
int v = edges[i][1];
adj[u].push_back(v);
adj[v].push_back(u);
}

vector<bool> vis(V, false);

for(int i = 0; i < V; i++){
if(!vis[i]){
bool output = dfs(adj, i, vis, -1);
if(output){
return true;
}
}
}
return false;
}
};

2

Reply

vijayakumar2 months agoJul 15, 2026 11:04 (GMT +5:30)

class Solution {
bool dfs(vector<int> adj[], int sv, vector<bool>& vis, int parent){
vis[sv] = true;

for(int neighbor: adj[sv]){
if(!vis[neighbor]){
bool ans = dfs(adj, neighbor, vis, sv);
if(ans == true){
return true;
}
}else if(neighbor != parent){
return true;
}
}
return false;
}
public:
bool isCycle(int V, vector<vector<int>>& edges) {
vector<int> adj[V];

for(int i = 0; i < edges.size(); i++){
int u = edges[i][0];
int v = edges[i][1];
adj[u].push_back(v);
adj[v].push_back(u);
}

vector<bool> vis(V, false);

for(int i = 0; i < V; i++){
if(!vis[i]){
bool output = dfs(adj, i, vis, -1);
if(output){
return true;
}
}
}
return false;
}
};

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed112 / 112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:247

Time Taken2.33

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
27
28
29
30
31
32
33
34
35

from collections import deque
class Solution:
def isCycle(self, V, edges):
#Code here
adj_list=[[] for _ in range(V)]
for u,v in edges:
adj_list[u].append(v)
adj_list[v].append(u)
vis=[0]*V
for i in range(V):
if vis[i]==1:
continue
#not visited store node, parent into queue
q=deque()
q.append((i,-1))
vis[i]=1
while q:
node, parent=q.popleft()
#check for adj_List
for i in adj_list[node]:
if vis[i]==0:
vis[i]=1
q.append((i,node))
else:
if i!=parent:
return True
return False

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed112 / 112
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:247

Time Taken2.33

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Undirected Graph Cycle](https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1)
