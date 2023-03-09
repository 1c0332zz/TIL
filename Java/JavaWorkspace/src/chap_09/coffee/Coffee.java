package chap_09.coffee;
// 제너릭 클래스
// 타입이 뭐든 상관없음
public class Coffee <T> {
    public T name;

    public Coffee(T name) {
        this.name = name;
    }

    public void ready() {
        System.out.println("커피 준비 완료 : " + name);
    }
}
