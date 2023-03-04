package chap_06;

public class _07_VariableScope {
    // 지역 변수 { } 안에 생성된 변수는 { } 밖에서는 사용할 수 없음
    // 사용하려면 전달값을 줘야함.
    public static void methodA(int number) {
        // System.out.println(number);
        // System.out.println(result);
        System.out.println(number);
    }

    public static void methodB() {
        int result = 1; // 지역변수
    }
    public static void main(String[] args) {
        int number = 3;

        // System.out.println(result);

        for (int i = 0; i < 3; i++) {
            System.out.println(i);
        }
        // for 문 안에서 선언된 i도 중괄호 안에서만 사용 할 수 있음
        // System.out.println(i);

        {
            int j = 0;
            System.out.println(j);
            System.out.println(number);
        }
        // System.out.println(j);
    }
}
