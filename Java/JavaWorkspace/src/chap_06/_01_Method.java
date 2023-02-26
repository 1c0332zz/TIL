package chap_06;
// 어떤 기능을 하는 코드들의 묶음 (함수)
public class _01_Method {
    public static void sayHello() {
        // 메소드 정의
        // 메소드명은 동작을 의미하는 경우가 많아서 변수를 만들때 주의
        System.out.println("안녕하세요. 메소드입니다.");
    }

    public static void main(String[] args) {
        // 메소드 호출
        System.out.println("메소드 호출 전");
        sayHello();
        System.out.println("메소드 호출 후");
    }
}
