package chap_08.camera;

public abstract class Camera { // abstract 키워드를 통해 카메라라는 추상 클래스를 만듦
    public void takePicture() {
        System.out.println("사진을 촬영합니다.");
    }

    public void recordVideo() {
        System.out.println("동영상을 녹화합니다.");
    }

    // 추상메소드 정의
    // 일반적으로 만드는 클래스의 메소드는 바디부분을 { }로 정의해 주었지만
    // 추상메소드는 () 후 바로 ;로 끝맺음
    // Camera 클래스를 상속하는 자식클래스에서 구현해야 하는 메소드
    public abstract void showMainFeature();
}
