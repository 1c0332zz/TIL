package chap_10_.converter;

public class KRWConverter implements Convertible{
    @Override
    public void convert(int USD) {
        // 1 달러 = 1300 원
        System.out.println(USD + "달러 = " + (USD * 1300) + " 원");
    }
}
