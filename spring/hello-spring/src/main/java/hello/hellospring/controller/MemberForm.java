package hello.hellospring.controller;

public class MemberForm {
    private String name; // createMemberForm.html 의 name 이랑 매칭이 됨

    public String getName() {
        return name; // getName 으로 꺼내면댐
    }

    public void setName(String name) {
        this.name = name; // 여기에 name 저장 됨
    }


}
