package chap_07;

public class BlackBox {
    // 4개의 인스턴스 변수 or 필드
    // 인스턴스 변수는 서로 다른 객체에서 서로 다른값을 가질 수 있다.
    String modelName; // 모델명
    String resolution; // 해상도
    int price; // 가격
    String color; // 색상

    // static 을 붙이면 클래스 변수가 됨
    // 클래스 변수는 클래스로 만들어지는 모든 객체에 똑같이 적용됨
    static boolean canAutoReport = false; // 자동 신고 기능

    // 클래스 내에 기능을 정의해 객체가 사용하게 할 수도 있음 = 메소드
    void autoReport() {
        if (canAutoReport) {
            System.out.println("충돌이 감지되어 자동으로 신고합니다.");
        }
        else {
            System.out.println("자동 신고 기능이 지원되지 않습니다.");
        }

    }
    // 메모리가 삽입되었을때 전달값을 주는 메소드
    void insertMemoryCard(int capacity) {
        System.out.println("메모리 카드가 삽입되었습니다.");
        System.out.println("용량은 " + capacity + "GB 입니다." );
    }

    // 블랙박스 장치 내에 저장되어 있는 영상 개수를 반환하는 메소드
    // 충돌영상, 이벤트영상 분리
    int getVideoFileCount(int type) {
        if (type == 1) { // 일반 영상
            return 9;
        }
        else if (type == 2) { // 이벤트 영상
            return 1;
        }
        return 10;
    }

    // showDateTime : 날짜정보 표시여부
    // showSpeed : 속도정보 표시여부
    // min : 영상 기록 단위(분)
    // 블랙박스 화면에 보이는 여러 기능
    void record(boolean showDateTime, boolean showSpeed, int min) {
        System.out.println("녹화를 시작합니다.");
        if (showDateTime) {
            System.out.println("영상에 날짜 정보가 표시 됩니다.");
        }
        if (showSpeed) {
            System.out.println("영상에 속도정보가 표시됩니다.");
        }
        System.out.println("영상은 " + min + "분 단위로 기록됩니다.");
    }

    // 메소드 오버로딩
    // 위에 record 메소드를 호출해 사용해 기본값으로 설정할 수 있음
    void record() {
        record(true, true, 5);
    }

    // 고객센터 메소드
    // 모든 객체에 공통으로 적용
    static void callServiceCenter() {
        System.out.println("서비스 센터(1588-0000) 로 연결합니다.");
        // modelName = "test";
        // 클래스변수 안에서 인스턴스 변수는 수정 불가능 / 객체가 만들어져야 만들어지기 때문

        boolean canAutoReport = false;
        // 스테틱으로 선언한 클래스 변수는 접근 가능
    }
}
