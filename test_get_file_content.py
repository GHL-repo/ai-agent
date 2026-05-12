from functions.get_file_content import MAX_CHARS, get_file_content


def test():
    result = get_file_content("calculator", "lorem.txt")
    truncation = f'File "lorem.txt" truncated at {MAX_CHARS} characters]'
    print(truncation)
    if result.endswith(truncation):
        print("lorem.txt truncated: True")
    result = get_file_content("calculator", "main.py")
    print(result)
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print(result)
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)


if __name__ == "__main__":
    test()
