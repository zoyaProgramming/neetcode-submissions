class Solution {
    public int[] productExceptSelf(int[] nums) {
        int[] prefixProducts = new int[nums.length];
        prefixProducts[0] = 1;
        int[] suffixProducts = new int[nums.length];
        suffixProducts[nums.length-1] = 1;
        int[] res = new int[nums.length];
        for(int i = 1, a=nums.length-2; i< nums.length && a >= 0; i++, a--){
            prefixProducts[i] = prefixProducts[i-1] * nums[i-1];
            System.out.printf("index: %d, product: %d\n",i,suffixProducts[a+1]);
            suffixProducts[a] = suffixProducts[a+1] * nums[a+1];
            
        }
        for(int i = 0; i< nums.length; i++){
            res[i] = prefixProducts[i] * suffixProducts[i];
        }
        return res;
    }
}  
