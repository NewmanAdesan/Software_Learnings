// #include <cs50.h>
#include <stdio.h>

// prototypes
int get_start_size();
int get_end_size(int start_size);

int main(void)
{
    // TODO: Prompt for start size
    int start = get_start_size();

    // TODO: Prompt for end size
    int end = get_end_size(start);

    // TODO: Calculate number of years until we reach threshold
    int years = 1;

    for(int i = 0; start < end; i++){


        // number of babies every year -----> total_population / 3
        // number of deaths every year -----> total_population / 4
        start += (start / 3) + (start / 4);
        years++;

    }

    // TODO: Print number of years
    printf("years :%i\n", years)
}

int get_start_size(){

    int n;
    do
    {
        n = get_int("Start size: ")
    }while(n < 9);
    return n
}

int get_end_size(int start_size){

    int n;
    do
    {
        n = get_int("Stop size: ")
    }while(n < start_size);
}