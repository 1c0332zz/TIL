#include <stdio.h>

int main(void)
{
    double a, b;
    scanf("%lf %lf", &a, &b);
    printf("%.9lf\n", a / b);

    return 0;
}
