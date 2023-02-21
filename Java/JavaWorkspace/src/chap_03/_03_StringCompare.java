package chap_03;

public class _03_StringCompare {
    public static void main(String[] args) {
        // 문자열 비교
        String s1 = "Java";
        String s2 = "Python";

        System.out.println(s1.equals(s2)); // 문자열 내용이 같으면 true, 다르면 false
        System.out.println(s1.equals("Java")); // 문자열 내용이 같으면 true, 다르면 false
        System.out.println(s2.equals("python")); // 문자열 내용이 같으면 true, 다르면 false (대소문자 구분)
        System.out.println(s2.equalsIgnoreCase("python")); // 대소문자 구분 없이 같으면 true, 다르면 false

        // 문자열 비교 심화
        // 한개의 메모리에 저장해놓고 s1과 s2가 참조한다.
        s1 = "1234";
        s2 = "1234";
        System.out.println(s1.equals(s2)); // true (문자열 그 자체) / 내용을 비교
        System.out.println(s1 == s2); // true (문자열이 저장되어 있는 데이터의 위치) / 참조하는 곳의 위치가 같은지

        // new String을 통해서 만들면 서로 다른 데이터에 저장됨.
        s1 = new String("1234");
        s2 = new String("1234");
        System.out.println(s1.equals(s2)); // true
        System.out.println(s1 == s2); // false
    }
}
