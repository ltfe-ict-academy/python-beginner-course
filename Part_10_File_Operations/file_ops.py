import pathlib

my_file_path = pathlib.Path(__file__).parent / "test.txt"
print(my_file_path)


with open(my_file_path, encoding="utf-8") as my_file:
    print(f"Start: {my_file.tell()}")
    text = my_file.read(12)
    print(f"After read: {my_file.tell()}")
    my_file.seek(0)
    all_lines = my_file.readlines()
    print(f"After readlines: {my_file.tell()}")
    print(text)
    print(all_lines)

with open(my_file_path, mode="a", encoding="utf-8") as my_file:
    my_file.writelines(["To je nova vrstica 1\n", "to je nova vrstica 2\n"])
