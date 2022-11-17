#include <stdio.h>

int main(void)
{
  char *s="EMMA";
  char *t="EMMA";

    printf("%p\n",s);
    printf("%p\n",t);
    printf("%c\n",*s);
    printf("%c\n",*t);
    
    if(s==t){
        printf("same");
    }
    else{
        printf("diff");
    }
}