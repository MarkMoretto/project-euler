package main

import (
	"fmt"
	"math"
)

func main() {
	const seven = 7
	res := math.Sqrt(seven)
	msg := fmt.Sprintf("Square root of 7: %.4f", res)
	fmt.Println(msg)
}
