package chap_07.camera;

public final class ActionCam extends Camera{ // 다른클래스가 나를 상속해서 기능을 확장하길 원하지 않는 경우 final
    // 값을 선언과 동시에 할 수도 있지만, 선언만 해두고 생성자 내에서 초기화 할 수도 있다.
    public final String lens; // = "광각렌즈";

    // 생성자
    // 객체가 만들어지는 시점에 호출 되기 때문에
    public ActionCam() {
        super("액션 카메라");
        lens = "광각렌즈";
    }

    public final void makeVideo() { // final 을 쓰면 자식클래스에서 오버라이딩을 할 수 없음
        System.out.println(this.name + " : " +  this.lens + "로 촬영한 영상을 통해 멋진 비디오를 제작합니다.");
    }

}
