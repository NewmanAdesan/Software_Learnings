#include <cs50.h>
#include <stdio.h>
#include <string.h>

// Max Voters and Max Candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9


// Creating a candidate structure
// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;


// Array of candidates --> to reference each candidate structure we create
candidate candidates[MAX_CANDIDATES];


// preferences[i][j] is jth preference for voter i
// based on the candidate  the voters choose,
// it contains index of that candidate structure in the candidate array
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Numbers of voters and candidates
// based on the number of voters or candites for a use case
// this variable sets kinda like an upper bound
// so that we use just enough memory from the arrays as needed
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }

    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];       // dont forget candidate name starts from argv[1]
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    // get the number of Voters
    voter_count = get_int("Number of voters: ");

    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }


    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;

}

bool vote(int voter, int rank, string name)
{
    /*
     * the idea here is, based on the name of the candidate
     * go to position [i][j] of the preference structure
     * and place the index of the candidate object in the candidate array
     * having that name.
     */


    /* loop through all the candidate structure in the candidat array
     * looking for the candidate that corresponds to that "name" argument
     * that will be specified
     */
    for (int i = 0; i < candidate_count; i++)
    {
        if (strcmp(candidates[i].name, name) == 0)
        {
            preferences[voter][rank] = i ;
            return true;
        }
    }

    return false;
}

void tabulate(void)
{

    /* the idea here is to go through each voters first preferences
     * if first preference has not been eliminated...<you check the candidate eliminated status>
     * increment vote count of that candidate and move to the next voter
     * if first preference has been eliminated, do the same for second preferences
     * go to it, check if the candidate at that spot has not been eliminated,
     * increment vote count of that candidate
     */


    for (int i = 0; i < voter_count; i++)
    {

        // checking all their preferences if need be
        for (int j = 0; j < candidate_count; j++)
        {
            // check the candidate eliminated status
            // if candidate has not been eliminated, dont go to other preferences
            // instead go to the other voters choice
            int index = preferences[i][j];

            if (!candidates[index].eliminated)
            {
                candidates[index].votes++;
                break;
            }
        }

    }

}


bool print_winner(void)
{
    /*
    *  The idea here is to go through each candidate in the candidate array
    *  Check candidate vote count if it is more than 50% of the total votes
    *  that is ((50/100( * voter_count)
    *  candidate who fulfill this condition is termed the winner
    *
    *  do not forget that candidates we check must have an eliminated status of "false"
    *
    *  if winner is found, print their name/names and return true
    */
    float cut_off = 0.5 * (float) voter_count;

    // if we find at lease one winner, this flag will be set to true
    bool found_winner = false;

    for (int i = 0; i < candidate_count; i++)
    {

        // if a candidate has not been eliminated check its vote count
        if (!candidates[i].eliminated)
        {

            if (candidates[i].votes > cut_off)
            {
                printf("%s\n", candidates[i].name);
                found_winner = true;
            }
        }
    }


    if (found_winner)
    {
        return true;
    }

    return false;

}


// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    // TODO
    /*
     * Out of all the Candidates votes, find the minimum vote
     *
     * initially setting the minimum vote to be an impossibly high vote.
     * the highest vote an individual can have is the number of voters
     * that is "voter_count". As we go through the candidate array
     * if we find a more smaller amount of vote, we will update minimum vote
     */

    // initially setting the minimum vote to be an impossibly high vote
    int min = voter_count + 2;

    for (int i = 0; i < candidate_count; i++)
    {
        // if a candidate has not been eliminated check its vote count
        if (!candidates[i].eliminated)
        {

            if (candidates[i].votes < min)
            {
                min = candidates[i].votes;
            }
        }
    }


    return min;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min)
{
    // TODO
    /*
     * If none of the candidates <that have not been eliminated> have vote
     * higher than the min vote, then there was a tie, return true
     */

    for (int i = 0; i < candidate_count; i++)
    {
        // if a candidate has not been eliminated check its vote count if greater that than mininum vote
        if (!candidates[i].eliminated)
        {

            if (candidates[i].votes > min)
            {
                return false;
            }
        }
    }

    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min)
{
    // TODO
    // Candidates which have minimum vote will have their eliminated status set to true
    for (int i = 0; i < candidate_count; i++)
    {
        // if a candidate has not been eliminated check its vote count if it ia the candidate with minimum number of vote
        if (!candidates[i].eliminated)
        {
            if (candidates[i].votes == min)
            {

                candidates[i].eliminated = true;
            }
        }
    }

    return;
}