package chap_10_;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;
import java.util.stream.Stream;

public class _05_Stream {
    public static void main(String[] args) {
        // 스트림 => 데이터가 흐른다
        // 스트림 생성

        // Arrays.stream 을 이용하는 방법
        int[] scores = {100, 95, 90 ,85, 80};
        IntStream scoreStream = Arrays.stream(scores);

        String[] langs = {"python", "java", "javascript", "c", "c++", "c#"};
        Stream<String> langStream = Arrays.stream(langs);

        // Collection.stream() 을 이용하는 방법
        List<String> langList = new ArrayList<>();
        // langList.add("python");
        // langList.add("java"); 이렇게 하는 대신
        langList = Arrays.asList("python", "java", "javascript", "c", "c++", "c#"); // 이렇게 집어넣을 수 있다.
        // System.out.println(langList.size());
        Stream<String> langListStream = langList.stream();

        // of 로 만들 수 있음
        Stream<String> langListOfStream = Stream.of("python", "java", "javascript", "c", "c++", "c#");

        // 스트림 사용
        // 중간 연산(Intermediate Operation) => 정수기의 필터? / filter, map, sorted, distinct, skip, ....
        // 최종 연산(Terminal Operation) => 필터를 통해서 최종적으로 나오는 결과물 / count, min, max, sum, forEach, anyMatch, allMatch, ....

        // 90 점 이상인 점수만 출력
        Arrays.stream(scores).filter(x -> x >= 90).forEach(x -> System.out.println(x));
        Arrays.stream(scores).filter(x -> x >= 90).forEach(System.out::println);
        System.out.println("-------------------");

        // 90 점 이상인 사람의 수
        int count = (int) Arrays.stream(scores).filter(x -> x >= 90).count(); // count 는 long 이라 int 로 변환해주든가 long 으로 저장해줘야함.
        System.out.println(count);
        System.out.println("-------------------");

        int sum = Arrays.stream(scores).filter(x -> x >= 90).sum();
        System.out.println(sum);
        System.out.println("-------------------");

        // 90 점 이상인 점수를 정렬
        Arrays.stream(scores).filter(x -> x >= 90).sorted().forEach(System.out::println);
        System.out.println("-------------------");

        // 문자열
        // "python", "java", "javascript", "c", "c++", "c#"
        // c 로 시작하는 프로그래밍 언어
        Arrays.stream(langs).filter(x -> x.startsWith("c")).forEach(System.out::println);
        System.out.println("-------------------");

        // java 라는 글자를 포함하는 언어
        Arrays.stream(langs).filter(x -> x.contains("java")).forEach(System.out::println);
        System.out.println("-------------------");

        // 4글자 이하인 언어를 정렬해서 출력 (Collection.stream())
        langList.stream().filter(x -> x.length() <= 4).sorted().forEach(System.out::println);
        System.out.println("-------------------");

        // 4글자 이하의 언어중에서 c라는 글자를 포함하는 언어
        langList.stream()
                .filter(x -> x.length() <= 4)
                .filter(x -> x.contains("c"))
                .forEach(System.out::println);
        System.out.println("-------------------");

        // 4글자 이하의 언어중에서 c라는 글자를 포함하는 언어가 하나라도 있는지?
        boolean anyMatch = langList.stream()
                .filter(x -> x.length() <= 4)
                .anyMatch(x -> x.contains("c")); // anyMatch 은 boolean 으로 표현
        System.out.println(anyMatch);
        System.out.println("-------------------");

        // 4글자 이하의 언어들은 모두 c라는 글자를 포함하는 언어인지?
        boolean allMatch = langList.stream()
                .filter(x -> x.length() <= 3)
                .allMatch(x -> x.contains("c")); // allMatch 은 boolean 으로 표현
        System.out.println(allMatch);
        System.out.println("-------------------");

        // 4글자 이하의 언어 중에서 c라는 글자를 포함하는 언어뒤에 (어려워요) 라는 글자를 함께 출력
        // map => 원하는 데이터를 가공하거나 꺼내고 싶은 인스턴스 변수를 지정
        langList.stream()
                .filter(x -> x.length() <= 4)
                .filter(x -> x.contains("c"))
                .map(x -> x + " (어려워요)")
                .forEach(System.out::println);
        System.out.println("-------------------");

        // c 라는 글자를 포함하는 언어를 대문자로 출력
        langList.stream()
                .filter(x -> x.contains("c"))
                .map(String::toUpperCase)
                .forEach(System.out::println);
        System.out.println("-------------------");

        // c 라는 글자를 포함하는 언어를 대문자로 변경하여 리스트로 저장
        List<String> langListStartsWithC = langList.stream()
                .filter(x -> x.contains("c"))
                .map(String::toUpperCase)
                .collect(Collectors.toList());

        langListStartsWithC.stream().forEach(System.out::println);
    }
}
