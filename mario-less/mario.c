#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = get_int("Pyramid height: ");

    for (int i = 0; i < height; i++)
    {
        printf("#");
    }
}
