class Solution {
    public boolean isValidSudoku(char[][] board) {
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] rows = new HashSet[9];
        for(int i = 0 ; i< 9; i++){
            cols[i] = new HashSet<Character>();
            rows[i] = new HashSet<Character>();
        }
        int n =9;
        for(int l = 0; l < 9; l += 3){
        for(int c = 0; c < 9; c+= 3){
            HashSet<Character> section = new HashSet<Character>();
            for(int i = l; i < l+3; i++){
                
              //  if(rows[i] == null ) {rows[i] = new HashSet<Character>();}
                for(int j = c; j< c+3 ; j++ ){
                    System.out.printf("i%d j%d, %c, b%b\n",i, j, board[i][j], isDigit(board[i][j]));
               //     if(cols[j] == null ) cols[j] = new HashSet<Character>();
                    if(isDigit(board[i][j]))
                    {
                        System.out.printf("sfdi board[%d][%d] : %c\n",i,j, board[i][j]);
                        char ch = board[i][j];
                        if(!rows[i].add(ch) || !cols[j].add(ch) || !section.add(ch)){                            
                          //  System.out.printf("row %d col %d value %c\n", i, j, board[i][j]);
                            return false;
                        }
                       /* else if(!cols[j].add(board[i][j])) {
                            System.out.printf("row %d col %d value %c\n", i, j, board[i][j]);
                            return false;
                        }
                        else if(!section.add(board[i][j])){ 
                            System.out.printf("row %d col %d value %d\n", i, j, board[i][j]);
                            return false;
                            }*/
                    }
                }
            }
            
            
        }
        }
        return true;
    }
    public boolean isDigit(char c){
        return (c >= '1') && (c <= '9');
    }
}
