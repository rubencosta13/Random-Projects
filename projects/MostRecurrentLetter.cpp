#include <stdio.h>
#define size 4


void count(char string[]){
	
    int counter = 0;
    char counting[size]={};
    for(int i=0; i<size; i++){
        if(string[i]==string[i+1] ||string[i]==string[i+2] || string[i]==string[i+3] || string[i]==string[i+4]){
            counting[i] = string[i];
        }else{
        	counting[i] = ' ';
		}
    }
    if(counting[0] != counting[1]){
    	printf("Most recurrent letters: ");
    	printf("%c",counting[0]);
    	printf("%c",counting[1]);
	}else{
		printf("Most recurrent letter: ");
    	printf("%c",counting[0]);	
	}
}

main(){
    char string1[size] = {'A','B','A','B'};
    char handeler;
    count(string1);
    
}
