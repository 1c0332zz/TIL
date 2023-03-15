package hello.hellospring.controller;
// Controller 가 서비스를 통해서 회원가입과 조회를 할 수 있어야함
// 의존관계
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;

@Controller // 컨트롤러 역할을 하는 클래스에 지정
public class MemberController {

    private final MemberService memberService;

    @Autowired // 디펜젼시 인젝션, 의존관계
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }
}
