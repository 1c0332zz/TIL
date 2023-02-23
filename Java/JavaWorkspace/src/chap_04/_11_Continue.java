package chap_04;

public class _11_Continue {
    public static void main(String[] args) {
        // Continue

        // 치킨 주문 손님중에 노쇼 손님이 있다고 가정
        int max = 20; // 최대 치킨 판매 수량
        int sold = 0; // 현재 치킨 판매 수량
        int noShow = 17; // 노쇼 고객

        for (int i = 1; i <= 50; i++) {
            System.out.println(i + "번 고객님 주문하신 치킨 나왔습니다.");

            // 손님이 없다면 ? (noShow)
            if (i == noShow) {
                System.out.println(i + "고객님 노쇼로 다음분에게 드리겠씁니다.");
                continue; // 이 아래코드는 실행하지 않고 다시 위로 올라감.
            }
            sold++; // 판매 처리

            if (sold == max) {
                System.out.println("금일 재료가 모두 소진되었습니다.");
                break;
            }
        }
        System.out.println("영업 종료");

        System.out.println("---While---");
        // While 문
        sold = 0;
        int index = 0; // 손님 번호
        while (true) {
            index++;
            System.out.println(index + "번 고객님 주문하신 치킨 나왔습니다.");
            // 손님이 없다면 ? (noShow)
            if (index == noShow) {
                System.out.println(index + "고객님 노쇼로 다음분에게 드리겠씁니다.");
                continue;
            }
            sold++;
            if (sold == max) {
                System.out.println("금일 재료가 모두 소진되었습니다.");
                break;
            }
        }
        System.out.println("영업 종료");
    }
}
