#include <stdio.h>

int sumOfDigits(int);

int main(){
    int num_to_pass;
    int result;
    scanf("%d", &num_to_pass);
    result = sumOfDigits(num_to_pass);
    printf("%d", result);
    return 0;
}
int sumOfDigits(int a){
    if (a<10){
        return a;
    }else{
    return sumOfDigits(a%10) + sumOfDigits(a/10);
    }

}