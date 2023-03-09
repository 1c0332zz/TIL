package chap_09;

public class _01_Generics {
    public static void main(String[] args) {
        // 제네릭스
        // 다양한 타입의 객체를 지원하는 클래스나 인터페이스, 메소드를 정의하는 방법
        // 기본자료형은 제네릭스로 바로 사용할 수 없음

        Integer[] iArray = {1, 2, 3, 4, 5};
        Double[] dArray = {1.0, 2.0, 3.0, 4.0, 5.0};
        String[] sArray = {"A", "B", "C", "D", "E"};
        
        printIntArray(iArray);
        printDoubleArray(dArray);
        printStringArray(sArray);

        System.out.println("------------");

        printAnyArray(iArray);
        printAnyArray(dArray);
        printAnyArray(sArray);
    }

    // 제네릭스를 이용한 방법
    // 서로 다른 타입이 들어가도 다 출력해 줄 수 있는 제네릭
    // T : Type
    private static <T> void printAnyArray(T[] array) {
        for (T t :
                array) {
            System.out.print(t + " ");
        }
        System.out.println();
    }

    // -----이 아래 클래스는 타입만 다르고 중복된 코드
    private static void printStringArray(String[] sArray) {
        for (String s :
                sArray) {
            System.out.print(s + " ");
        }
        System.out.println();
    }

    private static void printDoubleArray(Double[] dArray) {
        for (double d :
                dArray) {
            System.out.print(d + " ");
        }
        System.out.println();
    }

    private static void printIntArray(Integer[] iArray) {
        for (int i :
                iArray) {
            System.out.print(i + " "); // 1 2 3 4 5
        }
        System.out.println();
    }
}