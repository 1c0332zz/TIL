package chap_07;

public class _18_Enum {
    public static void main(String[] args) {
        // 열거형 (Enum)
        // 상수들의 묶음
        // 달력 : JAN, FEB, MAR, ...
        // 옷 사이즈 : S, M, L, XL ...
        // OS 종류 : Window, OS, LINUX ...

        Resolution resolution = Resolution.HD;
        System.out.println(resolution); // HD

        resolution = Resolution.FHD;
        System.out.println(resolution); // FHD

        System.out.print("동영상 녹화 품질 : ");
        switch (resolution) {
            case HD:
                System.out.println("일반 화질");
                break;
            case FHD:
                System.out.println("고화질");
                break;
            case UHD:
                System.out.println("초고화질");
                break;
        }
        // 문자열로 부터 불러오기
        resolution = Resolution.valueOf("UHD");
        System.out.println(resolution);

        System.out.println("------------------");

        // 반복문을 이용해 나열하기
        for (Resolution myRes : Resolution.values()) {
            System.out.println(myRes.name() + " : " + myRes.ordinal());
        }

        System.out.println("------------------");

        // 상수가 가진 진짜 값
        for (Resolution myRes :
                Resolution.values()) {
            System.out.println(myRes.name() + " : " + myRes.getWidth());
        }
    }
}

enum Resolution {
    HD(1280), FHD(1920), UHD(3840);

    private final int width;
    Resolution(int width) {
        this.width = width;
    }

    public int getWidth() {
        return width;
    }

}