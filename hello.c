#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("type first int ");
    int y = get_int("type second int ");

    while (x > 0)
    {
        printf("print counter %i\n",x);
        x--;
    }

    for (int i = 0; y > i, y--)
    {
        printf("print second counter %i\n",y);
    }

}
