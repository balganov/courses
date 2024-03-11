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

    int sum = (card_number % 10)*2;

    for (int i = 100; i < 1000000; i=i*100)
    {
        sum = sum + (card_number/i % 10)*2;
    }
    
    printf("%i\n",sum);

    string output = "INVALID\n";
    output = "AMEX\n";
    output = "VISA\n";
    output = "MASTERCARD\n";


}
