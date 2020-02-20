#!/usr/bin/python

# Write a function `rock_paper_scissors` to generate all of the possible plays that can be made in a game of "Rock Paper Scissors",
# given some input `n`, which represents the number of plays per round.

# You'll want to define a list with all of the possible Rock Paper Scissors plays.
# Another problem that asks you to generate a bunch of permutations,
# so we're probably going to want to opt for using recursion again. Since we're building up a list of results,
# we'll have to pass the list we're constructing around to multiple recursive calls so that each recursive call can add
# to the overall result. However, the tests only give our function `n` as input.
# To get around this, we could define an inner recursive helper function that will perform the recursion for us,
# while allowing us to preserve the outer function's function signature.
# In Python, you can concatenate two lists with the `+` operator.
# However, you'll want to make sure that both operands are lists!
# If you opt to define an inner recursive helper function, don't forget to make an initial call to
# the recursive helper function to kick off the recursion.

# The Tribonacci Sequence :
# 0, 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415,
# 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601,
# 334745777, 615693474, 1132436852

import sys

rock = ["rock"]
paper = ["paper"]
scissors = ["scissors"]
available_options = ["rock", "paper", "scissors"]
def rock_paper_scissors(n):
    if n == 0:
        return [[]]
    if n == 1:
        return [rock, paper, scissors]
    return rps_helper(n, rock) + rps_helper(n, paper) + rps_helper(n, scissors)
def rps_helper(n, list):
    if n == 1:
        return [list]
    rockList, paperList, scissorList = list[:], list[:], list[:]
    rockList += rock
    paperList += paper
    scissorList += scissors
    n -= 1
    return (
        rps_helper(n, rockList) + rps_helper(n, paperList) + rps_helper(n, scissorList)
    )

# rock = "rock"
# paper = "paper"
# scissors = "scissors"
# initSet = [rock, paper, scissors]
# complete_list = rock + paper + scissors


#def rock_paper_scissors(n):



  # available_options = ['rock', 'paper', 'scissors']
  # end_results = [] # Will result in a list of all the possible plays available.
  # # Create Recursive Function
  # # Using two parameters, rounds and match_results
  # # rounds control how long our function will run for.
  # # match_results will store the record of all the resulting plays
  # def total_plays(rounds, match_result=[]):
  #   # Base Case
  #   # Once the loop is complete, add all of our plays to our end results
  #   if rounds < 1:
  #     return end_results.append(match_result)
  #   else:
  #     for option in available_options:
  #       total_plays(rounds - 1, match_result + [option])
  #       # Decrement our number of rounds each time
  # total_plays(n) # Trigger the recursion
  # return end_results

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')

