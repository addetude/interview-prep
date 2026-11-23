import java.util.Stack;
class Solution {
    public boolean isValid(String s) {
        Stack stack = new Stack();
        int length = s.length();
        String [] arr = s.split("");
        for(int i = 0; i < length; i++){
            if(arr[i].equals("(") || arr[i].equals("[") || arr[i].equals("{")){
                stack.push(arr[i]);
            }else{
                if(stack.empty() == true){
                    return false;
                }else if(stack.peek().equals("(") && arr[i].equals(")") || stack.peek().equals("[") && arr[i].equals("]") || stack.peek().equals("{") && arr[i].equals("}")){
                    stack.pop();
                }else{
                    return false;
                }
            }
        }
        return stack.empty();
    }
}