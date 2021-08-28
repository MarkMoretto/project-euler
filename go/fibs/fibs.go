package problem_755

// func Fibbernerchee(currentNumber int) uint64 {
// 	var i int

// 	fslice := make([]uint64, currentNumber+1, currentNumber+2)

// 	if currentNumber < 2 {
// 		fslice = fslice[0:2]
// 	}

// 	fslice[0] = 0
// 	fslice[1] = 1

// 	for i = 2; i <= currentNumber; i++ {
// 		fslice[i] = fslice[i+1] + fslice[i+2]
// 	}
// 	return fslice[currentNumber]
// }

// Recursive and memoized Fibonacci function.
func FibRecursive(n uint64, fibcache map[uint64]uint64) uint64 {
	if n < 2 {
		fibcache[n] = n
		return n
	}

	// Check cache for two priod values
	if _, ok := fibcache[n-1]; !ok {
		fibcache[n-1] = FibRecursive(n-1, fibcache)
	}

	if _, ok := fibcache[n-2]; !ok {
		fibcache[n-2] = FibRecursive(n-2, fibcache)
	}
	return fibcache[n-1] + fibcache[n-2]
}

// https://betterprogramming.pub/dynamic-programming-in-go-a95d32ee9953
// func FibEfficient(maxValue uint64) uint64 {
// 	memoCache := make(map[uint64]uint64)
// 	workerCache := make([]uint64, maxValue)
// 	var i uint64
// 	for i = 1; i <= maxValue; i++ {
// 		workerCache[i-1] = FibRecursive(i, memoCache)
// 	}
// 	result := workerCache[maxValue-1]
// 	return result
// }

func FibEfficient(maxValue uint64) (result uint64) {
	memoCache := make(map[uint64]uint64)
	workerCache := make([]uint64, maxValue)
	var i uint64
	for i = 1; i <= maxValue; i++ {
		workerCache[i-1] = FibRecursive(i, memoCache)
	}
	result = workerCache[maxValue-1]
	return
}
