package chap_09.coffee;
// 정해진 타입의 객체만 받겠다.

import chap_09.user.User;


public class CoffeeByUser <T extends User> { // 어떠한 타입이 오든 상관없지만 반드시 User 란 클래스를 상속하는 T여야 함
    // User, VIPUser 만 받을 수 있음
    public T user;

    public CoffeeByUser(T user) {
        this.user = user;
    }

    public void ready() {
        System.out.println("커피 준비 완료 : " + user.name);
        user.addPoint();
    }
}
