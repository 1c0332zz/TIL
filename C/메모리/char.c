#include <stdio.h>

int main(void)
{
    char *s = "EMMA";
    printf("%s\n", s); // EMMA

    // 주소를 출력하려면 %p를 사용
    printf("%p\n", s); // 00405064

    //이렇게 출력하면 각 char에 해당하는 주소를 가져옴
    // 1바이트씩 차이
    printf("%p\n", &s[0]); // 00405064
    printf("%p\n", &s[1]); // 00405065
    printf("%p\n", &s[2]); // 00405066
    printf("%p\n", &s[3]); // 00405067

    // 한단어만 출력하려면 %c로 해당하는 인덱스
    printf("%c\n", s[0]); // E
    printf("%c\n", s[1]); // M
    printf("%c\n", s[2]); // M
    printf("%c\n", s[3]); // A

    // [0]방법의 인덱스로 접근해도 컴퓨터가 ()로 변경해주기 때문
    // 이런방법으로도 가능 (구문 설탕) *s는 s의 주소로 가달라는 의미
    printf("%c\n", *s);       // E
    printf("%c\n", *(s + 1)); // M
    printf("%c\n", *(s + 2)); // M
    printf("%c\n", *(s + 3)); // A
}