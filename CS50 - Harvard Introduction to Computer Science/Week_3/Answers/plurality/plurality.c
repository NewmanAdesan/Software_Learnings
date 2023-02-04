#include <stdio.h>
#include <string.h>

// Max number of candidates
#define MAX 9

// Candidates have name and vote count
typedef struct
{
    string name;
    int votes;
}
candidate;

// Array of candidates
candidate candidates[MAX];

// Number of candidates
int candidate_count;

// Function prototypes
bool vote(string name);
void print_winner(void);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: plurality [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX)
    {
        printf("Maximum number of candidates is %i\n", MAX);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
    }

    int voter_count = get_int("Number of voters: ");

    // Loop over all voters
    for (int i = 0; i < voter_count; i++)
    {
        string name = get_string("Vote: ");

        // Check for invalid vote
        if (!vote(name))
        {
            printf("Invalid vote.\n");
        }
    }

    // Display winner of election
    print_winner();
}

// Update vote totals given a new vote
bool vote(string name)
{
    // Loop through each candidate structure and check for candidate name
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            candidates[i].votes++;
            return true;
        }
    }

    return false;
}

// Print the winner (or winners) of the election
void print_winner(void)
{
    // get candidate name with the maximum vote 

    // we will set a candidate 1 as the place holder winner
    // by setting candidate 1 vote to be the winning vote
    // then we will loop through the array of candidates 
    // for any other candidate that has a higher vote
    int winning_vote = candidate[0].votes;

    for (int i = 1; i < candidate_count; i++)
    {
        if (candidates[i].votes > winning_vote)
        {
            // update the winning vote
            winning_vote = candidates[i].votes;
        }
    }

    // Once winning vote is found
    // the winner/winners of this election are those whose votes equal max_vote
    for (int i = 0; i < candidate_count; i++)
    {
        if (candidates[i].votes == winning_vote)
        {
            printf("%s\n", candidates[i].name);
        }
    }

    return;
}

// check out how to clear an array at once!!!!!!