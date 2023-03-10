package chap_10_;

public class _01_AnonymousClass1 {
    public static void main(String[] args) {
        // 익명 클래스
        // 똑같은 클래스는 이용하지만, 어떤 기능을 추가로 확장할 때 (객체 하나만을 위한 1회성)
        Coffee c1 = new Coffee();
        c1.order("아메리카노");
        System.out.println("-------------");

        Coffee c2 = new Coffee();
        c2.order("라떼");
        System.out.println("-------------");

        // 친한 친구 방문
        Coffee specialCoffee = new Coffee() {
            @Override
            public void order(String coffee) {
                // 부모클래스의 오더 메소드 호출
                super.order(coffee);
                System.out.println("(귓속말) 딸기 케이크는 서비스예요");
            }

            @Override
            public void returnTray() {
                // 부모 클래스를 지우고 재정의
                System.out.println("(귓속말) 자리에 두시면 제가 치울께요~");
            }
        };
        specialCoffee.order("바닐라 라떼");
        specialCoffee.returnTray();
    }
}

class Coffee {
    public void order(String coffee) {
        System.out.println("주문하신 " + coffee + " 나왔습니다.");
    }

    public void returnTray() {
        System.out.println("커피 반납이 완료되었습니다.");
    }
}