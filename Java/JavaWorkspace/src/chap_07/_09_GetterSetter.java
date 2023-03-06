package chap_07;

public class _09_GetterSetter {
    // getter & setter 를 설정하면 값 설정하다가 불러오는 오류를 줄일 수 있고 여러 오류에 대안으로 설정할 수 있다.
    public static void main(String[] args) {
        BlackBox b1 = new BlackBox();
        b1.modelName = "퐁퐁이";
        b1.resolution = "FHD";
        b1.price = 50000;
        b1.color = "블랙";

        // 할인행사
        b1.price = -5000;
        System.out.println("가격 : " + b1.price + "원");

        // 고객 문의
        System.out.println("해상도 : " + b1.resolution);

        System.out.println("------오류 설정 후-----");

        // Setter 로 설정
        BlackBox b2 = new BlackBox();
        // 실수로 resolution 안넣음
        b2.setModelName("팡팡이");
        b2.setPrice(-5000);
        b2.setColor("화이트");

        // Getter 로 설정
        System.out.println("가격 : " + b2.getPrice() + "원");
        System.out.println("해상도 : " + b2.getResolution());

        // 하지만 여전히 아래처럼 설정하면 다시 돌아감
        b2.price = -5000;
        System.out.println(b2.getPrice());
    }
}
