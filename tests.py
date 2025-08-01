from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file_content


def test():

    result = write_file_content(
        "calculator", "lorem.txt", "wait, this isn't lorem ipsum"
    )
    print("- Result:")
    print(result)

    result = write_file_content(
        "calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"
    )
    print("- Result:")
    print(result)

    result = write_file_content(
        "calculator", "/tmp/temp.txt", "this should not be allowed"
    )
    print("- Result:")
    print(result)


if __name__ == "__main__":
    test()

"""
    result = get_file_content("calculator", "main.py")
    print("Result for '../' directory:")
    print(result)

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result for '../' directory:")
    print(result)

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '../' directory:")
    print(result)

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for '../' directory:")
    print(result)
"""
