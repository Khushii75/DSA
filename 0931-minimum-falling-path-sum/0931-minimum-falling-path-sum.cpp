class Solution {
public:
    int minFallingPathSum(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        vector<vector<int>>dp(m, vector<int>(n));
           for(int j=0; j<n; j++){
                dp[0][j]=matrix[0][j];
            }
        for(int i=1; i<m; i++){
            for(int j=0; j<n; j++){
                int left= INT_MAX;
                int right= INT_MAX;
                int up= INT_MAX;
                left= (j>0) ? dp[i-1][j-1]:INT_MAX;
                right= (j<n-1)? dp[i-1][j+1]:INT_MAX;
                up= dp[i-1][j]; 
            
            dp[i][j]= matrix[i][j] + min(left, min(right,up));
            }
        }
        int ans=INT_MAX;
        for(int i=0; i<n; i++){
            ans= min(ans, dp[m-1][i]);
        }
        return ans;
    }
};