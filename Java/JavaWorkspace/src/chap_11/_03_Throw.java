package chap_11;

public class _03_Throw {
    public static void main(String[] args) {
        // 의도적으로 에러 만들기
        int age = 17;
        try {
            if (age < 19) {
                // System.out.println("만 19세 미만에게는 판매하지 않습니다.");
                // 예외를 던지다
                throw new Exception("만 19세 미만에게는 판매하지 않습니다.");
            } else {
                System.out.println("주문하신 상품입니다.");
            }
        } catch (Exception e) { // throw 에서 던진 예외를 여기서 잡음
            e.printStackTrace();
        }
    }
}
