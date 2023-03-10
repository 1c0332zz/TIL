package chap_10_;
// 수제버거 만들기
// 똑같은 추상클래스를 상속받지만 다 같은내용이 아니고 그때그때 새로운 익명클래스를 생성해 반환
public class _02_AnonymousClass2 {
    public static void main(String[] args) {
        // _01_에서 했던거와 달리 아래에서 정의할 수 있음
        HomeMadeBurger momMadeBurger = getMomMadeBurger();
        momMadeBurger.cook();
        System.out.println("-----------------");

        // 다른햄버거 만들기
        // 똑같은 추상클래스를 사용
        HomeMadeBurger broMadeBurger = getBroMadeBurger();
        broMadeBurger.cook();
    }

    private static HomeMadeBurger getBroMadeBurger() {
        return new HomeMadeBurger() {
            @Override
            public void cook() {
                System.out.println("집에서 만든 동생표 군대리아");
                System.out.println("재료 : 빵, 패티, 양배추 샐러드, 딸기쨈, 치즈, 삶은 계란");
            }
        };
    }


    // 이 익명 클래스는 아래의 추상클래스를 상속 받아 정의함
    public static HomeMadeBurger getMomMadeBurger() {
        return new HomeMadeBurger() {
            @Override
            public void cook() {
                System.out.println("집에서 만드는 엄마표 수제 버거");
                System.out.println("재료 : 빵, 패티, 해쉬브라운, 양상추, 마요네즈");
            }
        };
    }
}

// 추상클래스 = 바로 객체를 만들 수 없고 상속 받은 후 재정의 해야함
abstract class HomeMadeBurger {
    public abstract void cook();
}