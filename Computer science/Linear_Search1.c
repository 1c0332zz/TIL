// 주어진 배열에서 특정 값을 찾기 위해서 선형 검색

#include <stdio.h>

int main(void)
{
    // numbers 배열 정의 및 값 입력
    int numbers[] = {4, 8, 15, 16, 23, 42};

    // 값 50 검색
    for (int i = 0; i < 6; i++)
    {
        if (numbers[i] == 50)
        {
            printf("Found\n");
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}