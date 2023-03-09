package chap_09.coffee;

public class CoffeeByName {
    // 오브젝트로 이름을 받아도 다른곳에서 값을 꺼내려 할 때, 항상 형 변환이 필요함.
    // 형 변환을 잘 못하게 되면은 에러가 발생할 위험
    // 이떄 사용하는게 제너릭클래스 (Coffee)
    public Object name; // Object 이기 때문에 Integer, Double, String 등 다 집어넣을 수 있음

    public CoffeeByName(Object name) {
        this.name = name;
    }

    public void ready() {
        System.out.println("커피 준비 완료 : " + name);
    }
}
