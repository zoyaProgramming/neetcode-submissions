class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> res = new ArrayList<List<String>>();
        HashMap<HashMap<Character, Integer>, Integer> maps = new HashMap<HashMap<Character, Integer>, Integer>();
        for(int i = 0 ; i < strs.length ; i++){
            HashMap<Character, Integer> hm = new HashMap<Character, Integer>();
            for(int j = 0; j < strs[i].length(); j++){
                hm.put(strs[i].charAt(j), hm.getOrDefault(strs[i].charAt(j), 0) + 1);
            } 
            if(maps.get(hm) == null){
                System.out.println(maps.size());
                maps.put(hm, maps.size());
                List<String> c = new ArrayList<String>();
                c.add(strs[i]);
                res.add(c);
            } else{
                int index = maps.get(hm);
                System.out.println("index: " +  index);
                List<String> mine = res.get(index);
                mine.add(strs[i]);
            }

        }
        return res;
    }
}
