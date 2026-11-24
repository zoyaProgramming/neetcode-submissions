class Solution {
    /**
     * @param {number} target
     * @param {number[]} position
     * @param {number[]} speed
     * @return {number}
     */
    carFleet(target, position, speed) {
        let arr = [];
        let n = position.length;
        for(let i = 0; i < n; i++){
            arr[i] = [position[i], speed[i]];
        }
        arr.sort((a, b) => {
            return a[0] > b[0]?1:(a[0]==b[0])?0:-1
        })
        let stack = [];

        let len = n;
        for(let i = 0; i < n; i++ ){
            let prev = stack.length? arr[stack[stack.length - 1]]: null;
            function condition(a, b){
                return a[1] < b[1]; // if b[1 ]
            }
            while(stack.length && prev[1] > arr[i][1] && (target - prev[0])/prev[1] <= (target - arr[i][0])/(arr[i][1])){ // 
                let current_element = stack.pop();
                len--;
                prev = stack.length? arr[stack[stack.length - 1]]: null;
            }
            stack.push(i);
        }
        console.log(stack)
        return stack.length;
    }
}
