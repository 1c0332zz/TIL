package chap_10_.converter;

// 인터페이스엔 추상메소드가 2개이상 있으면 안됌
@FunctionalInterface
public interface Convertible {
    void convert(int USD);
}
