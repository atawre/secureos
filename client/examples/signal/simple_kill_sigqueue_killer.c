#include <stdio.h>
#include <sys/types.h>
#include <signal.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    kill(atoi(argv[1]), SIGKILL);
    sigqueue(atoi(argv[2]), SIGKILL, (const union sigval)NULL);
    return 0;
}
