package chap_07;

public class _08_Constructor {
    public static void main(String[] args) {
        // 생성자 = 객체가 만들어 질때 자동으로 호출해 주는 메소드
        BlackBox b1 = new BlackBox();
        b1.modelName = "퐁퐁이";
        b1.resolution = "FUD";
        b1.price = 20000;
        b1.color = "블랙";
        System.out.println(b1.modelName);
        System.out.println(b1.serialNumber);

        System.out.println("-------------------");

        // 생성자를 활용한 호출
        BlackBox b2 = new BlackBox("팡팡이", "UHD", 300000, "화이트");
        System.out.println(b2.modelName);
//        System.out.println(b2.resolution);
//        System.out.println(b2.price);
//        System.out.println(b2.color);
        System.out.println(b2.serialNumber);
    }
}
