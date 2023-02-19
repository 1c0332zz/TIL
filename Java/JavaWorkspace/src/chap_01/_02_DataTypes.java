package chap_01;

public class _02_DataTypes {
  public static void main(String[] args) {
        // 정수
        System.out.println("== 정수형 데이터 타입 ==");
        byte by = 127; // 1byte, -128 ~ 127
        System.out.printf("by : %d\n", by);
        System.out.println("byte :" + Byte.BYTES);

        short s = 32767; // 2byte, -32768 ~ 32767
        System.out.printf("s : %d\n", s);
        System.out.println("Short : " + Short.BYTES);

        int i = 2147483647; // 4byte, -2147483648 ~ 2147483647
        System.out.printf("i : %d\n", i);
        System.out.println("int : " + Integer.BYTES);

        long l = 9223372036854775807l; // 8byte, -9223372036854775808 ~ 9223372036854775807
        System.out.printf("l : %d\n", l);
        System.out.println("long : " + Long.BYTES);

        // 실수
        System.out.println("== 실수형 데이터 타입 ==");
        float f = 3.141592653589793f; // 4byte
        System.out.print("f : " + f + "\n");
        System.out.println("float : " + Float.BYTES);

        double d = 3.141592653589793; // 4byte
        System.out.print("d : " + d + "\n");
        System.out.println("double : " + Double.BYTES);

        // 논리
        System.out.println("== 논리형 데이터 타입 ==");
        boolean bool1 = true;
        boolean bool2 = false;
        System.out.println(bool1);
        System.out.println(bool2);

        //문장(문자열, " 사용)
        System.out.println("== 문장형 데이터 타입 ==");
        String str = "안녕하세요.";
        System.out.println(str);

        // 문자(한 글자, ' 사용)
        System.out.println("== 문자형 데이터 타입 ==");
        char c = '낢'; // 2byte
        System.out.println(c);
  }
}
