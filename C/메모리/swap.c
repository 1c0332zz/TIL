#include <stdio.h>

void swap(int *a, int *b);

int main(void)
{
    int x = 1;
    int y = 2;

    printf("x is %i, y is %i\n", x, y);
    // & = 주소를 전달
    swap(&x, &y);
    printf("x is %i, y is %i\n", x, y);
}

void swap(int *a, int *b)
{
    // * = 정수를 가리키는 포인터
    // tmp를 *a가 가리키는 주소로 가라고 명령하면 그곳엔 x가 있고 값은 1이다.
    int tmp = *a;
    // 마찬가지로 *b의 주소로 가라고 하고 그곳엔 y가 있고 값은 2다.
    // *a의 주소에 *b가 가리키는 주소를 저장시킨다
    *a = *b;
    *b = tmp;
}
// malloc을 쓰지 않았으니 free할 필요 없음