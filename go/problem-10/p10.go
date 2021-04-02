package problem_10

import (
	"fmt"
	"math"
)
/C/Users/Work1/Desktop/Info/PythonFiles/project-euler/go
var Result int

func isPrime(n int) bool {
	var res bool = true
	var i int = 2

	if n >= 2 {
		for i <= int(math.Sqrt(float64(n))) {
			if n%i == 0 {
				res = false
				break
			}
			i++
		}
	} else {
		res = false
	}
	return res
}

func SumPrimesToN(n int) {
	pResult := &Result
	for i := 1; i < n; i++ {
		if isPrime(i) {
			*pResult += i
		}
	}
}

func Run() {
	N := 2000000
	SumPrimesToN(N)

	fmt.Println("The sum of prime numbers up to 2 million is: ", Result)
}
