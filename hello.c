#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("type first int ");
    int y = get_int("type second int ");

    if (x > y)
    {
        printf("first is greater than second\n");
    } else if (x < y)
    {
        printf("second is greater than first\n");
    } else
    {
        printf("first is equal to second\n");
    }
}
