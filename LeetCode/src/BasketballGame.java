import java.util.Stack;

public class BasketballGame {
    public static void main(String[] args){
        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);

        System.out.print(stack.peek());
        System.out.print(stack.peek());
        stack.empty();
    }
}
