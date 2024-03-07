#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int height = get_int("Pyramid height: ");

    draw (height);

}

void draw (int a)
{
    for (int r = 0; r < a; r++)
    {
        for (int c = 0; c < a; c++)
        {
            printf("#");
        }
        printf("\n");
    }
}
