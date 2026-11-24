class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length() ){return false;}
        HashMap<Character, Integer> h1 = new HashMap<Character, Integer>();
        HashMap<Character, Integer> h2 = new HashMap<Character, Integer>();
        for(int i = 0; i<s.length(); i++){
            System.out.println("djsifojds");
            Character j = s.charAt(i), k= t.charAt(i);
            Integer a = h1.get(s.charAt(i));
            Integer b = h2.get(t.charAt(i));
            if(a == null) {
                h1.put(j, Integer.valueOf(1));
            } else {
                h1.put(j, Integer.valueOf(a+ 1));
            }
            if(b == null) {
                h2.put(k, Integer.valueOf(1));
            } else {
                h2.put(k, Integer.valueOf(b+1));
            }
        }
        System.out.println(h1);
        System.out.println(h2);
        return h1.equals(h2);
    }
}
