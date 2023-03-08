package chap_07.camera;

// FactoryCam is a Camera (Is-A)
public class FactoryCam extends Camera { // 자식 클래스
    public FactoryCam() {
        //this.name = "공장 카메라";
        // super() = 부모클래스의 생성자에 바로 접근
        super("공장 카메라");
    }

    public void recordVideo() {
        // super
        // 부모 클래스에 있는 기능을 그대로 쓰면서 그 후에 추가적인 기능을 사용하겠다는 명시
        super.recordVideo();
        detectFire();
    }

    public void detectFire() {
        // 화재 감지
        System.out.println("화재를 감지합니다.");
    }

    // 메소드 오버라이딩
    public void showMainFeature() {
        System.out.println(this.name + "의 주요 기능 : 화재 감지");
    }
}
