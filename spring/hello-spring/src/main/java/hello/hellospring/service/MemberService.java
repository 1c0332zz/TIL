package hello.hellospring.service;
// 서비스는 회원 리포지토리와 도메인을 활용해서 비지니스 로직을 작성하는 구간

import hello.hellospring.domain.Member;
import hello.hellospring.repository.MemberRepository;
import hello.hellospring.repository.MemoryMemberRepository;

import java.util.List;
import java.util.Optional;

public class MemberService {
    public final MemberRepository memberRepository;

    public MemberService(MemberRepository memberRepository) {
        this.memberRepository = memberRepository;
    }


    /**
     * 회원 가입
     */
    public long join(Member member) {
        // 중복 회원 검증 코드를 작성 후 메소드로 변경시킴.
//        Optional<Member> result = memberRepository.findByName(member.getName()); // Optional 로 감싸면 Optional 안에 멤버 객체가 들어있음
//        result.ifPresent(m -> { // ifPresent -> 이미 있는 값이면 이 아래가 동작함(Optional 이기에 가능)
//            throw new IllegalStateException("이미 존재하는 회원입니다.");
//        });

        validateDuplicateMember(member);    // 중복 회원 검증
        memberRepository.save(member);      // 통과하면 저장
        return member.getId();
    }

    private void validateDuplicateMember(Member member) { // 중복회원 검증 메소드
        memberRepository.findByName(member.getName())
                .ifPresent(m -> {
                    throw new IllegalStateException("이미 존재하는 회원입니다.");
                });
    }

    /**
     * 전체 회원 조회
     */
    public List<Member> findMembers() {
        return memberRepository.findAll();
    }

    public Optional<Member> findOne(Long memberId) {
        return memberRepository.findById(memberId);
    }
}
