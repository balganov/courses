#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = get_int("Pyramid height: ");

    for (int r = 0; r < height; r++)
    {
        for (int c = 0; c < height; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}
