package chap_06;

public class _08_MainMethod {
    // 전달값 주는법
    // 실행 왼쪽 현재파일에 구성편집 -> + 버튼 클릭 -> 애플리케이션 -> 메인 클래스 선택 -> 프로그램 인수에 값 작성
    public static void main(String[] args) {
        // 반환값은 void 라서 없음.
        // 전달값은 String[] args 라는 배열 => 문자열배열
        for (String s : args) {
            System.out.println(s);
        }

        // 1. 도서 조회
        // 2. 도서 대출
        // 3. 도서 반납
        if (args.length == 1) {
            switch (args[0]) {
                case "1":
                    System.out.println("도서 조회 메뉴입니다.");
                    break;
                case "2":
                    System.out.println("도서 대출 메뉴입니다.");
                    break;
                case "3":
                    System.out.println("도서 반납 메뉴입니다.");
                default:
                    System.out.println("잘못 입력 하였습니다.");
            }
        } else {
            System.out.println("사용법) 1~3 메뉴 중 하나를 입력하세요.");
        }
    }
}
