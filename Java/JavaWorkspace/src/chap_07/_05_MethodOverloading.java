package chap_07;

public class _05_MethodOverloading {
    // 같은 클래스 내에서 같은 이름을 가진 메소드를 파라미터의 개수나 타입을 다르게 함으로써 다르게 정의
    public static void main(String[] args) {
        BlackBox b1 = new BlackBox();
        b1.modelName = "퐁퐁이";

        b1.record(false, false, 10);
        System.out.println("----------------");
        b1.record(true, false, 3);
        System.out.println("----------------");
        b1.record();

        // String
        // 이것도 메소드로 미리 작성되어있는 것
        String s = "BlackBox";
        System.out.println(s.indexOf("a"));
    }
}
