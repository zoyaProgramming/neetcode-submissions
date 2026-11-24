class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> m = new HashSet<Integer>();

        int count = 0;
        for(int i = 0; i< nums.length; i++){
            m.add(nums[i]);
        }
        int longest = 0;
        for(int num : m){
            if(!m.contains(num -1)){
                int length = 1;
                while(m.contains(num + length)){
                    length++;
                }
                longest = Math.max(longest, length);
            }
        }
        return longest;
    }
}
