#include <stdio.h>
#include <cs50.h>
void draw (int a);

int main(void)
{

    int height;
    while (true)
    {
        do
        {
            height = get_int("Pyramid height: ");
        }
        while (height < 1);

        draw (height);
    }
}

void draw (int a)
{
    int c;
    for (int r = a; r > 0; r--)
    {
        for (c = 0; c < r; c++)
        {
            printf("#");
        }

        for (int k = 0; k > c; k++)
        {
            printf("*");
        }
        printf("\n");
    }
}
