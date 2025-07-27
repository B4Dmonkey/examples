package main

import (
	"fmt"

	"github.com/brianvoe/gofakeit/v7"
)

type Foo struct {
	Name string `fake:"{firstname}"`
	Bar  Bar
	Baz  []Baz `fakesize:"10"`
}

type Bar struct {
	Phone string `fake:"{phone}"`
}

type Baz struct {
	Email string `fake:"{email}"`
}

func main() {
	var f Foo
	err := gofakeit.Struct(&f)
	if err != nil {
		panic(err)
	}
	fmt.Printf("%v", f)
}
