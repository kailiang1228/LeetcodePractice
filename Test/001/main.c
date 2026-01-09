#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, j, k,n=0;

    for (i = 1; i < 5; i++)
    for (j = 1; j < 5; j++)
    for (k = 1; k < 5; k++){
        if ( i!=k && i!=j && j!=k ){        //&& and
            n++;                            //n計算幾個
            printf("%d%d%d\n", i, j, k);    //output
        }
    }
    printf("一共有%d個\n", n);

return 0;
}
