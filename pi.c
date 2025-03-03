#include <stdio.h>
#include <math.h>

long double taylor_pi(){
    long double pi = 0.0;
    long double n = 1;
    while(1 > 0){
        pi = pi + (powl(-1, (n + 1))) / ((2 * n - 1));
        n++;
        long double out_pi = 4 * pi;
        //printf("                            C: %.19Lf\r", out_pi);
        printf("                            C: %.19Lf\n", out_pi);
    }

}

int main(){
    taylor_pi();
    return 0;
}
