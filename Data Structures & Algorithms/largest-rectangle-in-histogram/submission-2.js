class Solution {
    /**
     * @param {number[]} heights
     * @return {number}
     */
    largestRectangleArea(heights) {
        let stack = [];
        let stack2 = [];
        let n = heights.length
        let leftWidths = [...heights];
        let leftSmallest = [];
        let max = 0;
        for(let i = 0, b = (n-1); i < n; i++, b--){
            // while loop runs while stck not empty and the 
            // stack top is larger than the top of the stack
            // this means the stack will always be increasing
       //     console.log("i: %d", i)console.log("i: %d, b: %d, stack1: %s, stack2: %s", i, b, stack, stack2)
            console.log("i: %d, b: %d, stack1: %s, stack2: %s", i, b, stack, stack2)
            while(stack.length &&  heights[stack.at(-1)] > heights[i]){
                // since heights[i] < heights[top]
                // the next smallest right of curr_element
                // it's popped once it finds one element smaller than it
                let curr_element = stack.pop();
                leftWidths[curr_element] += (i - curr_element - 1) * heights[curr_element];
                //console.log("loop 1: curr: %d, %s",curr_element, leftWidths)
                if(leftWidths[curr_element ] > max){
                    max = leftWidths[curr_element ]
                }
                // 1 undefined 3 undefined undefined undefined
                // undefined 2 undefined 5 5 undefined
            }
            console.log(leftWidths);
             
         //   console.log(stack2)
            
           while(stack2.length &&  heights[stack2.at(-1)] > heights[b]){
                // since heights[i] < heights[top]
                // the next greatest right of heights[i]
                // it's popped once it finds one element greater than it
                let curr_element = stack2.pop();
                leftSmallest[curr_element] = b
                leftWidths[curr_element] += (curr_element - b - 1) * heights[curr_element];
                if(leftWidths[ curr_element] > max){
                    max = leftWidths[curr_element]
                }
           }
            console.log(leftWidths);
            stack.push(i);
            stack2.push(b);
        }
        while(stack.length){
            console.log(stack)
            let curr = stack.pop();
            leftWidths[curr] += (n - curr - 1) * heights[curr];
            if(leftWidths[curr] > max) max = leftWidths[curr]
        }
        while(stack2.length){
            console.log(stack2)
            let curr = stack2.pop();
            leftWidths[curr] += (curr) * heights[curr];
            if(leftWidths[curr] > max) max = leftWidths[curr]
        }
        console.log(leftWidths)
        console.log("left smallest: %s", leftSmallest)
        return max;
    }
}
