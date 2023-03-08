package chap_08.camera;

import chap_08.detector.Detectable;
import chap_08.report.Reportable;

// 인터페이스를 구현하는 팩토리캠으로 변경
// 인스턴스 변수로
public class FactoryCam extends Camera implements Detectable, Reportable {
    public Detectable detector; // 인터페이스 변수로 인스턴스 변수를 생성
    public Reportable reporter; // 인스턴스 변수 생성 후 Alt + ins 를 통해 set 생성 후 오버라이딩 된 detect, report 에 해당 변수를 호출

    public void setDetector(Detectable detector) { // setter 를 통해서 외부에서 보내주는 객체를 적용해 detector 의 기능을 그대로 쓸 수 있음
        this.detector = detector;
    }

    public void setReporter(Reportable reporter) {
        this.reporter = reporter;
    }


    @Override
    public void showMainFeature() {
        System.out.println("화재 감지");
    }

    @Override
    public void detect() {
        detector.detect();
    }

    @Override
    public void report() {
        reporter.report();
    }
    // 중복된 메소드는 인터페이스로 대체
//    public void detect() {
//        System.out.println("화재를 감지합니다.");
//    }
//
//    public void report() {
//        System.out.println("화재 신고를 진행합니다.");
//    }
}
// detect, report 가 FactoryCam 이랑 겹침.
// 코드의 중복을 없애야 할 떈, 인터페이스를 활용
