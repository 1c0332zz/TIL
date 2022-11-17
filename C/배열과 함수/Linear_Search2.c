// 전화번호부에서 특정 이름을 찾아 해당하는 전화번호를 출력하는 프로그램을 작성
#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    // names 배열과 numbers 배열을 따로 정의하고 names 배열에서 검색을 해서 해당하는 인덱스의 numbers 배열 값을 출력하는 것
    string names[] = {"EMMA", "RODRIGO", "BRIAN", "DAVID"};
    string numbers[] = {"617–555–0100", "617–555–0101", "617–555–0102", "617–555–0103"};

    for (int i = 0; i < 4; i++)
    {
        if (strcmp(names[i], "EMMA") == 0)
        {
            printf("Found %s\n", numbers[i]);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}