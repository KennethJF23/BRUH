#include <stdio.h>
#include "area.h"

int main(){
    int radius,side;
    printf("Enter the radius and side: \n");
    scanf("%d %d",&radius,&side);
    printf("Area of Square=%d\n",AREA_SQUARE(side));
    printf("AREA of Circle=%d\n",AREA_CIRCLE(radius));
    return 0;
}
