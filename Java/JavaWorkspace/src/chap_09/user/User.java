package chap_09.user;

public class User {
    // 사용자의 이름
    public String name;

    // 사용자 이름의 생성자
    public User(String name) {
        this.name = name;
    }

    // 커피 주문시 포인트 적립 문구
    public void addPoint() {
        System.out.println(this.name + "님, 포인트 적립되었습니다.");
    }
}
