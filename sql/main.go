package main

import (
	"database/sql"
	"fmt"
	"main/rsql"

	_ "github.com/mattn/go-sqlite3"
)

const DB_DRIVER = "sqlite3"
const DB_NAME = "crud.db"

type Datum struct {
	Id   int
	Data string
}

func main() {
	fmt.Println("Just a quick demo\n\n")
	// * Connect to an sql lite db
	db, err := sql.Open(DB_DRIVER, DB_NAME)
	defer db.Close()

	if err != nil {
		panic("I'm freaking out dude!!! I couldn't open the database o_O")
	}

	if err := db.Ping(); err != nil {
		fmt.Println(err)
		panic("dude this is freaky I connected but couldn't ping?")
	}

	// * Load a script
	rawSQL, _ := rsql.Open("./crud.sql")

	fmt.Println(rawSQL)

	var stmt *sql.Stmt
	if stmt, err = db.Prepare(rawSQL); err != nil {
		fmt.Println(err)
		panic("Bru I swear im trying my best but i couldn't prepare the statement")
	}

	
	randData := "Boots and Cats"
	// * Execute crud
	if res, err := stmt.Exec(randData); err != nil {
		panic("Woah that execution didn't work out the way i hoped")
	} else {
		fmt.Println("I wonder what the res is?")
		fmt.Println(res)
	}
	fmt.Println("\n\nThank you for coming to my ted talk")
}
