# Directed Graph Cycle

## Problem

CoursesSale

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

Directed Graph Cycle
Solved

Difficulty: MediumAccuracy: 27.88%Submissions: 618K+Points: 4

Given a directed graph with V vertices numbered from 0 to V - 1 and E directed edges. The graph is represented using a 2D array edges[][] of size E, where each entry edges[i] = [u, v] denotes a directed edge from vertex u to vertex v.

Check whether the graph contains any cycle. Return true if there exists at least one cycle in the graph; otherwise, return false.

Examples:

Input: V = 4, edges[][] = [[0, 1], [1, 2], [2, 0], [2, 3]]

Output: true
Explanation: The diagram clearly shows a cycle 0 -> 1 -> 2 -> 0

Input: V = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]

Output: false
Explanation: no cycle in the graph

Constraints:
1 ≤ V ≤ 105
0 ≤ E ≤ 105
0 ≤ edges[i][0], edges[i][1] < V

Expected Complexities

Time Complexity: O(V + E)
Auxiliary Space: O(V + E)

Company Tags

FlipkartAmazonMicrosoftSamsungMakeMyTripOracleGoldman SachsAdobeBankBazaarRockstandNPCI

Topic Tags

Graph

Related Interview Experiences

Makemytrip Interview Experience Set 13 On Campus For Full TimeSamsung R D Noida Interview Experience On CampusSamsung Interview Experience On Campus For Software Engineer September 2018

Related Articles

Detect Cycle In A Graph

Discussions ( 614 Threads )

Commenting as Khushi KumariComment Anonymously

💡Discussion Guidelines
Please avoid posting complete solutions or full code in the comments.
Ask questions, share hints, discuss approaches, or report any issues. Let's help everyone learn together.

Ronak Mulani1 month agoAug 26, 2026 19:03 (GMT +5:30)

//BFS (Kahn's algorithm approach)
class Solution {
public boolean isCyclic(int V, int[][] edges) {
// code here
int count = 0;
ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
Queue<Integer> q = new LinkedList<>();
int[] inDegree = new int[V];
Arrays.fill(inDegree,0);
for(int i=0;i<V;i++){
adj.add(new ArrayList<>());
}
for(int i=0;i<edges.length;i++){
int u = edges[i][0];
int v = edges[i][1];
adj.get(u).add(v);
//Calculating the inDegree
inDegree[v]++;
}
for(int i=0;i<V;i++){
if(inDegree[i]==0){
//Include all node in Queue whose inDegree is 0
q.offer(i);
//increse count when inDegree of node is 0
count++;
}
}
while(!q.isEmpty()){
int node = q.poll();
for(int j=0;j<adj.get(node).size();j++){
//we are decresing indegree by 1 when adjaenct node pop out from Queue
inDegree[adj.get(node).get(j)]--;
if(inDegree[adj.get(node).get(j)]==0){
q.offer(adj.get(node).get(j));
//increse count when inDegree of node is 0
count++;
}
}
}
//If cycle presenr then count!=V (means inDegree = 0 is not for all nodes after traversal)
if(count!=V){
return true;
}
return false;
}
}

0

Reply

Ronak Mulani1 month agoAug 26, 2026 18:30 (GMT +5:30)

class Solution {

boolean detectCycle(int node, ArrayList<ArrayList<Integer>> adj,boolean[] visited, boolean[] path){
visited[node] = true;
path[node] = true;
for(int j=0;j<adj.get(node).size();j++){
//if that node in path is already visited then cycle is present
if(path[adj.get(node).get(j)]){
return true;
}
//if node is not visited then go further and do recursive call
if(!visited[adj.get(node).get(j)]){
if(detectCycle(adj.get(node).get(j),adj,visited,path)){
return true;
}
}
}
//make node of path again 0, kind of backtraking bvz cycle not detected then reverse back
path[node] = false;
return false;
}

public boolean isCyclic(int V, int[][] edges) {
// code here
ArrayList<ArrayList<Integer>> adj = new ArrayList<>();
boolean[] visited = new boolean[V];
boolean[] path = new boolean[V];
for(int i=0;i<V;i++){
adj.add(new ArrayList<>());
}
for(int i=0;i<edges.length;i++){
int u = edges[i][0];
int v = edges[i][1];
adj.get(u).add(v);
}
for(int i=0;i<V;i++){
if(detectCycle(i,adj,visited,path)){
return true;
}
}
return false;
}
}

0

Reply

Izan Ahmad1 month agoAug 16, 2026 19:33 (GMT +5:30)

bool isCyclic(int V, vector<vector<int>> &edges) {
vector<int>indegree(V,0);
queue<int>q;
int count = 0;
unordered_map<int,vector<int>>adj;
for(auto &edge: edges){
int u = edge[0];
int v = edge[1];
adj[u].push_back(v);
}
for(int u = 0; u < V; u++){
for(int &v : adj[u]){
indegree[v]++;
}
}
for(int i = 0; i < V; i++){
if(indegree[i] == 0){
q.push(i);
}
}
while(!q.empty()){
int u = q.front();
q.pop();
count++;
for(int &v: adj[u]){
indegree[v]--;
if(indegree[v] == 0){
q.push(v);
}
}
}
return count != V;
}

1

Reply

NV Yashwanth1 month agoAug 14, 2026 14:38 (GMT +5:30)

is people clearly affected in their brian they have specified dont put solution in discussion tab why are they putting the solution here

2

Reply

Rahul Aligeti2 months agoJul 15, 2026 16:45 (GMT +5:30)

class Solution {
public boolean isCyclic(int V, int[][] edges) {
// code here
ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

for(int i=0;i<V;i++){
adj.add(new ArrayList<>());
}

for(int[] e:edges){
int a = e[0];
int b = e[1];
adj.get(a).add(b);
//adj.get(b).add(a);
}
boolean[] vis = new boolean[V];
boolean[] path = new boolean[V];
for(int i=0;i<V;i++){
if(!vis[i]){
if(dfs(i,adj,vis,path)){
return true;
}
}
}
return false;
}
boolean dfs(int src,ArrayList<ArrayList<Integer>> adj,boolean[] vis,boolean[] path){
vis[src] = true;
path[src] = true;
for(Integer i:adj.get(src)){
if(!vis[i]){
if(dfs(i,adj,vis,path)) return true;
}else if(path[i]){
return true;
}
}
path[src] = false;
return false;
}
}

0

Reply

Ritesh Kumar2 months agoJul 15, 2026 10:06 (GMT +5:30)

class Solution {
public:
bool isCyclic(int V, vector<vector<int>> &edges) {

// by using topo sort

vector<int>indegree(V , 0) ;

queue<int>Q ;

vector<int>ans ;

vector<vector<int>>adj(V) ;

for(int i=0 ; i < edges.size() ; i++){
int a = edges[i][0] ;
int b = edges[i][1] ;

adj[a].push_back(b) ;

}

for(int i=0 ; i < V ; i++){
for(int x : adj[i]){
indegree[x]++ ;
}
}

for(int i=0 ; i < V ; i++){
if(indegree[i] == 0){
Q.push(i) ;
}
}

while(!Q.empty()){
int f = Q.front() ;
Q.pop() ;

ans.push_back(f) ;

for(int x : adj[f]){
indegree[x]-- ;

if(indegree[x] == 0){
Q.push(x) ;
}
}
}

return ans.size() == V ? false : true  ;

}
};

0

Reply

ashok Sakuru4 months agoMay 25, 2026 00:16 (GMT +5:30)

class Solution {
public:
bool isCyclic(int V, vector<vector<int>> &edges) {
vector<vector<int>>adj(V);
vector<int>indegree(V);
queue<int>q;
int cnt=0;
for(auto &it:edges){
adj[it[0]].push_back(it[1]);
indegree[it[1]]++;
}
for(int i=0;i<V;i++){
if(indegree[i]==0){
q.push(i);
}
}
while(!q.empty()){
cnt++;
int val=q.front();
q.pop();
for(auto &it:adj[val]){
indegree[it]--;
if(indegree[it]==0){
q.push(it);
}
}
}
return (cnt!=V);
}
};

1

Reply

Vidhi Soni4 months agoMay 17, 2026 14:38 (GMT +5:30)

class Solution {
public:

bool helper(int src, vector<bool>&vis, vector<bool>&rec,vector<vector<int>>&adj){
vis[src]=true;
rec[src]=true;
for(int it:adj[src]){
if(!vis[it]){
if(helper(it,vis,rec,adj)){
return true;
}
}else{
if(rec[it]){
return true;
}
}
}
rec[src]=false;
return false;
}

bool isCyclic(int V, vector<vector<int>> &edges) {
// code here
vector<vector<int>>adj(V);
for(auto&i:edges){
adj[i[0]].push_back(i[1]);//only 0 to 1 not 1 to 0 because of directed
}
vector<bool>vis(V,false);
vector<bool>rec(V,false);

for(int i=0;i<V;i++){
if(!vis[i]){
if(helper(i,vis,rec,adj)){
return true;
}
}
}
return false;
}
};

0

Reply

Chukka komal sai(Edited)16/05/2026, 08:04
4 months agoMay 16, 2026 07:53 (GMT +5:30)

class Solution {
public:
vector<vector<int>>_g ;
vector<int>color ;
bool cycle = false ;
bool isCyclic(int V, vector<vector<int>> &edges) {
_g.resize(V , {}) ;
color.resize(V) ;
for(auto edge : edges){
_g[edge[0]].push_back(edge[1]) ;
}

for(int i = 0 ; i<V ; i++){
if(color[i] == 0)
dfs(i) ;
}
return cycle ;
}

void dfs(int node){
color[node] = 1 ;

for(auto child : _g[node]){
if(color[child] == 0)
dfs(child) ;
else if(color[child] == 1)
cycle = true ;

}
color[node] = 2 ;
}
};

0 indicates white which means edge hasnot yet discovered.

1 indicates grey which means currently its children node is begin explored  indirectly also  indicates parent node is in call stack of dfs.

2 indicates black which means node and its also children  is fully explored.

Condition for cycle

- when going to its children , If its color[child] is grey  then it must have a back edge. how can child be already visited and color is grey(still in call stack) ?
- only possible way is it must be ancestor.
Thus a back edge which indicates cycle

0

Reply

Vinikesh Hiranandani4 months agoMay 12, 2026 23:41 (GMT +5:30)

class Solution:
def dfs(self,current_node,visited,path,adj_list):
visited[current_node]=1
path[current_node]=1
for adj_node in adj_list[current_node]:
if visited[adj_node]==0:
x=self.dfs(adj_node,visited,path,adj_list)
if x==True:
return True
elif path[adj_node]==1:
return True
path[current_node]=0
return False
def isCyclic(self, V, edges):
adj_list = [[] for _ in range(V)]
for u,v in edges:
adj_list[u].append(v)
visited=[0]*V
path=[0]*V
for i in range(0,V):
if visited[i]==0:
ans=self.dfs(i,visited,path,adj_list)
if ans == True:
return True
return False

0

Reply

If you are facing any issue on this page. Please let us know.

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1113 / 1113
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:251

Time Taken2.14

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

class Solution:
def dfs(self,curr_node, vis , path_vis, adj_list ):
vis[curr_node]=1
path_vis[curr_node]=1
for i in adj_list[curr_node]:
if vis[i]==0:
x=self.dfs(i, vis , path_vis, adj_list )

if x==True:
return True
elif path_vis[i]==1:
return True
path_vis[curr_node]=0
return False

def isCyclic(self, V: int, edges: list[list[int]]) -> bool:
# code here
vis=[0]*V
path_vis=[0]*V
adj_list=[[] for _ in range(V)]

for u,v in edges:
adj_list[u].append(v)

for i in range(V):
if vis[i]==0:
ans=self.dfs(i, vis , path_vis, adj_list)
if ans==True:
return True

return False

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

Output Window

Compilation ResultsCustom InputY.O.G.I. (AI Bot)
Problem Solved Successfully
Suggest Feedback

Test Cases Passed1113 / 1113
Attempts : Correct / Total1 / 1Accuracy : 100%

Points Scored 4 / 4Your Total Score:251

Time Taken2.14

Custom Input

If you are facing any issue on this page. Please let us know.

## Problem Link

[Directed Graph Cycle](https://www.geeksforgeeks.org/problems/detect-cycle-in-a-directed-graph/1)
