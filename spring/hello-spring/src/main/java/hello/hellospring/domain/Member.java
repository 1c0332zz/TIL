package hello.hellospring.domain;

public class Member {

    private Long id; // 시스템에서 정하는 ID 값
    private String name; // 그냥 이름

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }



}
