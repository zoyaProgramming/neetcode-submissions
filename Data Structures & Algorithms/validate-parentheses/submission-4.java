class Solution {
    public boolean isValid(String s) {
        if(s.length()%2 ==1) return false;
        Stack<Character> stack = new Stack<Character>();
        char[] charArray = s.toCharArray();
        int i =0;
        do{
            Character c = charArray[i++];
            switch(c){
                case '(','{','[':
                    stack.push(c);
                    break;
                case ')':
                    if(stack.size() == 0) return false;
                    if(stack.pop() != '(') return false;
                    break;
                case '}':
                    if(stack.size() == 0) return false;
                    Character c1 = stack.pop();
                    System.out.printf("c: %c, c1: %c\n", c, c1);
                    if(c1!= '{') return false;
                    break;
                case ']':
                    if(stack.size() == 0) return false;
                    if(stack.pop() != '[') return false;
                    break;
                default:
                    return false;
            }

        } while( i < charArray.length);
        if(stack.size() > 0 )return false;
        return true;
    }
}
