package chap_07;

public class _04_Method {
    public static void main(String[] args) {
        BlackBox b1 = new BlackBox();
        b1.modelName = "퐁퐁이";

        // 클래스 내에 기능을 정의해 객체가 사용하게 할 수도 있음 = 메소드
        b1.autoReport(); // 지원 안됨
        BlackBox.canAutoReport = true;
        b1.autoReport();

        // 전달값과 반환값이 있는 메소드
        b1.insertMemoryCard(256);

        // 일반 영상 : 1 (type)
        // 이벤트 영상 (충돌 감지) : 2 (type)
        int fileCount = b1.getVideoFileCount(1); // 일반 영상
        System.out.println("일반 영상 파일 수 " + fileCount + "개");

        System.out.println("이벤트 영상 파일 수 " + b1.getVideoFileCount(2) + "개"); // 이벤트 영상
    }
}
