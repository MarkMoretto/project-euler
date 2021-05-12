package perms

// Generate a slice in the domain [start, stop)
// https://www.golangprograms.com/golang-program-to-generate-slice-permutations-of-number-entered-by-user.html
func RangeSlice(start, stop int) []int {
	if start > stop {
		panic("Slice ends before it started")
	}
	xs := make([]int, stop-start)
	for i := 0; i < len(xs); i++ {
		// xs[i] = i + 1 + start
		xs[i] = i + start
	}
	return xs
}

// Generate permutations from a slice.
func Permutation(xs []int) (permuts [][]int) {
	var rc func([]int, int)
	rc = func(a []int, k int) {
		if k == len(a) {
			permuts = append(permuts, append([]int{}, a...))
		} else {
			for i := k; i < len(xs); i++ {
				a[k], a[i] = a[i], a[k]
				rc(a, k+1)
				a[k], a[i] = a[i], a[k]
			}
		}
	}
	rc(xs, 0)

	return permuts
}

func PowerSet(arr []uint) (output [][]uint) {
	if arr == nil {
		return nil
	}

	var (
		nlen uint = uint(len(arr))
		i    uint
	)

	for i = 0; i < (1 << nlen); i++ {
		var subset []uint
		for j := uint(0); j < nlen; j++ {
			if (i>>j)&1 == 1 {
				subset = append(subset, arr[j])
			}
		}

		if len(subset) > 0 {
			output = append(output, subset)
		}

	}
	return output
}

// var ps func([]int, int)

// func PowerSet(nums []int) (output [][]int) {
// 	if nums == nil {
// 		return nil
// 	}
// 	nlen := len(nums)

// 	ps = func(q []int, trgt int) {
// 		if trgt == len(q) {
// 			output = append(output, append([]int{}, q...))
// 		}
// 	}
// }
