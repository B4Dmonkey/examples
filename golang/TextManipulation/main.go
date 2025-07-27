package main

import (
	"fmt"

	"golang.org/x/text/cases"
	"golang.org/x/text/language"
)

func main() {
	caser := cases.Title(language.English, cases.Compact)
	primary := "PRIMARY_WIN"
	fmt.Println(caser.String(primary))
	federal := "FEDERAL"
	fmt.Println(caser.String(federal))
}
