// class Solution {
// public:
//     vector<vector<int>> threeSum(vector<int>& nums) {
//         int n= nums.size();
//         sort(nums.begin(),nums.end());
//         set<vector<int>> set;
//         vector<vector<int>>output;
//         for(int i=0;i<n-2;i++){
//             for(int j=i+1;j<n-1;j++){
//                 for(int k=j+1;k<n;k++){
//                     if(nums[i]+nums[j]+nums[k]==0 && i!=j&& j!=k && k!=i){
//                         set.insert({nums[i],nums[j],nums[k]});
//                     }
//                 }
//             }
//         }
//         for(auto it: set){
//             output.push_back(it);
//         }
//         return output;
  
//     }
// };

class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        int n = nums.size();
        vector<vector<int>>res;
        sort(nums.begin(),nums.end());
        for(int i=0;i<n-2;i++){
            if(i>0 && nums[i]==nums[i-1]) continue;

            int left=i+1, right=n-1;
            while(left < right){
                int s= nums[i]+nums[left]+nums[right];
                if(s==0){
                    res.push_back({nums[i], nums[left], nums[right]});

                    while(left < right && nums[left]==nums[left+1]) left++;
                    while(left < right && nums[right] == nums[right-1]) right--;

                    left++;
                    right--;
                }
                else if(s>0){
                    right--;
                }
                else{
                    left++;
                }
            }
        }
        return res;
       
    }
};