#include <stdio.h>
#include <ctype.h>
#include <errno.h>
#include <float.h>
#include <limits.h>
#include <math.h>
#include <stdarg.h>
#include <stdint.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <inttypes.h>

// 나이 물어보기
int main(void)
{
    int age = get_int("what's your age?\n");
    // int days = age * 365;
    printf("You are at least %i days old.\n", age * 365);
}


// 6.25의 세금구하기
int main(void)
{
    float price = get_float("what's the price??\n");
    // 그냥 %f를 사용하면 소수점 106.250000 까지 나옴. 그래서 %.2f로 2자리까지만 나오게 해줌
    printf("Your total is %.2f.\n", price * 1.0625);

}

// 홀짝 구하기
int main(void)
{
    int n = get_int("n: ");

    if (n % 2 == 0)
    {
        printf("even\n");
    }
    else
    {
        print("odd\n");
    }
}

int main(void)
{
    for (int i = 0; i < 3; i++)
    {
        printf("cough\n");
    }
}