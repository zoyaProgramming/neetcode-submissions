class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        Set<List<Integer>> set = new HashSet<List<Integer>>();

       // List<List<Integer>> res = new ArrayList<List<Integer>>();

        
        for(int i = 0; i < nums.length - 2 && nums[i] <= 0; i++){
            int a = i+1, b = nums.length - 1;
            while(a < b){
                if(nums[a] + nums[b] == -1 * nums[i]){
                    System.out.printf("sum == target: %d, %d, %d\n", nums[a], nums[b], nums[i]);
                    set.add(new ArrayList<Integer>(Arrays.asList(nums[a], nums[b], nums[i])));
                    a++; b--;
                } else if (nums[a] + nums[b] < (-1 * nums[i])){
                    System.out.printf("sum < target: %d, %d, %d\n", nums[a], nums[b], -1 * nums[i]);
                    a++;
                } else {
                    System.out.printf("sum > target: %d, %d, %d\n", nums[a], nums[b], -1 * nums[i]);
                    b--;
                }
            } 

        }
        return new ArrayList<List<Integer>>(set);

    }
}
