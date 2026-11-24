class Solution {
    public boolean isPalindrome(String s) {
        int a = 0;
        int b = s.length() -1;
        s = s.toLowerCase();
        while(a < b){
            
            while(a < s.length() && !Character.isLetterOrDigit(s.charAt(a))) {
                a++;
            }
            while(b > 0 && !Character.isLetterOrDigit(s.charAt(b))) {
                b--;
            }
            if(a >= b) break;
            if(s.charAt(a++) != s.charAt(b--)) return false;
            
        }
        return true;
    }
}
