package main

import (
	"fmt"
	p "project-euler/problem-10"
	"time"
)

func main() {

	startTime := time.Now()
	p.Run()
	endTime := time.Now()
	timeDiff := endTime.Sub(startTime)
	fmt.Println("Tot. time: ", timeDiff.Seconds(), "s")
}
