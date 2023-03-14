package hello.hellospring.service;

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.Optional;

import static org.assertj.core.api.Assertions.*;
import static org.junit.jupiter.api.Assertions.*;

// Test 의 기본
// given => 무언가를 주어졌는데
// when => 이걸 실행했을때
// then => 이게 나와야함

class MemberServiceTest {

    MemberService memberService;
    MemoryMemberRepository memberRepository;

    @BeforeEach
    public void beforeEach() { // 테스트를 독립적으로 실행하기 위해 DI 사용
        memberRepository = new MemoryMemberRepository();
        memberService = new MemberService(memberRepository);
    }

    @AfterEach
    public void afterEach() {
        memberRepository.clearStore();
    }

    @Test
    void 회원가입() {
        // given => 무언가를 주어졌는데
        Member member = new Member();
        member.setName("hello"); // 맴버에 hello 라는 이름이 저장함

        // when => 이걸 실행했을때
        long saveId = memberService.join(member); // join 을 검증 => 회원정보를 저장하고 저장한 아이디를 반환받음

        // then => 이게 나와야함
        // 우리가 검증하려는게 db에 있는지 확인을 해야하니까 repository 를 꺼내야함
        Member findMember = memberService.findOne(saveId).get(); // 반환받은 ID 를 repository 에 있는 id 로 반환받고 findMember에 저장
        assertThat(member.getName()).isEqualTo(findMember.getName()); // 이름이 일치하는지 확인
    }

    @Test
    public void 중복_회원_예외() {
        // given => 무언가를 주어졌는데
        Member member1 = new Member();
        member1.setName("spring");

        Member member2 = new Member();
        member2.setName("spring");

        // when => 이걸 실행했을때
        memberService.join(member1);
        IllegalStateException e = assertThrows(IllegalStateException.class, () -> memberService.join(member2));
        // () -> memberService.join(member2) 이 로직을 실행 할건데 IllegalStateException 이 예외가 터져야해.

        // 메세지를 검증하려면 e로 변수를 지정하고 아래와 같이 작성.
        assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");

        // try 문으로 실행법
/*        try {
            memberService.join(member2);
            fail();
        } catch (IllegalStateException e) {
            assertThat(e.getMessage()).isEqualTo("이미 존재하는 회원입니다.");
        }*/

        // then => 이게 나와야함
    }

    @Test
    void findMembers() {
    }

    @Test
    void findOne() {
    }
}