package problem_755

import (
	"fmt"
	f "project_euler/go/fibs"
)

func FibSequenceDemo(maxNumber uint64) {
	var i uint64
	for i = 2; i < maxNumber; i++ {
		fmt.Printf("%d ", f.FibEfficient(i))
	}
}


