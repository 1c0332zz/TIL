package chap_07;
// 클래스를 이용해 햄버거를 자동으로 만드는 클래스 작성

// 햄버거, 치즈버거, 새우버거
// 각 버거는 각각의 클래스로 생성
// 버거 이름을 담기 위한 name 변수 정의
// 재료 정보를 표시하는 cook() 메소드 정의
// 공통 부분은 상속 및 메소드 오버라이딩으로 처리
public class _Quiz_07 {
    public static void main(String[] args) {
        HamBurger[] hamBurgers = new HamBurger[3];
        hamBurgers[0] = new HamBurger();
        hamBurgers[1] = new CheeseBurger();
        hamBurgers[2] = new ShrimpBurger();

        System.out.println("주문하신 메뉴를 만듭니다.");
        System.out.println("-----------");
        for (HamBurger hamBurger : hamBurgers) {
            hamBurger.cook();
            System.out.println("-----------");
        }
        System.out.println("메뉴 준비가 완료되었습니다.");

    }
}

class HamBurger {
    public String name;

    // String name 에 값을 정의해주는 생성자
    // main 메소드의 ()속에 아무것도 값을 받지 않으니 이것이 호출댐
    public HamBurger() {
        this("햄버거");
    }

    // 위에있는 생성자가 호출됨
    public HamBurger(String name) {
        this.name = name;
    }

    public void cook() {
        System.out.println(this.name + "를 만듭니다.");
        System.out.println("빵 사이에 들어가는 재료는?");
        System.out.println("> 양상추");
        System.out.println("+ 패티");
        System.out.println("+ 피클");
    }
}

class CheeseBurger extends HamBurger{

    // 부모 클래스에 있는 생성자에 값을 받아서 업데이트
    public CheeseBurger() {
        super("치즈버거");
    }
    public void cook() {
        super.cook();
        System.out.println("+ 치즈");
    }
}

class ShrimpBurger extends HamBurger{
    public ShrimpBurger() {
        super("새우버거");
    }
    public void cook() {
        super.cook();
        System.out.println("+ 새우");
    }
}