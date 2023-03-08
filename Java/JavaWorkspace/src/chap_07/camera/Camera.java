package chap_07.camera;

public class Camera { // 부모 클래스
    public String name;

    public Camera() {
        this("카메라");
    }

    protected Camera(String name) { // 이름 클래스를 전달받아 생성
        this.name = name;
    }

    public void takePicture() {
        // 사진 촬영
        System.out.println(this.name + " : 사진을 촬영합니다.");
    }

    public void recordVideo() {
        // 동영상 녹화
        System.out.println(this.name + " : 동영상을 녹화합니다.");
    }

    // 메소드 오버라이딩
    public void showMainFeature() {
        System.out.println(this.name + "의 주요 기능 : 사진 촬영, 동영상 녹화");
    }
}
