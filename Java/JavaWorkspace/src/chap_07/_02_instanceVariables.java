package chap_07;

public class _02_instanceVariables {
    public static void main(String[] args) {
        // BlackBox 클래스를 통해 b1 이라는 객체 생성
        BlackBox b1 = new BlackBox();
        // 객체가 가지고 있는 인스턴스 변수에 각각 접근하여 설정할 수 있음
        b1.modelName = "퐁퐁이";
        b1.resolution = "FHD";
        b1.price = 200000;
        b1.color = "블랙";

        System.out.println(b1.modelName);
        System.out.println(b1.resolution);
        System.out.println(b1.price);
        System.out.println(b1.color);

        System.out.println("-----------");

        // 새로운 블랙박스 제품
        BlackBox b2 = new BlackBox();
        b2.modelName = "퐁퐁";
        b2.resolution = "UHD";
        b2.price = 300000;
        b2.color = "화이트";

        System.out.println(b2.modelName);
        System.out.println(b2.resolution);
        System.out.println(b2.price);
        System.out.println(b2.color);
    }
}
