#include <stdio.h>
int main(){
    char word[51];
    scanf("%s", word);
    int i;
    int bot;
    int val = -1;
    int len = 0;
    while(word[len] != '\0'){
        len++;
    }
    if (len%2 ==1){
        bot = len/2 + 1;
    }else{
        bot = len/2;
    }
    for (i=0; i<bot;i++){
        if(word[i]=='t'||word[i]=='T'){
            val = 1;
        }
    }
    for (i=bot;i<len;i++){
        if(word[i]=='t'||word[i]=='T'){
            val = 2;
        }
    }
    printf("%d\n",val);
    return 0;
}