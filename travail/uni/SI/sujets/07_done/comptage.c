
#include<stdlib.h>
#include<stdio.h>
#include<unistd.h>

int countLines(FILE * fp){ 
    int lines= 0;
    char ch;
    while(!feof(fp))
    {
	ch = fgetc(fp);
	if(ch == '\n')
	{
	    lines++;
	}
    }
    return lines;
}

int main(int argc, char *argv[]){
    int lines= 0;
    FILE * fp;
    fp = fopen("myFile.txt", "r");
    lines= countLines(fp);
    printf("Number of line: %d", lines);
    return 0;
}
