#include <cs50.h>
#include <stdio.h>
#include <math.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // Ask how many cents the customer is owed
    int cents = get_cents();

    // Calculate the number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // Calculate the number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // Calculate the number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // Calculate the number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Print total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    // TODO
    int n;
    do
    {
        //  getting change from user
        float change = get_float("Change owed: ");

    }while(n < 0);

    // converting change to cents
    n = round(change * 100);

    return n;
}

int calculate_quarters(int cents)
{
    // TODO
    quarters_count = 0;

    for(int i = 0; cents < 25; i++)
    {
        cents = cents - 25;
    } 

    return quarters_count;
}

int calculate_dimes(int cents)
{
    // TODO
    dimes_count = 0;

    for(int i = 0; cents < 10; i++)
    {
        cents = cents - 10;
    } 
    
    return dimes_count;
}

int calculate_nickels(int cents)
{
    // TODO
    nickels_count = 0;

    for(int i = 0; cents < 5; i++)
    {
        cents = cents - 5;
    } 

    return nickels_count;
}

int calculate_pennies(int cents)
{
    // TODO
    pennies_count = 0;

    for(int i = 0; cents < 1; i++)
    {
        cents = cents - 1;
    } 

    return pennies_count;
}
