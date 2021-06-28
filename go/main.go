package main

import (
	"fmt"
	// p "project_euler/go/problem_755"

	p "project_euler/go/problem_760"
	// "time"
)

func main() {

	// startTime := time.Now()
	// var maxNumber uint64 = 20
	// p.FibSequenceDemo(maxNumber)
	// endTime := time.Now()
	// timeDiff := endTime.Sub(startTime)
	// fmt.Println("Tot. time: ", timeDiff.Seconds(), "s")
	// fibs := []uint{1, 2, 3, 5, 8, 13}
	// ps := perm.PowerSet(fibs)
	// fmt.Println(ps)

	var num uint = 100
	p.G(num)
	fmt.Printf("The result of G(%d) is: %d\n", num, p.Total)
}
