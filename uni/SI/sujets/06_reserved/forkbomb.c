#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>

int main(int argc, char* argv []) {
    pid_t pid = 0;
    int status;

    while(pid == 0) {
        pid = fork();
        if (pid < 0) {
            perror("fork");
            exit(errno);
        }
    }
    
    waitpid(pid, &status, 0);
    if WIFEXITED(status) {
        printf("status: %d\n", WEXITSTATUS(status));
    }
    
    return errno;
}