#include <cs50.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, string argv[])
{
    int key;

    if (argc != 2 || atoi(argv[1]) < 0)
    {
        printf("Usage ./ceasar key\n");
        return 1;
    }
    printf("all good %s", argv[1]);
}
