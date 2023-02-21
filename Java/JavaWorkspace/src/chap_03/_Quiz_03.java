package chap_03;
// 주민등록번호에서 생년월일 및 성별까지만 출력하는 프로그램을 작성하시오.
public class _Quiz_03 {
    public static void main(String[] args) {
        String id1 = "901231-1234567";
        String id2 = "030708-4567890";

        System.out.println(id1.substring(0, 8)); // 0 위치부터 8 위치 직전까지
        System.out.println(id2.substring(0, id2.indexOf("-") + 2)); // 0 위치부터 하이픈 위치 + 2 직전까지
    }
}
