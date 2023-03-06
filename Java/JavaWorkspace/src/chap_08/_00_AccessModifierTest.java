package chap_08;

import chap_07.BlackBoxRefurbish;

public class _00_AccessModifierTest {
    public static void main(String[] args) {
        BlackBoxRefurbish b1 = new BlackBoxRefurbish();
        b1.modelName = "까망이"; // public 이여서 다른 패키지에서도 접근 가능
        // b1.resolution = "FHD"; // default 여서 다른 패키지에서 접근이 불가능
        // b1.price = 200000; // private 같은 클래스가 아니여서 접근 불가능
        // b1.color = "화이트" // protected 자식 클래스가 아니여서 접근 불가능
    }
}
