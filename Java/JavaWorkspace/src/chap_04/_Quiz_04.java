package chap_04;
// 조건문을 활용해 주차 요금 정산 프로그램을 작성

// -- 조건 --
// 1. 주차요금은 시간당 4,000원 (일일 최대 요금은 30,000원)
// 2. 경차 또는 장애인 차량은 최종 요금에서 50% 할인 (장애인 차량: 직접 운전 또는 탑승 모두 포함)

// 예시
// 일반 차량 5시간 주차 시 20,000원
// 경차 5시간 주차 시 10,000원
// 장애인차량 10시간 주차 시 15,000원

// 실행결과 : 주차 요금은 xx 원 입니다.
public class _Quiz_04 {
    public static void main(String[] args) {
        int hour = 10; // 주차 시간
        boolean isSmallCar = false; // 경차 여부
        boolean withDisabledPerson = true; // 장애인 차량 여부

        int fee = hour * 4000; // 주차 정산 요금 (시간당 4,000원 곱하기)

        // 30,000원 초과 시 일일 최대 요금으로 수정
        if (fee > 30000) {
            fee = 30000; // 일일 최대 요금 적용
        }

        //경차 또는 장애인 차량인 경우 50% 할인
        if (isSmallCar || withDisabledPerson) {
            fee *= 0.5f; // 50% 할인 적용
        }
        System.out.println("주차 요금은 " + fee + "원 입니다.");
    }
}
