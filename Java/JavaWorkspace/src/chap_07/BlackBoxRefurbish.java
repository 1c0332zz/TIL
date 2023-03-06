package chap_07;

public class BlackBoxRefurbish {
    // public 은 어디서든지 접근 가능
    public String modelName; // 모델명
    // default 는 아무것도 안적어도 기본으로 설정
    String resolution; // 해상도
    // 앞에 private 을 사용하면 BlackBoxRefurbish 이라는 클래스 내에서만 접근이 가능
    private int price; // 가격
    protected String color; // 색상

    // Getter & Setter 쉽게 생성하는 법
    // 코드 -> 생성 -> Getter & Setter
    public String getModelName() {
        return modelName;
    }

    public void setModelName(String modelName) {
        this.modelName = modelName;
    }

    public String getResolution() {
        if (resolution == null || resolution.isEmpty()) { // isEmpty = "" << 빈공간일때 true
            return "판매자에게 문의하세요";
        }
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        if (price < 100000) {
            this.price = 100000;
        }
        else {
            this.price = price;
        }
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
}

