package chap_09;

import java.util.HashSet;

public class _06_HashSet {
    public static void main(String[] args) {
        // 세트
        // 중복값을 허용하지 않음
        // 순서는 무작위
        HashSet<String> set = new HashSet<>();

        // 데이터 추가
        set.add("삼겹살");
        set.add("쌈장");
        set.add("음료");
        set.add("소금");
        set.add("후추");
        set.add("삼겹살");
        set.add("깻잎");
        set.add("상추");
        set.add("삼겹살");
        set.add("밥");

        System.out.println("총 구매 상품 수 : " + set.size());

        // 순회
        for (String s : set) {
            System.out.println(s);
        }
        System.out.println("-------------");

        // 확인
        if (set.contains("삼겹살")) {
            System.out.println("삼겹살 사러 출발");
        } else {
            System.out.println("안사도댐");
        }
        System.out.println("-------------");

        // 삭제
        System.out.println("삼겹살 구매 전 : " + set.size());
        set.remove("삼겹살");
        System.out.println("삼겹살 구매 후 : " + set.size());
        System.out.println("-------------");

        // 전체 삭제
        set.clear();
        if (set.isEmpty()) {
            System.out.println("남은 구매 상품 수 : " + set.size());
        }
        System.out.println("-------------");

        // 순서 뒤죽박죽이니 순서를 맞추고 싶고 중복도 제거하고 싶다면 LinkedHashSet 을 사용
        HashSet<Integer> intSet = new HashSet<>();
        intSet.add(1);
        intSet.add(9);
        intSet.add(5);

        for (int i : intSet) {
            System.out.println(i);
        }
    }
}
