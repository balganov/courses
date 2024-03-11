#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long card_number;

    do
    {
        card_number = get_long("Number: ");
    }
    while (card_number < 0);

    int last_digit = card_number % 10;

    100
    10000
    1000000
    100000000
    for (int i = 0; i < 1000000; i*100)
    {
        
    }

    printf("%i\n",last_digit);

    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";


}
