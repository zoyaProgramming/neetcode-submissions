class Solution {

    public String encode(List<String> strs) {
        StringBuilder sb = new StringBuilder();
        for(String str: strs){
            int len = str.length();
            sb.append(Integer.toString(len) + "#");
            sb.append(str);
        }
        return sb.toString();
    }

    public List<String> decode(String str) {

        List<String> res = new ArrayList<String>();
        int i = 0;
        while( i < str.length()){
            System.out.println("running");
            char c = str.charAt(i);
            int num = 0;
            while(c != '#'){
                num *= 10;
                num += (int)( c - '0');
                i++;
                c = str.charAt(i);
            }
            i++;
            StringBuilder sb = new StringBuilder();
            int cutoff = (i + num );
            while(i < cutoff){
                sb.append(str.charAt(i));
                i++;
            }
            res.add(sb.toString());
        }
        return res;
    }
}
