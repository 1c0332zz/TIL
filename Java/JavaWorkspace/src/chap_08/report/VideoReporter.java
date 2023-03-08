package chap_08.report;

public class VideoReporter implements Reportable {
    @Override
    public void report() {
        System.out.println("진적 30초 영상과 함께 신고를 진행합니다.");
    }
}
