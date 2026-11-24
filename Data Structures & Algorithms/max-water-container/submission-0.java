class Solution {
    public int maxArea(int[] heights) {
        int l = 0; int r = heights.length - 1;
        int max = 0;
        while(l < r){
            int min = Math.min(heights[l], heights[r]);
            if(min * (r - l ) > max ){
                max = min * (r-l);
            }
            if(heights[l] == heights[r]){
                l++;
                r--;
            }
            else if(min == heights[l]){
                l++;
            } else{
                r--;
            }
        }
        return max;
    }
}
