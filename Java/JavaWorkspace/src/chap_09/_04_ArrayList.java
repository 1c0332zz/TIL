package chap_09;

import java.util.ArrayList;
import java.util.Collections;

public class _04_ArrayList {
    public static void main(String[] args) {
        // 컬렉션 프레임워크 (List(ArrayList, LinkedList), Set, Map)
        // 다수의 데이터를 쉽고 효과적으로 처리할 수 있는 표준화된 방법을 제공하는 클래스의 집합

        // list 라는 이름의 문자열데이터를 보관 할 수 있는 ArrayList가 만들어짐
        ArrayList<String> list = new ArrayList<>();

        // 데이터 추가
        list.add("유재석");
        list.add("조세호");
        list.add("김종국");
        list.add("박명수");
        list.add("강호동");

        // 데이터 조회
        System.out.println(list);
        System.out.println(list.get(0));
        System.out.println(list.get(1));
        System.out.println(list.get(2));
        System.out.println(list.get(3));
        System.out.println(list.get(4));

        System.out.println("-----------------");

        // 삭제 (박명수)
        System.out.println("학생 수 : " + list.size());
        list.remove("박명수");
        System.out.println("학생 수 : " + list.size());
        System.out.println(list.get(3));

        System.out.println("-----------------");

        System.out.println("학생 수 : " + list.size()); // 4
        list.remove(list.size() - 1); // 마지막 것을 지울려면 - 1 하면 됨
        System.out.println("학생 수 : " + list.size()); // 3

        System.out.println("-----------------");

        // 순회
        for (String i:
             list) {
            System.out.println(i);
        }

        System.out.println("-----------------");

        // 데이터 변경
        System.out.println("양도 전 : " + list.get(0));
        list.set(0, "이수근");
        System.out.println("양도 전 : " + list.get(0));

        System.out.println("-----------------");

        // 포함이 되어있는지 확인
        System.out.println(list.indexOf("김종국")); // 몇번째에 있는지

        if (list.contains("김종국")) {
            System.out.println("수강 신청 선공");
        } else {
            System.out.println("수강 신청 실패");
        }

        System.out.println("-----------------");

        // 전체 삭제
        list.clear();
        // isEmpty = 없으면 true
        if (list.isEmpty()) {
            System.out.println("삭제 완료 : " + list.size());
        } else {
            System.out.println("남았음");
        }

        // 데이터 새로 추가 후 정렬
        list.add("유재석");
        list.add("조세호");
        list.add("김종국");
        list.add("박명수");
        list.add("강호동");

        // 정렬
        Collections.sort(list);
        for (String s : list) {
            System.out.println(s);
        }
    }
}
