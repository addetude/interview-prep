import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack <Character> stack = new Stack<Character>();
        int length = s.length();
        for(int i = 0; i < length; i++){
            char a = s.charAt(i);
            if(a == '(' || a == '[' || a == '{'){
                stack.push(a);
            }else{
                if(stack.empty() == true){
                    return false;
                }else if(stack.peek() == '(' && a == ')' || stack.peek() == '[' && a == ']' || stack.peek() == '{' && a == '}'){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
        return stack.empty();
    }
}