class Solution {
    public int evalRPN(String[] tokens) {
        Deque<Integer> q = new ArrayDeque<Integer>(); 
        int res = 0;
        for(String str : tokens){
            char c = str.charAt(0);
            System.out.printf("c: %c, ", c);
            int a, b;
             //   System.out.printf("Last executed: %c\n", c);
            if(str.length() == 1 && !Character.isDigit(c)){
                switch(c){
                    case '+':
                        res = q.removeLast() + q.removeLast();
                        break;
                    case '-':
                        b = q.removeLast();
                    //   System.out.printf("Res: %d, b :%c", res, b);
                        a = q.removeLast();
                        res = a - b; 
                        break; 
                    case '*':
                        res = q.removeLast() * q.removeLast(); 
                        break;
                    case '/':
                        b = q.removeLast(); 
                        System.out.printf(" %d\n",b  );
                        a = q.removeLast();
                        res = b==0?0:(a/b);
                        System.out.printf("%d / %d : %d\n",a , b, res );
                        break;
                }
            } else {
                try{
                    res = Integer.valueOf(str);
                } catch (Exception e){
                    res = 1;
                }
            }
            System.out.printf("C: %c, Res: %d, ",c, res);
            q.addLast(res);
              
            
        }
        return res;

    }
}
