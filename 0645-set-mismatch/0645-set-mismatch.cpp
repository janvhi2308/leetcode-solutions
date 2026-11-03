class Solution {
public:
    vector<int> findErrorNums(vector<int>& nums) {
        int n= nums.size();
        vector<int>ans(2);
        unordered_map<int,int> mp;
        for(int i=0;i<n;i++){
            mp[nums[i]]++;
        }
        for(int i=0;i<n;i++){
            if(mp[nums[i]]==2){
                ans[0]=nums[i];
            }
        }
        for(int i=0;i<=n;i++){
            if(mp.find(i)==mp.end()){
                ans[1]=i;
            }
        }
        return ans;
        
    }
};