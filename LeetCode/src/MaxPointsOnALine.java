
import java.util.HashMap;
import java.util.Map;


public class MaxPointsOnALine {
    public static void main(String[] args) {
        Point[] point = initPoint();
        int res = maxPoints(point);
        System.out.print(res);
    }

    private static Point[] initPoint() {
        Point[] points;
        points = new Point[3];
        points[0] = new Point(2,3);
        points[1] = new Point(3,3);
        points[2] = new Point(-5,3);
//        points[3] = new Point(9,-25);
//        points[4] = new Point(-28,-134);
//        points[5] = new Point(40,-23);
//        points[6] = new Point(-72,-149);
//        points[7] = new Point(32,-32);
//        points[8] = new Point(-207,288);
//        points[9] = new Point(7,32);
//        points[10] = new Point(-5,0);
//        points[11] = new Point(-161, 216);
//        points[12] = new Point(-48, -122);
//        points[13] = new Point(-3, 39);
//        points[14] = new Point(-40, -133);
//        points[15] = new Point(115, -216);
//        points[16] = new Point(-112, -464);
//        points[17] = new Point(-72, -149);
//        points[18] = new Point(-32, -104);
//        points[19] = new Point(12, 42);
//        points[20] = new Point(-22, 19);
//        points[21] = new Point(-6, -21);
//        points[22] = new Point(-48, -122);
//        points[23] = new Point(161, -288);
//        points[24] = new Point(16, 11);
//        points[25] = new Point(39, 23);
//        points[26] = new Point(39, 30);
//        points[27] = new Point(873, -111);
//        points[28] = new Point(0, -17);


//        points[3] = new Point(-6, -1);
//        points[4] = new Point(2, 2);
//        points[5] = new Point(2, 2);
        return points;

    }


    public static int maxPoints(Point[] points) {
        Map<Map<Integer, Integer>, Integer> xieLu = new HashMap<>();
        Map<Integer, Integer> fenShu = new HashMap<>();
        if (points.length==0){
            return 0;
        }
        if (points.length<=2){
            return points.length;
        }
        int  result = 0;
        for (int i = 0; i < points.length; i++) {
            xieLu.clear();
            int max=0,overlap=0;
            for (int k = i + 1; k < points.length; k++) {
               fenShu.clear();
                int x = points[k].x - points[i].x;
                int y = points[k].y - points[i].y;
                if (x==y&&x==0){
                    overlap++;
                    continue;
                }
                if (x*y<0){
                    x=-Math.abs(x);
                    y=Math.abs(y);
                }else {
                    x = Math.abs(x);
                    y = Math.abs(y);
                }
                int maxV = 1;

                if (x==0){
                    y=1;
                }
                if (y==0){
                    x=1;
                }
                maxV=generateGCD(x,y);
                if (maxV!=0) {
                    fenShu.put(x / maxV, y / maxV);
                }
                if (xieLu.containsKey(fenShu)) {
                    xieLu.put(fenShu, xieLu.get(fenShu) + 1);
                } else {
                    xieLu.put(fenShu, 1);

                }
                max= Math.max(max,xieLu.get(fenShu));
            }
            result = Math.max(max+overlap+1,result);
        }
        return result;
    }

    private static int generateGCD(int x, int y) {
        if (y==0) return x;
        else return generateGCD(y,x%y);

    }
}

    class Point {
        int x;
        int y;

        Point() {
            x = 0;
            y = 0;
        }

        Point(int a, int b) {
            x = a;
            y = b;
        }
    }

