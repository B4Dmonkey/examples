package main

import "fmt"
import "example.com/greetings"
import "rsc.io/quote"


func main() {
    fmt.Println("Hello, World!")
		fmt.Println(quote.Go())
		message := greetings.Hello("Gladys")
    fmt.Println(message)
}


