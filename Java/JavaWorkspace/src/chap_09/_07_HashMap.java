package chap_09;

import java.util.HashMap;

public class _07_HashMap {
    public static void main(String[] args) {
        // 맵 (Key, Value)
        HashMap<String, Integer> map = new HashMap<>();

        // 데이터 추가
        map.put("유재석", 10);
        map.put("박명수", 5);
        map.put("김종국", 3);
        map.put("서장훈", 15);

        System.out.println("총 고객 수 : " + map.size());
        System.out.println("-------------");

        // 조회
        System.out.println("유재석님의 포인트 : " + map.get("유재석"));
        System.out.println("유재석님의 포인트 : " + map.get("박명수"));
        System.out.println("-------------");

        // 키의 값을 확인하고 값을 추가 없다면 키를 추가
        if (map.containsKey("서장훈")) {
            int point = map.get("서장훈");
            map.put("서장훈", ++point);
            System.out.println("서장훈의 누적 포인트 : " + map.get("서장훈"));
        } else {
            map.put("서장훈", 1);
            System.out.println("서장훈 신규 등록 (포인트 1)");
        }
        System.out.println("-------------");

        // 삭제
        map.remove("유재석");
        System.out.println(map.get("유재석"));
        System.out.println("-------------");

        // 전체삭제
        map.clear();
        if (map.isEmpty()) {
            System.out.println("남은 고객 수 : " + map.size());
        }
        System.out.println("--------------");

        map.put("유재석", 10);
        map.put("박명수", 5);
        map.put("김종국", 3);
        map.put("서장훈", 15);

        // Key 확인
        for (String key : map.keySet()) {
            System.out.println(key);
        }
        System.out.println("--------------");

        // Value 확인
        for (int value : map.values()) {
            System.out.println(value);
        }
        System.out.println("--------------");

        // Key, Value 함께 확인
        for (String key : map.keySet()) {
            System.out.println("고객 이름 : " + key + " \t포인트 : " + map.get(key));
        }
        System.out.println("--------------");

        // Map : 중복 X, 순서 X
        // 맨 마지막걸로 업데이트
        map.put("김종국", 10);
        map.put("김종국", 30);
        map.put("김종국", 50);
        System.out.println(map.get("김종국"));

        // 순서를 보장 받고 싶으면 LinkedHashMap 사용
    }
}
