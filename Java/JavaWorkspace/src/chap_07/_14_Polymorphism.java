package chap_07;

import chap_07.camera.Camera;
import chap_07.camera.FactoryCam;
import chap_07.camera.SpeedCam;

public class _14_Polymorphism {
    public static void main(String[] args) {
        // 다형성

        // class Person : 사람
        // class Student extends Person : 학생 (학생은 사람이다. Student is a person)
        // class Teacher extends Person : 선생님 (선생님은 사람이다. Teacher is a person)

        // 이건 상속관계
//        Camera camera = new Camera();
//        FactoryCam factoryCam = new FactoryCam();
//        SpeedCam speedCam = new SpeedCam();

        // 이건 다형성
        Camera camera = new Camera();
        Camera factoryCam = new FactoryCam();
        Camera speedCam = new SpeedCam();

        camera.showMainFeature();
        factoryCam.showMainFeature();
        speedCam.showMainFeature();

        System.out.println("-----반복문으로 showMainFeature객체 불러오기-----");

        Camera[] cameras = new Camera[3];
        cameras[0] = new Camera();
        cameras[1] = new FactoryCam();
        cameras[2] = new SpeedCam();

        for (Camera cam:
             cameras) {
            cam.showMainFeature();
        }

        System.out.println("-----instanceof-----");

        // 문제점
        // 자식클래스에 있는 메소드를 사용하지 못함.
//        factoryCam.detectFire();
//        speedCam.checkSpeed();
//        speedCam.recognizeLicensePlate();

        // instanceof = 이 객체가 어떤 클래스의 인스턴스인지 확인하는 키워드
        // if (객체 instanceof 클래스) => 객체가 클래스의 인스턴스인지 확인
        if (camera instanceof Camera) {
            System.out.println("카메라입니다.");
        }

        if (factoryCam instanceof FactoryCam) {
            // factoryCam.detectFire(); 이걸로 원래 클래스를 제공 받았지만 다형성을 사용하면 형변환을 해야함
            // ((형변환 하려는 클래스)객체).메소드
            ((FactoryCam)factoryCam).detectFire();
        }

        if (speedCam instanceof SpeedCam) {
            ((SpeedCam) speedCam).checkSpeed();
            ((SpeedCam) speedCam).recognizeLicensePlate();
        }

        // 자바에는 Object 라는 최상위 클래스가 존재
        // 어떤 형태던 모든 클래스 객체를 넣을 수 있음
        Object[] objs = new Object[3];
        objs[0] = new Camera();
        objs[1] = new FactoryCam();
        objs[2] = new SpeedCam();

    }
}
