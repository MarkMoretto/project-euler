package main

import (
	"errors"
	"fmt"
	"log"
	"math/rand"
	"time"
)

const HEADS_BIAS int = 60
var r *rand.Rand

type Side int
type RESULT int
type ResultMap map[Side]int



const (
	H Side = iota
	T Side = iota
)



type Coin struct {
	hCount int
	tCount int
	bias int
}

func(c *Coin) Init() {
	c.hCount = 0
	c.tCount = 0
	c.bias = HEADS_BIAS

}

func (c *Coin) BiasedCoinflip() {
	if r.Intn(100) < c.bias {
		c.hCount += 1
	} else {
		c.tCount += 1
	}
}

func (c *Coin) NHeads() int {
	return c.hCount
}

func (c *Coin) NTails() int {
	return c.tCount
}

func (c *Coin) denom()float64 {
	return float64(c.NHeads() + c.NTails())
}

func (c *Coin) HTRatio() (float64, error) {
	if c.NTails() <= 0 {
		return float64(0.0), errors.New("Zero division error.")
	}
	return float64(c.NHeads()) / c.denom(), nil
}

func (c *Coin) Epoch(cycleCount int) {
	for cycleCount > 0 {
		c.BiasedCoinflip()
		cycleCount--
	}
}

func init() {
	r = rand.New(rand.NewSource(time.Now().UnixNano()))
}

func main() {
	var cycles int = 1000
	var epochs int = 100
	fEpochs := float64(epochs)
	var res float64 = 0.0
	var coin Coin = Coin{hCount: 0, tCount: 0, bias: HEADS_BIAS}

	var i float64
	for i = 1; i <= fEpochs; i++ {
		coin.Epoch(cycles)
		pct, err := coin.HTRatio()
		if err != nil {
			log.Fatal(err)
		}
		res += pct
		if int(i)%5==0 {
			fmt.Printf("Epoch %f - pct: %.4f,\n", i, pct)			
		}
	}
	fmt.Printf("The result was: %f\n", res)

}
