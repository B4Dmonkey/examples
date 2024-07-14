package rsql

import (
	"fmt"
	"os"
	"strings"
)

func Open(sql_file string) (string, error) {
	var err error
	var data []byte
	if data, err = os.ReadFile(sql_file); err != nil {
		return "You should really handle that error brother man", err
	}

	// * should parse on the delimiters from -- to ; should probably
	// Todo: just return the first block only
	sql_string_statements := string(data)
	sql_statement_array := strings.SplitAfter(sql_string_statements, ";")
	statement_map := make(map[string]string)

	for i, statement_block := range sql_statement_array {
		fmt.Println("Loop iter", i)

		fmt.Println("The statement block is")
		cleanStatement := strings.TrimSpace(statement_block)
		fmt.Println(cleanStatement)

		fmt.Println("The ideal key is")
		//Todo: Need to figure out how to match on the comment so that the first word is the key and I think were money


		key := fmt.Sprint(i)
		statement_map[key] = cleanStatement

		fmt.Println()
	}

	fmt.Println(statement_map)

	// Todo: Put all the strings in a map?
	return sql_statement_array[0], nil
}
