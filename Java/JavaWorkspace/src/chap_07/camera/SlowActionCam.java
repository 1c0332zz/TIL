package chap_07.camera;

public class SlowActionCam{
    public String name;
    public SlowActionCam() {
        this.name = "슬로우 액션 카메라"; // Camera 에 접근해서 직접 이름 설정
    }

    public void makeVideo() {
        System.out.println("자체 개발한 슬로우 비디오 제작 기능");
    }

//    public void makeVideo() { // 부모 클래스가 final 설정을 하여 변경할 수 없음
//        System.out.println(this.name + " : " +  this.lens
//                + "로 촬영한 영상을 통해 멋진 슬로우모드 비디오를 제작합니다.");
//    }
}
