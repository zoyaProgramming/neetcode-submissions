class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int a = 0;
        int b = numbers.length -1;
        while ( a < b){
            int curSum = numbers[a] + numbers[b];
            if(curSum < target){
                a++;
            }
            else if (curSum > target){
                b--;
            }
            else {
            
                return new int [] {a + 1, b + 1};
            }
        }
        return new int[0];
    }
}
