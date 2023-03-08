package chap_07;

import chap_07.camera.Camera;
import chap_07.camera.SpeedCam;

public class _16_Reference {
    public static void main(String[] args) {
        // 참조
        // 기본 자료형 (Primitive Data Types) : int, float, double, long, boolean, ...
        // 기본 자료형은 메소드가 없음
        // 기본 자료형은 소문자로 시작함
        // 공간 3개를 만드는 int 자료형 배열
        int[] i = new int[3];
        System.out.println(i[0]); // 0

        double[] d = new double[3];
        System.out.println(d[0]); // 0.0

        boolean[] b_ = new boolean[3];
        System.out.println(b_[0]); // false

        // 참조 자료형 (Non-Primitive, Reference Data Types) : String, 사용자정의로 클래스로 만들어진 객체 (Camera, FactoryCam)
        // 참조 자료형은 메소드를 가질 수 있음
        // 참조 자료형은 대문자로 시작함
        String[] s = new String[3];
        System.out.println(s[0]); // null

        Camera[] c = new Camera[3];
        System.out.println(c[0] == null); // true

        ///////////////////////////////
        System.out.println("--------------");
        int a = 10;
        int b = 20;
        b = a;
        System.out.println(a);
        System.out.println(b);
        b = 30;
        System.out.println(a);
        System.out.println(b);

        System.out.println("--------------");
        Camera c1 = new Camera();
        Camera c2 = new Camera();
        c1.name = "카메라1";
        c2.name = "카메라2";
        System.out.println(c1.name);
        System.out.println(c2.name);
        c2 = c1;
        System.out.println(c1.name);
        System.out.println(c2.name);
        c2.name = "고장난 카메라";
        System.out.println(c1.name);
        System.out.println(c2.name);
        System.out.println("--------------");
        changeName(c2); // 여기서 아래 메소드로 전달값을 전달해주고 잘못된 카메라로 이름이 바뀜
        System.out.println(c1.name);
        System.out.println(c2.name);

        c2 = null;
        System.out.println(c2.name);
    }

    public static void changeName(Camera camera) {
        camera.name = "잘못된 카메라";
    }
}
