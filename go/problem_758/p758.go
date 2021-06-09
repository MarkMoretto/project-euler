package problem758

type Bucket struct {
	S, M, L int
}

func (b *Bucket) Init(small int, medium int) {
	b.S = small
	b.M = medium
}
