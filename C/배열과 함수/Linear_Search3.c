// 좋은 방법은 아래 코드와 같이 새로운 자료형으로 구조체를 정의해서 이름과 번호를 묶어주는 것
#include <cs50.h>
#include <stdio.h>
#include <string.h>

// person 이라는 이름의 구조체를 자료형으로 정의하고 person 자료형의 배열을 선언하면 그 안에 포함된 속성값은 ‘.’으로 연결해서 접근
typedef struct
{
    char name;
    char number;
} person;

int main(void)
{
    person people[4];

    people[0].name = "EMMA";
    people[0].number = "617–555–0100";
    people[1].name = "RODRIGO";
    people[1].number = "617–555–0101";
    people[2].name = "BRIAN";
    people[2].number = "617–555–0102";
    people[3].name = "DAVID";
    people[3].number = "617–555–0103";

    // EMMA 검색
    for (int i = 0; i < 4; i++)
    {
        // person a; 라는 변수가 있다면, a.name 또는 a.number 이 각각 이름과 전화번호를 저장하는 변수
        if (strcmp(people[i].name, "EMMA") == 0)
        {
            printf("Found %s\n", people[i].number);
            return 0;
        }
    }
    printf("Not found\n");
    return 1;
}