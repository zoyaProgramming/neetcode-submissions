class Solution {
    public boolean hasDuplicate(int[] nums) {
        HashMap<Integer, Integer> exists = new HashMap<Integer,Integer>();
        for(int i = 0; i< nums.length; i++){
            if(exists.get(nums[i]) == null){
                exists.put(nums[i], new Integer( i));
            } else {
                return true;
            }
        }
        return false;
    }
}