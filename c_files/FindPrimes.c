
#include <stdio.h>

int *EvalPrimes(int n)
{
    int i, j, is_prime;

    for (i = 2; i <= n; i++)
    {
        if (n % i == 0)
        {
            is_prime = 1;
            for (j = 2; j <= i / 2; j++)
            {
                if (i % j == 0)
                {
                    is_prime = 0;
                    break;
                }
            }
            if (is_prime == 1)
            {
                return i;
            }
        }
    }
}
