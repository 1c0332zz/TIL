package chap_09.user;

public class VIPUser extends User {
    public VIPUser(String name) {
        super("특별한 " + name); // super 를 이용해 부모클래스의 이름을 호출
    }
}
