// 자료형 3개로 이루어진 list라는 포인터를 4개로 변경할 때 무식하게 하는법....

#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    // int 자료형 3개로 이루어진 list 라는 포인터를 선언하고 메모리 할당
    int *list = malloc(3 * sizeof(int));

    // 포인터가 잘 선언되었는지 확인
    if (list == NULL)
    {
        return 1;
    }

    // list 배열의 각 인덱스에 값 저장
    list[0] = 1;
    list[1] = 2;
    list[2] = 3;

    // int 자료형 4개 크기의 tmp 라는 포인터를 선언하고 메모리 할당
    int *tmp = malloc(4 * sizeof(int));

    if (tmp == NULL)
    {
        return 1;
    }

    // list의 값을 tmp로 복사
    for (int i = 0; i < 3; i++)
    {
        tmp[i] = list[i];
    }

    // tmp배열의 네 번째 값도 저장
    tmp[3] = 4;

    // list의 메모리를 초기화
    free(list);

    // list가 tmp와 같은 곳을 가리키도록 지정
    list = tmp;

    // 새로운 배열 list의 값 확인
    for (int i = 0; i < 4; i++)
    {
        printf("%i\n", list[i]);
    }

    // list의 메모리 초기화
    free(list);
}