class Solution {
    /**
     * @param {number[]} temperatures
     * @return {number[]}
     */
    dailyTemperatures(temperatures) {
        let stack = [];
        let arr = new Array(temperatures.length)
        for(let i = 0; i <  temperatures.length; i++){
            while (stack.length  && temperatures[ stack[stack.length - 1]] < temperatures[i]){
                let stackTop = stack.pop();
                arr[stackTop] = i - stackTop;
            }
            if(arr[i] == undefined){
                arr[i] = 0
            }
            stack.push(i);
        }
        return arr;
    }
}
