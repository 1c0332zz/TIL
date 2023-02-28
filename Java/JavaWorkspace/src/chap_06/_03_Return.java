package chap_06;

public class _03_Return {
    // 호텔 전화번호
    // void 는 반환값이 없을 때 사용
    public static String getPhoneNumber() {
        String phoneNumber = "02-1234-5678";
        return phoneNumber;
    }
    // 호텔 주소
    public static String getAddress() {
        return "하남시 어디쯤";
    }
    // 호텔 액티비티
    public static String getActivities() {
        return "볼링장, 탁구장, 노래방";
    }
    public static void main(String[] args) {
        // 반환값, Return
        String contactNumber = getPhoneNumber();
        System.out.println("호텔 전화번호 : " + contactNumber);

        String address = getAddress();
        System.out.println("호텔 주소 : " + address);

        // 리턴값을 변수에 저장하지 않고 불러오는 법
        System.out.println("호텔 액티비티 :" + getActivities());
    }
}
