package chap_09;

import java.util.Collections;
import java.util.LinkedList;

public class _05_LinkedList {
    public static void main(String[] args) {
        // 링크드 리스트
        LinkedList<String> list = new LinkedList<>();

        // 데이터 추가
        list.add("유재석");
        list.add("조세호");
        list.add("김종국");
        list.add("박명수");
        list.add("강호동");

        // 데이터 조회 (인덱스)
        System.out.println(list.get(0));
        System.out.println(list.get(1));
        System.out.println(list.getFirst());
        System.out.println(list.getLast());

        System.out.println("---------------");

        // 추가
        list.addFirst("서장훈"); // 맨 첫번째로 넣음
        for (String s :
                list) {
            System.out.println(s);
        }

        System.out.println("---------------");

        list.addLast("김희철"); // 맨 마지막에 넣음
        for (String s :
                list) {
            System.out.println(s);
        }

        // 지정하는 인덱스 위치에 값 추가
        list.add(1, "김영철"); // 1번자리에 "김영철"
        System.out.println(list);

        // 삭제
        list.remove(list.size() - 1); // 마지막 삭제

        list.removeFirst(); // 0번째 삭제
        list.removeLast(); // 마지막 삭제
        for (String s : list) {
            System.out.println(s);
        }

        System.out.println("---------------");

        // 인덱스 변경
        list.set(0, "이수근");
        System.out.println(list.get(0));

        // 확인
        System.out.println(list.indexOf("김종국")); // 몇번째 인덱스인지
        if (list.contains("김종국")) {
            System.out.println("있음");
        } else {
            System.out.println("없음");
        }

        System.out.println("---------------");

        // 전체 삭제
        list.clear();
        if (list.isEmpty()) {
            System.out.println("학생 수 : " + list.size());
            System.out.println("없음");
        }

        System.out.println("---------------");

        // 데이터 추가
        list.add("유재석");
        list.add("조세호");
        list.add("김종국");
        list.add("박명수");
        list.add("강호동");

        Collections.sort(list); // 정렬
        for (String s : list) {
            System.out.println(s);
        }

        System.out.println("---------------");

    }
}
