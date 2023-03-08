package chap_07;

import chap_07.camera.FactoryCam;
import chap_07.camera.SpeedCam;

public class _15_Super {
    public static void main(String[] args) {
        // Super
        FactoryCam factoryCam = new FactoryCam();
        SpeedCam speedCam = new SpeedCam();

        factoryCam.recordVideo();
        System.out.println("----------");
        speedCam.takePicture();
    }
}