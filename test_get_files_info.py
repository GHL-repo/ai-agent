from functions.get_files_info import get_files_info


def test():
    result = get_files_info("calculator", ".")
    print("Result for current directory:")
    print(result, "\n")

    result = get_files_info("calculator", "pkg")
    print("Result for 'pkg' directory:")
    print(result, "\n")

    result = get_files_info("calculator", "/bin")
    print("Result for '/bin' directory:")
    print(result, "\n")

    result = get_files_info("calculator", "../")
    print("Result for '../' directory:")
    print(result, "\n")


if __name__ == "__main__":
    test()
