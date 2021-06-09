package problem758

type U interface {
	IsOdd() bool
	IsEven() bool
}

type V interface {
	IsOdd() bool
	IsEven() bool
}

type N uint

func (n *N) IsOdd() bool {
	return *n&1 == 0
}

func (n *N) IsEven() bool {
	return *n%2 == 0
}

func BinaryGCD(u uint, v uint) (solution uint) {
	if u == v {
		solution = u
	}
	if u == 0 {
		solution = v
	}
	if v == 0 {
		solution = u
	}
	switch {
	case (u&1 == 0):
		switch {
		case (v%2 == 0):
			return BinaryGCD(u, v/2)
		case (u > v):
			return BinaryGCD((u-v)/2, v)
		default:
			return BinaryGCD((v-u)/2, u)
		}
	case (v&1 == 0):
		switch {
		case (v&1 == 0):
			return BinaryGCD(u/2, v)
		default:
			return 2 * BinaryGCD(u/2, v/2)
		}
	default:
		return
	}
}

// func BinaryGCD(u uint, v uint) (solution uint) {
// 	if u == v {
// 		solution = u
// 	}
// 	if u == 0 {
// 		solution = v
// 	}
// 	if v == 0 {
// 		solution = u
// 	}
// 	switch {
// 	case (u&1 == 0):
// 		switch {
// 		case (v%2 == 0):
// 			return BinaryGCD(u, v/2)
// 		case (u > v):
// 			return BinaryGCD((u-v)/2, v)
// 		default:
// 			return BinaryGCD((v-u)/2, u)
// 		}
// 	case (v&1 == 0):
// 		switch {
// 		case (v&1 == 0):
// 			return BinaryGCD(u/2, v)
// 		default:
// 			return 2 * BinaryGCD(u/2, v/2)
// 		}
// 	default:
// 		return
// 	}
// }
