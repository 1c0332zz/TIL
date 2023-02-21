package chap_02;

public class _01_Operator1 {
    public static void main(String[] args) {
        // 연산자

        // 일반 연산
        System.out.println(2 + 4); // 6
        System.out.println(2 - 4); // -2
        System.out.println(4 * 2); // 8
        System.out.println(4 / 2); // 2
        System.out.println(4 % 2); // 0

        // 증감 연산 ++, --
        // ++val은 1을 더한 후 문장을 실행시켜줌
        int val;
        val = 10;
        System.out.println(val); // 10
        System.out.println(++val); // 11
        System.out.println(val); // 11

        // val++은 ++val과 다르게 문장을 다 수행한 뒤 1을 더해줌
        val = 10;
        System.out.println(val); // 10
        System.out.println(val++); // 10
        System.out.println(val); // 11

        // 예제
        // 은행 대기번호 표
        int waiting = 0;
        System.out.println("대기인원 : " + waiting++); // 대기인원 : 0
        System.out.println("대기인원 : " + waiting++); // 대기인원 : 1
        System.out.println("대기인원 : " + waiting++); // 대기인원 : 2
        System.out.println("총 대기인원 : " + waiting); // 총 대기인원 : 3
    }
}
