package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.List;
import java.util.Optional;

public interface MemberRepository {
    Member save(Member member); // 저장소에 저장되는 기능
    Optional<Member> findById(Long id); // 저장된 아이디를 불러와줌
    Optional<Member> findByName(String name); // 저장된 네임을 불러와줌
    List<Member> findAll(); // findAll 하면 저장된 모든 회원 리스트를 가져옴
}
