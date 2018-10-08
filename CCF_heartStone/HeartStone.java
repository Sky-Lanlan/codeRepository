//import java.util.Scanner;
//
//public class Main_3 {
//    public static void main(String[] args){
//        Player player1 = new Player();
//        Player player2 = new Player();
////        player1.summon("Rose",1,6,3);
////        player1.summon("FuDing",2,2,4);
////
////        player2.summon("lanLong",1,5,4);
////        player2.summon("lanLon",1,1,2);
////        player2.attack(player1.getAttendants(1), player2.getAttendants(2));
////
////        if (player2.getAttendants(2).getHealth() <= 0)
////            player2.attendantDie(2);
////        if (player1.getAttendants(1).getHealth() <= 0)
////            player1.attendantDie(1);
////
////        player1.attack(player1.getAttendants(1),  player2.getAttendants(1));
////        if (player2.getAttendants(1).getHealth() <= 0)
////            player2.attendantDie(1);
////        if (player1.getAttendants(1).getHealth() <= 0)
////            player1.attendantDie(1);
//        Scanner input = new Scanner(System.in);
//        int commondN = Integer.parseInt(input.nextLine());
//        String[] commonC = new String[commondN];
//        boolean flag = true;
//        for (int i = 0;i<commondN;i++){
//            commonC[i] = input.nextLine();
//            String[] commondE = commonC[i].split(" ");
//            if (flag) {
//                if (commondE[0].contains("summon"))
//                    player1.summon(Integer.parseInt(commondE[1]), Integer.parseInt(commondE[2]), Integer.parseInt(commondE[3]));
//                if (commondE[0].contains("attack")) {
//                    player1.attack(player1.getAttendants(Integer.parseInt(commondE[1])),
//                            player2.getAttendants(Integer.parseInt(commondE[2])));
//                    if (player2.getAttendants(Integer.parseInt(commondE[2])).getHealth() <= 0)
//                        player2.attendantDie(Integer.parseInt(commondE[2]));
//                    if (player1.getAttendants(Integer.parseInt(commondE[1])).getHealth() <= 0)
//                        player1.attendantDie(Integer.parseInt(commondE[1]));
//                }
//            }
//            else {
//                if (commondE[0].contains("summon"))
//                    player2.summon(Integer.parseInt(commondE[1]), Integer.parseInt(commondE[2]), Integer.parseInt(commondE[3]));
//                if (commondE[0].contains("attack")) {
//                    player2.attack(player2.getAttendants(Integer.parseInt(commondE[1])),
//                            player1.getAttendants(Integer.parseInt(commondE[2])));
//                    if (player1.getAttendants(Integer.parseInt(commondE[2])).getHealth() <= 0)
//                        player1.attendantDie(Integer.parseInt(commondE[2]));
//                    if (player2.getAttendants(Integer.parseInt(commondE[1])).getHealth() <= 0)
//                        player2.attendantDie(Integer.parseInt(commondE[1]));
//                }
//            }
//            if (commondE[0].contains("end"))
//                flag = !flag;
//        }
//        if (!player1.isAlive())
//            System.out.println(2);
//        else if (!player2.isAlive())
//            System.out.println(1);
//        else System.out.println(0);
////        for (int i = 0; i<commondN;i++)
//        player1.check();
//        player2.check();
//
//
//    }
//}
//
//class Attendant{
//    private int health;
//    private int atk;
//    private String name;
//    private int position;
////    Attendant(String name,int health, int atk,int position){
////        this.health = health;
////        this.atk = atk;
////        this.name = name;
////        this.position = position;
////    }
//Attendant(int health, int atk,int position){
//    this.health = health;
//    this.atk = atk;
//    this.position = position;
//}
//
//
//    public boolean isAlive() {
//        if (this.health<=0)
//            return false;
//        else
//            return true;
//    }
//
//    public void setHealth(int health) {
//        this.health = health;
//    }
//
//    public int getHealth() {
////        if (health <=0 )
//        return health;
//    }
//
//    public int getAtk() {
//        return atk;
//    }
//
//    public int getPosition() {
//        return position;
//    }
//
//    public void setPosition(int position) {
//        this.position = position;
//    }
//}
//class Player{
//    private int health = 30;
//    private int atk = 0;
//    private int attendantNum = 0;//随从个数
//    private Attendant[] attendants = new Attendant[7];
////    private Attendant[] attendants;
//    void summon( int position,int atk,int health ){//召唤随从
//
////        attendants[position] = new Attendant(name,health,atk,position);
//        if (attendantNum > 0 && position <= attendantNum) {
////            attendants[position] = new Attendant(name, health, atk, position);
//            for (int i = attendantNum;i >= position;i--) {
//                attendants[i + 1] = attendants[i];
//                attendants[i + 1].setPosition(i + 1);
//            }
//            attendants[position] = new Attendant( health, atk, position);
//        }
//        attendants[position] = new Attendant( health, atk, position);
//        attendantNum++;
//    }
//
//    public Attendant getAttendants(int position) {
//        return attendants[position];
//    }
//    void attendantDie(int dPosition){
//
//        if(dPosition < attendantNum)
//            for (int i = dPosition;i<attendantNum;i++){
//                attendants[i] = attendants[i+1];
//                attendants[i].setPosition(i);
//            }
//        attendantNum--;
//
//    }
//    void check(){
//        System.out.println(this.health);
//        for(int i = 1;i <= attendantNum;i++)
//            System.out.println(i+" "+attendants[i].getHealth());
//    }
//
//    void attack(Attendant a, Attendant b){
//        a.setHealth(a.getHealth() - b.getAtk());
//        b.setHealth(b.getHealth() - a.getAtk());
//
////        if (!b.isAlive()&&attendantNum>1)//有随从死亡且场上仍然还存在随从
////            for (Attendant rest:attendants)
////                if (rest.getPosition() > a.getPosition())
////                    rest.setPosition(rest.getPosition()-1);
//    }
//    void attack(Attendant a, Player b){
////        if (b.getHealth()-a.getAtk() <= 0)
////            attendantDie();
////        if(a.getHealth()-b.getAtk()<=0)
////            attendantDie();
//        b.setHealth(b.getHealth()-a.getAtk());
//        a.setHealth(a.getHealth()-b.getAtk());
//    }
//
//    public int getAtk() {
//        return atk;
//    }
//
//    public boolean isAlive(){
//        if (this.health <= 0)
//            return false;
//        else
//            return true;
//    }
//    public int getHealth() {
//        return health;
//    }
//
//    public void setHealth(int health) {
//        this.health = health;
//    }
//
//}
import java.util.Scanner;

public class HeartStone {
    public static void main(String[] args){
        Player player1 = new Player();
        Player player2 = new Player();
        Scanner input = new Scanner(System.in);
        int commondN = Integer.parseInt(input.nextLine());
        String[] commonC = new String[commondN];
        boolean flag = true;
        for (int i = 0;i<commondN;i++){
            commonC[i] = input.nextLine();
            String[] commondE = commonC[i].split(" ");
            if (flag) {
                if (commondE[0].contains("summon"))
                        player1.summon(Integer.parseInt(commondE[1]), Integer.parseInt(commondE[2]), Integer.parseInt(commondE[3]));
                if (commondE[0].contains("attack")) {
                    if (Integer.parseInt(commondE[2])!=0) {
                        player1.attack(player1.getAttendants(Integer.parseInt(commondE[1])),
                                player2.getAttendants(Integer.parseInt(commondE[2])));
                        if (player2.getAttendants(Integer.parseInt(commondE[2])).getHealth() <= 0)
                            player2.attendantDie(Integer.parseInt(commondE[2]));
                        if (player1.getAttendants(Integer.parseInt(commondE[1])).getHealth() <= 0)
                            player1.attendantDie(Integer.parseInt(commondE[1]));
                    }
                    else    player1.attack(player1.getAttendants(Integer.parseInt(commondE[1])),player2);
                }
            }
            else {
                if (commondE[0].contains("summon"))
                    player2.summon(Integer.parseInt(commondE[1]), Integer.parseInt(commondE[2]), Integer.parseInt(commondE[3]));
                if (commondE[0].contains("attack")) {
                    if (Integer.parseInt(commondE[2])!=0) {
                        player2.attack(player2.getAttendants(Integer.parseInt(commondE[1])),
                                player1.getAttendants(Integer.parseInt(commondE[2])));
                        if (player1.getAttendants(Integer.parseInt(commondE[2])).getHealth() <= 0)
                            player1.attendantDie(Integer.parseInt(commondE[2]));
                        if (player2.getAttendants(Integer.parseInt(commondE[1])).getHealth() <= 0)
                            player2.attendantDie(Integer.parseInt(commondE[1]));
                    }
                    else player2.attack(player2.getAttendants(Integer.parseInt(commondE[1])),player1);

                }
            }
            if (commondE[0].contains("end"))
                flag = !flag;
        }
        if (!player1.isAlive())
            System.out.println(2);
        else if (!player2.isAlive())
            System.out.println(1);
        else System.out.println(0);
        player1.check();
        player2.check();


    }
}

class Attendant{
    private int health;
    private int atk;
    private String name;
    private int position;
    Attendant(int health, int atk,int position){
        this.health = health;
        this.atk = atk;
        this.position = position;
    }


    public boolean isAlive() {
        if (this.health<=0)
            return false;
        else
            return true;
    }

    public void setHealth(int health) {
        this.health = health;
    }

    public int getHealth() {
        return health;
    }

    public int getAtk() {
        return atk;
    }

    public int getPosition() {
        return position;
    }

    public void setPosition(int position) {
        this.position = position;
    }
}
class Player{
    private int health = 30;
    private int atk = 0;
    private int attendantNum = 0;//随从个数
    private Attendant[] attendants = new Attendant[7];
    void summon( int position,int atk,int health ){//召唤随从
        if (attendantNum > 0 && position <= attendantNum) {
            for (int i = attendantNum;i >= position;i--) {
                attendants[i + 1] = attendants[i];
                attendants[i + 1].setPosition(i + 1);
            }
            attendants[position] = new Attendant( health, atk, position);
        }
        attendants[position] = new Attendant( health, atk, position);
        attendantNum++;
    }
    public Attendant getAttendants(int position) {
        return attendants[position];
    }
    void attendantDie(int dPosition){

        if(dPosition < attendantNum)
            for (int i = dPosition;i<attendantNum;i++){
                attendants[i] = attendants[i+1];
                attendants[i].setPosition(i);
            }
        attendantNum--;
    }
    void check(){
        System.out.println(this.health);
        System.out.print(attendantNum);
        for(int i = 1;i <= attendantNum;i++)
            System.out.print(" " + attendants[i].getHealth());
        System.out.println();
    }
    void attack(Attendant a, Attendant b){
        a.setHealth(a.getHealth() - b.getAtk());
        b.setHealth(b.getHealth() - a.getAtk());
    }
    void attack(Attendant a, Player b){
        b.setHealth(b.getHealth()-a.getAtk());
        a.setHealth(a.getHealth()-b.getAtk());
    }
    public int getAtk() {
        return atk;
    }

    public boolean isAlive(){
        if (this.health <= 0)
            return false;
        else
            return true;
    }
    public int getHealth() {
        return health;
    }

    public void setHealth(int health) {
        this.health = health;
    }

}
