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

    int digit = (card_number % 10)*2;
    int sum;

    for (int i = 100; i < 1000000; i=i*100)
    {
        digit = card_number/i % 10;
        sum = digit + digit*2;
    }
    */
    printf("%i\n",digit);

    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";


}
