class Solution {
   public List<List<Integer>> generate(int numRows) {
    List<List<Integer>> lst = new ArrayList<>();
    List<Integer> pre = null;
    for(int i = 0;i<numRows;i++){
        List<Integer> a = new ArrayList<>();
        for(int j=0;j<=i;j++){
            if(j==0||j==i){
                a.add(1);
            }
            else{
                a.add(pre.get(j-1)+pre.get(j));
            }                
        }
        pre = a;
        lst.add(a);
    }        
    return lst;
}
}
