class Solution {
    public int[] shuffle(int[] nums, int n) {
        int x=0,y=n,idx=0;
        int[] ans=new int[2*n];
        while(x<n){
            ans[idx]=nums[x];
            ans[idx+1]=nums[y];
            x+=1;
            y+=1;
            idx+=2;
        }
        return ans;
    }
}
