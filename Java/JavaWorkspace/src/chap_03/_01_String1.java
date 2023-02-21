package chap_03;

public class _01_String1 {
    public static void main(String[] args) {
        String s = "I like Java and Python and C.";
        System.out.println(s);

        // 문자열의 길이 len
        System.out.println(s.length()); // 29

        // 대소문자 변환 upper
        System.out.println(s.toUpperCase()); // 대문자로
        System.out.println(s.toLowerCase()); // 소문자로

        // 포함 관계
        System.out.println(s.contains("Java")); // 포함된다면 true
        System.out.println(s.contains("C#")); // 포함되지 않으면 false
        System.out.println(s.indexOf("Java")); // 위치 정보
        System.out.println(s.indexOf("C#")); // 포함되지 않으면 -1
        System.out.println(s.indexOf("and")); // 12 / 처음 만나는 위치 정보
        System.out.println(s.lastIndexOf("and")); // 23 / 마지막에 만나는 위치 정보
        System.out.println(s.startsWith("I like")); // 이걸로 시작하면 ture (아니면 false)
        System.out.println(s.endsWith(".")); // 이걸로 시작하면 ture (아니면 false)
    }
}
