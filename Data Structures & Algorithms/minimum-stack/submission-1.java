class MinStack {
    private int size;
    private int[] array;
    private int max_len = 10;

    private int min_size;
    private int[] min_array;
    private int max_min_len = 10;
    

    public MinStack() {
        array = new int[10];
        min_array = new int[max_min_len];
        size = 0;
        min_size = 0;
    }
    
    public void push(int val) {
        if(size + 1 > max_len){
            expand_array();
        }
        if(min_size ==0 || (min_size > 0 && val <= array[min_array[min_size - 1]])){
            if(min_size == max_min_len) expand_mins();
            min_array[min_size++] = size;
        }
        array[size++] = val;
        System.out.printf("top : %d\n" ,array[size-1]);
    }
    
    public void pop() {
        this.size -=1;
        if(min_size > 0 && min_array[min_size - 1] == size){
            min_array[--min_size] = 0;
        }

        if(size > 0) array[size] = 0;
    }
    
    public int top() {
        return array[size - 1];
    }
    
    public int getMin() {
        return array[min_array[min_size - 1]];
    }
    private void expand_array(){
        int[] new_array = new int[size * 2];
        for(int i = 0; i<size; i++){
            new_array[i] = array[i];
        }
        array = new_array;
    }
    private void expand_mins(){
        int[] new_array = new int[min_size * 2];
        for(int i = 0; i<min_size; i++){
            new_array[i] = array[i];
        }
        min_array = new_array;
    }
}
