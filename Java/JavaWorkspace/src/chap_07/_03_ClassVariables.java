package chap_07;

public class _03_ClassVariables {
    public static void main(String[] args) {
        BlackBox b1 = new BlackBox();
        b1.modelName = "퐁퐁이";
        System.out.println(b1.modelName);

        BlackBox b2 = new BlackBox();
        b2.modelName = "펑펑이";
        System.out.println(b2.modelName);

        // 특정 범위를 초과하는 충동 감지 시 자동 신고 기능 개발 여부
        System.out.println(" - 개발 전 -");
        System.out.println(b1.modelName + " 자동 신고 기능 : " + b1.canAutoReport);
        System.out.println(b2.modelName + " 자동 신고 기능 : " + b2.canAutoReport);
        // 클래스변수에 접근 할때에는 일반적으로 클래스명 + 클래스변수명 으로 접근
        System.out.println("모든 블랙박스 제품 자동 신고 기능 : " + BlackBox.canAutoReport );

        // 기능 개발
        BlackBox.canAutoReport = true;
        System.out.println(" - 개발 후 -");
        System.out.println(b1.modelName + " 자동 신고 기능 : " + b1.canAutoReport);
        System.out.println(b2.modelName + " 자동 신고 기능 : " + b2.canAutoReport);
        System.out.println("모든 블랙박스 제품 자동 신고 기능 : " + BlackBox.canAutoReport );

    }
}
