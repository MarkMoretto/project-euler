package problem760

const MOD uint = 1_000_000_007

var Total uint

func xor(a uint, b uint) uint {
	return a ^ b
}

func or(a uint, b uint) uint {
	return a | b
}

func and(a uint, b uint) uint {
	return a & b
}

func g(m uint, n uint) uint {
	return xor(m, n) + or(m, n) + and(m, n)
}

func G(N uint) {
	var n uint = 0
	var k uint
	pTotal := &Total
	*pTotal = 0
	for n <= N {
		k = 0
		for k <= n {
			*pTotal += (g(k, n-k) % MOD)
			k++
		}
		n++
	}
}
