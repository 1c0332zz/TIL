package chap_05;

public class _02_ArrayLoop {
    public static void main(String[] args) {
        // 배열의 순회
        String[] coffees = { "아메리카노", "카페모카", "라떼", "카푸치노"};

        // for 반복문 순회
        for (int i = 0; i < 4; i++) {
            System.out.println(coffees[i] + "하나");
        }

        System.out.println("------------");

        // 배열의 길이를 이용한 순회
        for (int i = 0; i < coffees.length; i++) {
            System.out.println(coffees[i] + " 하나");
        }

        System.out.println("------------");

        // enhanced for (for-each) 반복문 / foreach
        for (String coffee :
                coffees) {
            System.out.println(coffee + " 하나");
        }

        // 인덱스의 값을 가지고 처리해야 될 상황이면 fori
        // 모든요소를 다 순회하면서 작업해야 할 상황이면 foreach
    }
}
