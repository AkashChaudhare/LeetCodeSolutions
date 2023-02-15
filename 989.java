class Solution {
    public List<Integer> addToArrayForm(int[] A, int curr) {
        int N = A.length-1;
       
        List<Integer> ans = new ArrayList();

        while(N>=0 || curr>0){
            if (N>=0)curr+=A[N];
            ans.add(curr%10);
            curr/=10;
            N--;
        }


        Collections.reverse(ans);
        return ans;
    }
}
