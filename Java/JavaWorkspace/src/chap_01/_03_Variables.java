package chap_01;

public class _03_Variables {
    public static void main(String[] args) {
        // 정수형
        System.out.println("== 정수형 데이터 타입 ==");
        byte by = 127;  // 1byte = 8bit -> 값의 범위 : -128 ~ 127
        System.out.println("by : " + by);
        System.out.println("byte : " + Byte.BYTES);

        short s = 32767; // 2byte = 16bit ->  값의 범위 :  -32768 ~ 32767
        System.out.println("s : " + s);
        System.out.println("Short : " + Short.BYTES);

        int a = 2147483647; // 4byte = 32bit -> 값의 범위 : -2147483648 ~ 214748364
        System.out.println("a : " + a);
        System.out.println("int : " + Integer.BYTES);

        long l = 9223372036854775807L; // 8byte = 64bit -> 값의 범위 :  -9223372036854775808 ~ 9223372036854775807
        System.out.println("l : " + l);
        System.out.println("long : " + Long.BYTES);

        // 실수형
        System.out.println("== 실수형 데이터 타입 ==");
        float f = 3.141592653589793f; // 4byte
        System.out.println("f : " + f);
        System.out.println("float : " + Float.BYTES);

        double d = 3.141592653589793; // 8byte
        System.out.println("d : " + d);
        System.out.println("double : " + Double.BYTES);

        System.out.println("== 논리형 데이터 타입 ==");
        boolean bool1 = true;
        boolean bool2 = false;
        System.out.println(bool1);
        System.out.println(bool2);

        System.out.println("== 문장형 데이터 타입 ==");
        String str = "안녕하세요.";
        System.out.println(str);

        System.out.println("== 문자형 데이터 타입 ==");
        char c = 'H';
        System.out.println(c);
    }
}
