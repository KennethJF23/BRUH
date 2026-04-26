#include <stdio.h>
#include "fact.h"

int i=1,fact=1;
int main(){
    int n;
    printf("Enter the number:\n");
    scanf("%d",&n);
    fact(n);
    printf("%d",fact);
    return 0;
}