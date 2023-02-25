package chap_05;

public class _05_ASCII {
    public static void main(String[] args) {
        // 아스키 코드 (ANSI) : 미국 표준 코드
        char c = 'A'; // 알파벳 대문자는 65 부터 시작, 소문자는 97 부터 시작, 숫자(0)는 48 부터 시작.
        System.out.println(c);
        System.out.println((int)c);

        c = 'B';
        System.out.println(c);
        System.out.println((int)c);

        // 연산을 통해서도 계산이 가능
        c++;
        System.out.println(c);
        System.out.println((int)c);

        // _04_에서 수기로 작성했던 알파벳 순서도 아스키코드를 활용해 연산 가능
        // 세로 크기 10 * 가로 크기 15 에 해당하는 영화관 좌석
        String[][] seats3 = new String[10][15];
        char ch = 'A';
        for (int i = 0; i < seats3.length; i++) { // 세로
            for (int j = 0; j < seats3[i].length; j++) { // 가로
                seats3[i][j] = String.valueOf(ch) + (j + 1);
            }
            ch++;
        }

        // 영화관 좌석 번호 확인
        for (int i = 0; i < seats3.length; i++) { // 세로 / seats2.length 로 하면 seats2의 세로 값
            for (int j = 0; j < seats3[i].length; j++) { // 가로 / seats2[i].length 로 하면 seats2[i]의 가로 값
                System.out.print(seats3[i][j] + " "); // 좌표 = 세로 * 가로
            }
            System.out.println();
        }
    }
}
