package chap_11;

public class _01_TryCatch {
    public static void main(String[] args) {
        // 예외 처리
        // 오류 : 컴파일 오류, 런타임 오류 (에러 error, 예외 exception)

        // 컴파일 오류 (빌드 실패, 빨간줄)
        // int i = "문자열";

        // 런타임 오류 (에러 error, 예외 exception)
        // int[] arr = new int[3];
        // arr[5] = 100;

        // 에러, StackOverflowError => 무한히 자기자신을 호출하거나 끝없이 계산되는것
//        S s = new S();
//        s.methodA();

        // 예외 에러
//        S s = null;
//        s.methodA();

        // 예외 처리 문법
        try {
            // System.out.println(3 / 0);// 시도하려는 소스 코드

            // int[] arr = new int[3];
            // arr[5] = 100;

            Object obj = "test";
            System.out.println((int) obj);
        } catch (Exception e) {
            System.out.println("이런 문제가 발생 하였습니다. => " + e.getMessage()); // 문제에 대한 처리
            e.printStackTrace();
        }

        System.out.println("프로그램 정상 종류");
    }
}

// StackOverflowError => 무한히 자기자신을 호출하거나 끝없이 계산되는것
//class S {
//    public void methodA() {
//        this.methodA();
//    }
//}