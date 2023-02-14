// 메인 클래스
public class Main {
  // 메인 메서드
  public static void main(String[] args) {
    // 변수 선언, 변수 할당 = > 변수 초기화
    int x = 10;
    int y = 5;

    // 수정가능 시작
    int z = x;
    x = y;
    y = z;
    // 수정가능 끝

    System.out.println("x : " + x); // x : 10
    // 출력 => x : 5
    System.out.println("y : " + y); // y : 5
    // 출력 => y : 10


    // int x = 10; << 이건 불가능, 중복선언 불가능
    // 변수 재활용
    // x = 10;
  }
}