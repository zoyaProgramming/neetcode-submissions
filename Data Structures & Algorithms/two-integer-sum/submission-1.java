class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        HashMap<Integer, Integer> existing = new HashMap<Integer, Integer>();

        for(int i = 0; i < nums.length; i++){
            Integer c = existing.get(target - nums[i]);
            if(c != null){
                int[] res = {c, i};
                return res;
            }
            existing.put(nums[i], i);
        }
        return null;
    }
}
