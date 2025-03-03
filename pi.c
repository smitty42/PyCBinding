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

float exp_pi(float exp){
    float pi = 3.14159;
    float out = pow(pi, exp);
    //printf("%f\n", out);
    return out;

}

int main(){
    printf("%f\n", exp_pi(2.0));
    taylor_pi();
    return 0;
}
