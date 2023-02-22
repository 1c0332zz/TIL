package chap_04;

public class _05_For {
    public static void main(String[] args) {
        // 반복문 For
//        for ( 선언 ; 조건 ; 증감 ){
//            수행 명령
//        }
        for (int i = 0; i < 10; i++ ) {
            System.out.println("어서오세요. 옷가계입니다. " + i);
        }

        // 짝수만 출력 (fori 만 적고 엔터하면 for문 양식 완성시켜줌)
        for (int i = 0; i < 10; i += 2) {
            System.out.print(i); // 줄바꿈 없이 하려면 print
        }
        System.out.println();

        // 홀수만 출력
        for (int i = 1; i < 10; i += 2) {
            System.out.print(i);
        }
        System.out.println();

        // 거꾸로 숫자
        for (int i = 5; i > 0; i--) {
            System.out.print(i);
        }
        System.out.println();

        // 1부터 10까지의 수들의 합
        // 1 + 2 + ... + 10 = 55
        int sum = 0;
        for (int i = 1; i <= 10; i++) {
            sum += i;
            System.out.println(sum);
        }
        System.out.println(sum);
    }
}
