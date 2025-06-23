#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);
    // 25, 10, 5, 1
    int coins = 0;

    while (n >= 25)
    {
        n = n - 25;
        coins++;
    }
    while (n >= 10)
    {
        n = n - 10;
        coins++;
    }
    while (n >= 5)
    {
        n = n - 5;
        coins++;
    }
    while (n >= 1)
    {
        n = n - 1;
        coins++;
    }

    printf("%i\n", coins);
}
