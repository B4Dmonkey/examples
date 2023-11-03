from db.db import db_factory
from .someModule.mod import mod_one
from .someModule.mod_too import mod_two

def main():
    print("Hello from main!")
    db_factory()
    mod_one()
    mod_two()

# if __name__ == "__main__":
#     main()
