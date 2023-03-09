package chap_09;

import java.util.*;

public class _08_Iterator {
    public static void main(String[] args) {
        // 이터레이터
        // List 는 인터페이스
        // ArrayList 는 클래스인데 List 라는 인터페이스를 구현 하고 있음 (LinkedList 도 똑같음)
        // 다형성에 의해서 리스트로 객체 생성 가능
        // List<String> list2 = new LinkedList<>();

        List<String> list = new ArrayList<>();
        list.add("유재석");
        list.add("(알 수 없음)");
        list.add("김종국");
        list.add("(알 수 없음)");
        list.add("강호동");
        list.add("(알 수 없음)");
        list.add("박명수");
        list.add("(알 수 없음)");
        list.add("조세호");

        for (String s : list) {
            System.out.println(s);
        }
        System.out.println("----------------------");

        // 이터레이터를 통해 값을 가지고옴 (list.iterator() 입력 후 Ctrl + Alt + v 하면 자동 생성)
        Iterator<String> it = list.iterator();
        // 커서 현재 List<String> list = new ArrayList<>(); 이걸 가리키고 있고 next 를 통해 유재석을 가르키도록 함
        System.out.println(it.next()); // 유재석
        System.out.println(it.next()); // (알 수 없음)
        System.out.println(it.next()); // 김종국
        System.out.println(it.next()); // (알 수 없음)
        System.out.println("----------------------");

        it = list.iterator(); // 커서를 처음 위치로 이동
        // 순회는 hasNext 를 통해 사용
        while (it.hasNext()) {
            System.out.println(it.next());
        }
        System.out.println("----------------------");

        // 쓸모 없는 값을 순회로 지운 후 출력
        it = list.iterator(); // 커서를 처음 위치로 이동
        while (it.hasNext()) {
            String s = it.next();
            if (s.contains("(알 수 없음)")) {
                it.remove(); // 삭제
            } else {
                System.out.println(s);
            }
        }
        System.out.println("----------------------");

        // HashSet 으로도 가능
        HashSet<String> set = new HashSet<>();
        set.add("유재석");
        set.add("박명수");
        Iterator<String> itSet = set.iterator();
        while (itSet.hasNext()) {
            System.out.println(itSet.next());
        }
        System.out.println("----------------------");

        // Map 으로도 가능
        HashMap<String, Integer> map = new HashMap<>();
        map.put("유재석", 10);
        map.put("박명수", 5);
        map.put("김종국", 3);
        map.put("서장훈", 15);

        // map.iterator 는 제공되지 않음.
        // KEy 로 접근
        Iterator<String> itMapKey = map.keySet().iterator();
        while (itMapKey.hasNext()) {
            System.out.println(itMapKey.next());
        }
        System.out.println("----------------------");

        // Value 로 접근
        Iterator<Integer> itMapValue = map.values().iterator();
        while (itMapValue.hasNext()) {
            System.out.println(itMapValue.next());
        }
        System.out.println("----------------------");

        // Key 와 Value 함께 출력
        Iterator<Map.Entry<String, Integer>> itMap = map.entrySet().iterator();
        while (itMap.hasNext()) {
            System.out.println(itMap.next());
        }
    }
}
