package chap_09;

import chap_09.coffee.*;
import chap_09.user.User;
import chap_09.user.VIPUser;

public class _02_GenericClass {
    public static void main(String[] args) {
        // 제네릭 클래스

        // 번호표로 불러주는 손님 (정수형)
        CoffeeByNumber c1 = new CoffeeByNumber(33);
        c1.ready();

        // 닉네임으로 불러주는 손님 (문자형)
        CoffeeByNickname c2 = new CoffeeByNickname("송강섭");
        c2.ready();

        System.out.println("---------------");

        // Object 로 클래스를 생성해서 문자열이든 정수형이든 받을 수 있음
        CoffeeByName c3 = new CoffeeByName(34);
        c3.ready();

        CoffeeByName c4 = new CoffeeByName("송강식");
        c4.ready();

        System.out.println("---------------");

        // 이름으로 주문 고객 번호를 찾을려면
        // int c3Name = c3.name; 인트로 형 변환 해야함
        int c3Name = (int) c3.name;
        System.out.println("주문 고객 번호 : " + c3Name);

        String c4Name = (String) c4.name;
        System.out.println("주문 고객 번호 : " + c4Name);

        // c4Name = (String) c3.name; // c3.name 을 c4.name 으로 형 변환 과정에서 에러 발생

        System.out.println("---------------");
        // 제네릭클래스 사용
        // 코드의 중복을 없앰
        // 형변환 없음
        // 정해진 타입의 데이터만 사용
        Coffee<Integer> c5 = new Coffee<>(35);
        c5.ready();
        int c5Name = c5.name;
        System.out.println("주문 고객 번호 : " + c5Name);

        Coffee<String> c6 = new Coffee<>("성창현");
        c6.ready();
        String c6name = c6.name;
        System.out.println("주문 고객 번호 : " + c6name);

        c6name = String.valueOf(c5Name);
        System.out.println(c6name);

        System.out.println("---------------");
        // User
        // 퐁퐁이라는 이름을 가진 객체를 만들고 그 객체를 CoffeeByUser 에 집어 넣어 c7 을 수행
        CoffeeByUser<User> c7 = new CoffeeByUser<>(new User("퐁퐁이"));
        c7.ready();

        CoffeeByUser<User> c8 = new CoffeeByUser<>(new VIPUser("팡팡이"));
        c8.ready();

        // BlackBox 는 User 를 상속받는 클래스가 아니기 떄문에 사용 X
        // CoffeeByUser<User> c9 = new CoffeeByUser<>(new BlackBox());

        System.out.println("---------------");
        // 값을 2개 이상 받을 때
        orderCoffee("팡팡이"); //
        orderCoffee("퐁퐁이", "아이스 아메리카노");
        orderCoffee(38, "라떼");
    }
    // 1개 받을 때
    public static <T> void orderCoffee(T name) {
        System.out.println("커피 주문 완료 : " + name);
    }

    // 2개 이상 받을 떄
    public static <T, V> void orderCoffee(T name, V coffee) {
        System.out.println(coffee + " 주문 완료 : " + name);
    }
}

class BlackBox {
}