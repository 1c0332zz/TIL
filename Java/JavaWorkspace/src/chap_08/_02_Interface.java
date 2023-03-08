package chap_08;

import chap_08.camera.FactoryCam;
import chap_08.detector.AdvancedFireDetector;
import chap_08.detector.Detectable;
import chap_08.detector.FireDetector;
import chap_08.report.NormalReporter;
import chap_08.report.Reportable;
import chap_08.report.VideoReporter;

public class _02_Interface {
    public static void main(String[] args) {
        // 인터페이스
        // 뼈대만 제공하는 구조
        Reportable normalReporter = new NormalReporter();
        normalReporter.report();

        Reportable videoReporter = new VideoReporter();
        videoReporter.report();

        System.out.println("-----인스턴스의 클래스에서 직접 접근해 사용------");

        Detectable fireDetector = new FireDetector();
        fireDetector.detect();

        Detectable advancedFireDetector = new AdvancedFireDetector();
        advancedFireDetector.detect();

        System.out.println("-----인터페이스 변수를 클래스에서 사용-----");
        FactoryCam factoryCam = new FactoryCam();
        factoryCam.setDetector(fireDetector);
        factoryCam.setReporter(normalReporter);

        factoryCam.detect();
        factoryCam.report();
    }
}
