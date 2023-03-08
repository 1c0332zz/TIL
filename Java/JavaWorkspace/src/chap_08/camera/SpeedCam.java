package chap_08.camera;

public class SpeedCam extends Camera{
    @Override
    public void showMainFeature() {
        System.out.println("속도 측정, 번호 인식");
    }

    public void detect() {
        System.out.println("사고를 감지합니다.");
    }

    public void report() {
        System.out.println("사고 신고를 진행합니다.");
    }
}
// detect, report 가 FactoryCam 이랑 겹침.
// 코드의 중복을 없애야 할 떈, 인터페이스를 활용
