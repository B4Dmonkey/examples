package main

import (
	"encoding/csv"
	"io"
	"iter"
	"os"
)

type Record []string

type Table struct {
	Reader *csv.Reader
	Writer *csv.Writer
	file   *os.File
}

func Open(fname string) (Table, error) {
	file, err := os.Open(fname)

	if err != nil {
		return Table{}, err
	}

	return Table{
		Reader: csv.NewReader(file),
		Writer: csv.NewWriter(file),
	}, nil
}

func (t Table) Close() error {
	return t.file.Close()
}

func (t Table) Read() (Record, error) {
	return t.Reader.Read()
}

func (t Table) ReadRows() iter.Seq[Record] {
	return func(yield func(Record) bool) {
		for {
			record, err := t.Reader.Read()
			if err == io.EOF {
				return
			}

			if err != nil {
				panic(err)
			}

			if !yield(record) {
				return
			}
		}
	}
}

func (t Table) Write(record Record) error {
	return t.Writer.Write(record)
}
