package chap_07;

import chap_07.camera.ActionCam;
import chap_07.camera.SlowActionCam;

public class _17_Final {
    public static void main(String[] args) {
        // Final

        // public (final) class .... = 클래스
        // public (final) void .... = 메소드
        // 순서 public > abstract > static > final > ....

        // 클래스, 메소드, 변수를 선언과 동시에 초기화를 하고 그 이후에 변경(상속) 불가
        ActionCam actionCam = new ActionCam();
        // actionCam.lens = "표준렌즈"; 이렇게 변경하지 못하게 만들려면 클래스에서  Final
        actionCam.recordVideo();
        actionCam.makeVideo();

        System.out.println("------------------");

        SlowActionCam slowActionCam = new SlowActionCam();
        // slowActionCam.recordVideo();
        slowActionCam.makeVideo();
    }
}
