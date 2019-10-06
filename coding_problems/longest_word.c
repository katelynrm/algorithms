#include <stdio.h>
int main(){
    int i;
    int k;
    char word[50];
    int num_words = 0;
    int max = 0;
    scanf("%d",&num_words);
    int lengths[num_words];
    for (i=0;i<num_words;i++){
        k=0;
        scanf("%s", word);
        while(word[k]!='\0'){
            k++;
        }
        lengths[i] = k;
    }
    for (i=0;i<num_words;i++){
        if (lengths[i] > max){
            max = lengths[i];
        }
    }
    printf("%d",max);
    return 0;
}