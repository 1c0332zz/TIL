package chap_11;

public class _02_Catch {
    public static void main(String[] args) {
        try {
             // System.out.println(3 / 0);// 시도하려는 소스 코드

//             int[] arr = new int[3];
//             arr[5] = 100;
//
//            Object obj = "test";
//            System.out.println((int) obj);
            String s = null;
            System.out.println(s.toLowerCase());
            // 예외가 중복되면 | 로 2개 이상 설정 가능
        } catch (ArithmeticException | ArrayIndexOutOfBoundsException e) { // "ArithmeticException" 이라는 오류가 발생해서 그걸 넣어줌
            System.out.println("뭔가 실수 하셨네요.");
//        } catch (ArrayIndexOutOfBoundsException e) { // "ArrayIndexOutOfBoundsException" 라는 오류가 발생하면 실행
//            System.out.println("뭔가 실수 하셨네요.");
        } catch (ClassCastException e) {
            System.out.println("잘못된 형 변환 입니다."); // "ClassCastException" 잘못된 형 변환의 오류문
        } catch (Exception e) { // Exception => 모든 예외들의 조상 클래스
            System.out.println("그 외의 모든 에러는 여기서 처리가 됩니다."); // 문제에 대한 처리
            e.printStackTrace();
        }

        System.out.println("프로그램 정상 종류");
    }
}
