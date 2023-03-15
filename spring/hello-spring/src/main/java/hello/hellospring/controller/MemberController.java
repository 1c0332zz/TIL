package hello.hellospring.controller;
// Controller 가 서비스를 통해서 회원가입과 조회를 할 수 있어야함
// 의존관계
import hello.hellospring.domain.Member;
import hello.hellospring.service.MemberService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;

import java.util.List;

@Controller // 컨트롤러 역할을 하는 클래스에 지정
public class MemberController {

    private final MemberService memberService;

    @Autowired // 디펜젼시 인젝션, 의존관계
    public MemberController(MemberService memberService) {
        this.memberService = memberService;
    }

    @GetMapping("/members/new") // members/new 의 URL 이 들어오면 members/createMemberForm 으로 찾아서 보내줌.
    public String createForm() {
        return "members/createMemberForm";
    }

    @PostMapping("/members/new") // 회원가입 Form 에서 일로 넘어와짐
    public String create(MemberForm form) { // MemberForm 클래스의 name 을 받아옴
        Member member = new Member();
        member.setName(form.getName()); // MemberForm 에서 받아온 name 을 getName 으로 꺼내서 member 의 setName 으로 저장시킴.

        System.out.println("member = " + member.getName());

        memberService.join(member); // join 을 통해서 중복이 없는지 확인 후 가입함.

        return "redirect:/";
    }

    @GetMapping("/members")
    public String list(Model model) {
        List<Member> members = memberService.findMembers();
        model.addAttribute("members", members); // K, V
        return "members/memberList";

    }
}
