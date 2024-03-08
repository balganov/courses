#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
       n = get_int("Change owed: ");
    }
    while(n < 0);
    //25, 10, 5, 1
    int coins;
    if (n % 25 == 0)
    {
        coins = n / 25;
        printf("%i\n",coins);
    } else if (n % 25 < 0 && n % 10 == 0)
    {
        coins = n / 10;
        printf("%i\n",coins);
    }
}
