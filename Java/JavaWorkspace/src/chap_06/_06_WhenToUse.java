package chap_06;

public class _06_WhenToUse {
    // 제곱 구하기
    public static int getPower(int number) {
        return getPower(number, 2);
    }
    // 2개의 수 정해서 제곱 구하기
    public static int getPower(int number, int exponent) {
        int result = 1;
        for (int i = 0; i < exponent; i++) {
            result *= number;
        }
        return result;
    }
    public static void main(String[] args) {
        // 메소드가 필요한 이유

        // 2의 2승 구하기
//        int result = 1;
//        for (int i = 0; i < 2; i++) {
//            result *= 2;
//        }
//        System.out.println(result); // 4
        System.out.println(getPower(2,2));
        
        // 3의 2승 구하기
//        result = 1;
//        for (int i = 0; i < 3; i++) {
//            result *= 3;
//        }
//        System.out.println(result); // 27
        System.out.println(getPower(3,2));
        
        // 4의 2승 구하기
//        result = 1;
//        for (int i = 0; i < 2; i++) {
//            result *= 4;
//        }
//        System.out.println(result); // 16
        System.out.println(getPower(4,2));

        // 5의 제곱
        System.out.println(getPower(5));
    }
}
