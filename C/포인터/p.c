#include <stdio.h>

int main(void)
{
    int n = 50;
    // n의 주소값을 변수에 저장할땐 변수명 앞에 *을 붙혀준다. (포인터)
    // 포인터가 가리키는 값이 int
    int *p = &n;
    // printf("%p\n", p);
    // 0061FF18 실제 메모리 주소

    // 해당 포인터가 가르키는 인트의 값을 가져와라
    printf("%i\n", *p);
    // 50
}
