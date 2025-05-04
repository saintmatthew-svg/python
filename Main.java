public class Main {
    public static int sumOfOddIndexNumbersRightToLeft(int[] creditCardNumber) {
        int sum = 0;
        for (int count = creditCardNumber.length - 1; count >= 0; count-=2) {
            int doubled = creditCardNumber[count] * 2;
            if (doubled > 9) {
                int single1 =  doubled % 10;
                doubled /= 10;
                int single2 = doubled % 10;
                int num = single1 + single2; 
                sum += num;
            } else {
                sum += doubled;
            }
        }
        return sum;
    }

    public static void main(String[] args){
        int[] creditCardNumber = {4,3,8,8,5,7,6,0,1,8,4,0,2,6,2,6};
        System.out.print(sumOfOddIndexNumbersRightToLeft(creditCardNumber));
    }
}
