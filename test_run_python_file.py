from functions.run_python_file import run_python_file


def test():
    r = run_python_file("calculator", "main.py")
    print(r)
    r = run_python_file("calculator", "main.py", ["3 + 5"])
    print(r)
    r = run_python_file("calculator", "tests.py")
    print(r)
    r = run_python_file("calculator", "../main.py")
    print(r)
    r = run_python_file("calculator", "nonexistent.py")
    print(r)
    r = run_python_file("calculator", "lorem.txt")
    print(r)


if __name__ == "__main__":
    test()
