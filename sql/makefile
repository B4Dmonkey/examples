APP_NAME = sql_file_parser
BUILD_DIR = $(PWD)/bin

build:
	CGO_ENABLED=1 go build -ldflags="-w -s" -o $(BUILD_DIR)/$(APP_NAME) main.go

run: build
	$(BUILD_DIR)/$(APP_NAME)


migration:
	dbmate new taybull

migration_up:
	dbmate --url=sqlite3:crud.db  up