package main

import (
	"testing"
)

func TestOpen(t *testing.T) {
	tbl, err := Open("./example.csv")

	if err != nil {
		t.Fatal(err)
	}

	for r := range tbl.ReadRows() {
		t.Log(r)
	}
}
