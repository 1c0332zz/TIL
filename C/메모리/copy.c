#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main(void)
{
    char *s = get_string("s: ");

    char *t = malloc(strlen(s) + 1);

    strcpy(t, s);

    t[0] = toupper(t[0]);

    printf("%s\n", s);
    printf("%s\n", t);
}