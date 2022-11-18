// realloc함수를 이용해 list.c보다 더 빠르게 간단하게 실행
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    int *list = malloc(3 * sizeof(int));
    if (list == NULL)
    {
        return 1;
    }

    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // tmp 포인터에 메모리를 할당하고 list의 값 복사
    // realloc은 자동으로 메모리를 늘려주고 줄여줌
    int *tmp = realloc(list, 4 * sizeof(int));
    if (tmp == NULL)
    {
        return 1;
    }

    // list가 tmp와 같은 곳을 가리키도록 지정
    list = tmp;

    // 새로운 list의 네 번째 값 저장
    list[3] = 4;

    // list의 값 확인
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // list 의 메모리 초기화
    free(list);
}