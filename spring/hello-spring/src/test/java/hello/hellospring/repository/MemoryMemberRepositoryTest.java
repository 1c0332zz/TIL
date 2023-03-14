package hello.hellospring.repository;

import hello.hellospring.domain.Member;
import org.assertj.core.api.Assertions;
import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.Test;

import java.util.List;

import static org.assertj.core.api.Assertions.*;

public class MemoryMemberRepositoryTest {
    // 테스트는 서로 순서와 관계없이 실행됨
    // 테스트 주도 개발 (TDD)
    MemoryMemberRepository repository = new MemoryMemberRepository();

    @AfterEach // 메소드가 끝날 때 마다 이걸 실행 (콜백)
    public void afterEach() { // 하나의 테스트가 끝날때 마다 지워줘야함
        repository.clearStore();
    }

    @Test
    public void save(){
        Member member = new Member();
        member.setName("spring"); // 내가 저장한 이름

        repository.save(member);

        Member result = repository.findById(member.getId()).get(); // 내가 꺼낸 이름
        // System.out.println("result = " + (result == member)); // 저장한거랑 맴버랑 같은지
        // Assertions.assertEquals(member, result); // 저장한거랑 맴버랑 같은지
        assertThat(member).isEqualTo(result); // member 가 result 랑 같은지 => import static org.assertj.core.api.Assertions.*; 해줘야함
    }

    @Test
    public void findByName() {
        Member member1 = new Member(); // 이렇게 3줄 치면 스프링1 이라는 회원이 가입이 된거임
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        Member result = repository.findByName("spring1").get(); // spring1 을 꺼내서 result 에 저장

        assertThat(result).isEqualTo(member1); // result 랑 member1 이랑 같은지 확인

    }

    @Test
    public void findAll() {
        Member member1 = new Member();
        member1.setName("spring1");
        repository.save(member1);

        Member member2 = new Member();
        member2.setName("spring2");
        repository.save(member2);

        List<Member> result = repository.findAll();

        assertThat(result.size()).isEqualTo(2);
    }
}
