#include <stdio.h>
#include <math.h>
#include <stdlib.h>
char* addBinary(char* a, char* b) {
    int a1=atoi(a);
    int b1=atoi(b),c=0,k=0;
    int st=0,s,a2,b2;
    // for(int i=0; i<((strlen(a)>strlen(b))?strlen(a):strlen(b));i++)
    while(a1||b1||c){
        a2=a1%10;
        b2=b1%10;
        s=a2^b2^c;
        c=(a2&b2) | ((a2^b2)&c);
        a1/=10;
        b1/=10;
        st=st+s*pow(10,k);
        k++;
    }
    char*m;
    // itoa(st,m,10);
    sprintf(m,"%d",st);
    return m;
}
// char* addBinary2(char* a, char* b) {
    
//     while
// }

int main(){
    printf("sum:%s",addBinary("1111100011111100111","111"));
    return 0;
}