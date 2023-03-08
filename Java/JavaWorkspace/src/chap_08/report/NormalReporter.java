package chap_08.report;

// NormalReporter 클래스는 report 라는 기능을 할 수 있다.
// 인터페이스를 상속 받을땐 implements 를 사용
public class NormalReporter implements Reportable {
    @Override
    public void report() {
        System.out.println("일반 화재 신고를 진행합니다.");
    }
}
