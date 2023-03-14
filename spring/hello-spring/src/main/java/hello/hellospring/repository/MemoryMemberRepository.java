package hello.hellospring.repository;

import hello.hellospring.domain.Member;

import java.util.*;

public class MemoryMemberRepository implements MemberRepository {

    private static Map<Long, Member> store = new HashMap<>();
    private static long sequence = 0L; // 0, 1, 2 ... Key 값 생성

    @Override
    public Member save(Member member) {
        member.setId(++sequence); // member 에 id 값을 셋팅해줌 (이름은 세이브하기전에 넘어옴)
        store.put(member.getId(), member); // store 에 저장함
        return member; // 결과 반환
    }

    @Override
    public Optional<Member> findById(Long id) {
        return Optional.ofNullable(store.get(id)); // null 값 안주게 반환
    }

    @Override
    public Optional<Member> findByName(String name) {
        return store.values().stream() // 네임이 있을때 까지 계속 찾음
                .filter(member -> member.getName().equals(name))
                .findAny();
    }

    @Override
    public List<Member> findAll() {
        return new ArrayList<>(store.values());
    }
}
