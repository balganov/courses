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
    for (int r = a; r > 0; r--)
    {
        for (int c = 0; c < r; c++)
        {
            printf("#");
        }
        
        printf("\n");
    }
}
