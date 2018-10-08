public class Main {
    public static void main(String[] args){
        LRUCache lruCache = new LRUCache(2);
        lruCache.put(2,1);
        lruCache.put(2,2);
//        lruCache.put(3,3);
//        lruCache.put(4,10);
//        lruCache.put(5,11);
//        lruCache.put(6,12);
//        lruCache.put(7,13);
//        lruCache.put(8,14);
//        lruCache.put(9,15);
//        lruCache.put(10,16);
//        lruCache.put(11,17);
//        lruCache.put(12,18);
        System.out.print( lruCache.get(2)+" ");
//        System.out.print( lruCache.get(1)+" ");
//        System.out.print( lruCache.get(3)+" ");
//        System.out.print( lruCache.get(4)+" ");
//        System.out.print( lruCache.get(1)+" ");
//        System.out.print( lruCache.get(1)+" ");
//        System.out.print( lruCache.get(1)+" ");
//        System.out.print( lruCache.get(1)+" ");
//        System.out.print( lruCache.get(1)+" ");

    }
}

class LRUCache {

    private int capacity;
    private int[] key;
    private int[] value;
    private int[] mark;//标记是否存满
    public LRUCache(int capacity) {
        this.capacity = capacity;
        key = new int[capacity];
        value = new int[capacity];
        mark = new int[capacity];
        for (int i=0;i<capacity;i++){
            mark[i] = capacity-i-1+capacity;
        }
    }

    public int get(int key) {
        for(int i=0;i<this.capacity;i++){
            if(this.key[i]==key){
                return value[i];
            }
        }
        return -1;

    }

    public void put(int key, int value) {
        int max=0,temp=0;
        boolean falg = true;
        for (int i=0;i<capacity;i++){
            if (mark[i]>=capacity){//成立，说明还没有完成一个周期
                falg = false;
            }
        }
        if (falg){
            for (int i=0;i<capacity;i++){
                mark[i] +=capacity ;
            }
        }
        for (int i=0;i<capacity;i++){
            if (max<mark[i]){
                max = mark[i];
                temp=i;
            }
        }
        this.key[temp] = key;
        this.value[temp] = value;
        mark[temp] = 2*capacity-max-1;
    }
}
