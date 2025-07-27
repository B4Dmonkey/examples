package main

import (
	"log"
	"os"
)

func main() {
	lg := log.New(os.Stdout, "foo", log.LstdFlags)
	lg.Println("hey")
}
