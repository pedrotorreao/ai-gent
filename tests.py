from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file_content
from functions.run_python import run_python_file


def test():

    result = run_python_file("calculator", "main.py")
    print("- Result:")
    print(result)

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("- Result:")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print("- Result:")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print("- Result:")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print("- Result:")
    print(result)


if __name__ == "__main__":
    test()

"""
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
"""
