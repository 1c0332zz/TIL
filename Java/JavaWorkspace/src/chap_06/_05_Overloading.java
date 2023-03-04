package chap_06;

public class _05_Overloading {
    public static int getPower(int number) {
        int result = number * number;
        return result;
        // 한줄로 줄일수도 있음
        // return number * number'
    }
    public static int getPower(String strNumber) {
        int number = Integer.parseInt(strNumber);
        return number * number;
    }

    public static int getPower(int number, int exponent) {
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= number;
        }
        return result;
    }

    public static void main(String[] args) {
        // 메소드 오버로딩
        // 이름이 같은 메소드를 여러번 선언
        // 1. 전달값의 개수가 다르거나
        // 2. 타입이 다를 경우
        // 3. 반환형이 다를경우는 X
        System.out.println(getPower(3)); // 3 * 3 = 9
        System.out.println(getPower("4")); // 4 * 4 = 16

        System.out.println(getPower(3,3)); // 27
    }
}