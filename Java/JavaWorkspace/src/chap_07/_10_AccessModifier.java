package chap_07;

public class _10_AccessModifier {
    public static void main(String[] args) {
        // 캡슐화 (Encapsulation)
        // 서로 관련이 있는 데이터, 기능, 메소드 등을 하나의 클래스로 정의

        // 정보은닉 (Information hiding)
        // 객체나 변수의 직접적인 접근을 막고 허용하는 형태로만 접근이 가능하게 하도록 함

        // 접근 제어자
        // private : 해당 클래스 내에서만 접근 가능
        // public : 모든 클래스에서 접근 가능
        // default : (아무것도 적지 않았을 때) 같은 패키지 내에서만 접근 가능 / 패키지: chap_07안에 속해있는 것
        // protected : 같은 패키지 내에서, 다른 패키지인 경우 자식 클래스에서 접근 가능

        BlackBoxRefurbish b1 = new BlackBoxRefurbish();
        // 실수로 resolution 안넣음
        b1.modelName = "퐁퐁이";
        b1.setPrice(200000);
        b1.color = "블랙";

        // 할인행사
        b1.setPrice(-5000);
        System.out.println("가격 : " + b1.getPrice() + "원");

        // 고객 문의
        System.out.println("해상도 : " + b1.resolution);

        System.out.println("------오류 설정 후-----");

        // Setter 로 설정
        BlackBoxRefurbish b2 = new BlackBoxRefurbish();
        // 실수로 resolution 안넣음
        b2.setModelName("팡팡이");
        b2.setPrice(-5000);
        b2.setColor("화이트");

        // Getter 로 설정
        System.out.println("가격 : " + b2.getPrice() + "원");
        System.out.println("해상도 : " + b2.getResolution());

        // 하지만 여전히 아래처럼 설정하면 다시 돌아감
        // 이런 경우 접근제어자(private)를 통해 막을 수 있음
//        b2.price = -5000;
//        System.out.println(b2.getPrice());


    }
}
