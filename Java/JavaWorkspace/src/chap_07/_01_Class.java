package chap_07;

public class _01_Class {
    public static void main(String[] args) {
        // 객체 지향 프로그래밍 (OOP : Object-Oriented Programming)
        // 유지보수 용이
        // 높은 재사용성

        // 차량용 블랙박스로 예시
        // 모델명, 해상도, 가격, 색상

        // 첫 번째 제품
        String modelName = "퐁퐁이";
        String resolution = "FHD";
        int price = 200000;
        String color = "블랙";

        // 두 번째 제품
        String modelName2 = "퐁퐁삼";
        String resolution2 = "UHD";
        int price2 = 300000;
        String color2 = "화이트";

        // 또 다른 제품을 개발?

        // 객체를 만드는 과정
        // 클래스명 객체이름 = NEW 클래스명();
        BlackBox bbox = new BlackBox();
        // BlackBox 클래스로부터 bbox 객체 생성
        // bbox 객체에는 BlackBox 클래스의 인스턴스

        BlackBox bbox2 = new BlackBox();
    }
}
