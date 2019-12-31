
"""
Purpose: Project Euler problems
Date created: 2019-12-08
Contributor(s): Mark M.

ID: 692
Title: Siegbert and Jo
URI: https://projecteuler.net/problem=692
Difficulty: ?

Status: Incomplete

Reference:
    https://en.wikipedia.org/wiki/Nim

Problem:
Siegbert and Jo take turns playing a game with a heap of N pebbles:
1. Siegbert is the first to take some pebbles. He can take as many pebbles as 
he wants. (Between 1 and N

inclusive.)
2. In each of the following turns the current player must take at least one
pebble and at most twice the amount of pebbles taken by the previous player.
3. The player who takes the last pebble wins.

Although Siegbert can always win by taking all the pebbles on his first turn,
to make the game more interesting he chooses to take the smallest number of
pebbles that guarantees he will still win (assuming both Siegbert and Jo play
optimally for the rest of the game).

Let H(N)
be that minimal amount for a heap of N pebbles.
H(1)=1, H(4)=1, H(17)=1, H(8)=8 and H(18)=5

Let G(n)
be ∑k=1nH(k)
G(13)=43

Find G(23416728348467685)
"""

def eval_selction(current_pick: int, prior_pick: int) -> bool:
    n_min: int = 1
    n_max: prior_pick * 2
    if current_pick >= n_min and current_pick <= n_max:
        return True
    else:
        return False


N: int = 17
start = 1
current = start
while current < N:












