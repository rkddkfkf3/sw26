import os

def compare_dirs(dir1, dir2):

    files1 = os.listdir(dir1)
    files2 = os.listdir(dir2)

    files1 = [f for f in files1 if os.path.isfile(os.path.join(dir1, f))]
    files2 = [f for f in files2 if os.path.isfile(os.path.join(dir2, f))]

    if len(files1) != len(files2):
        print("파일 개수가 다릅니다.")
        return

    files1.sort()
    files2.sort()

    if files1 != files2:
        print("파일 이름이 다릅니다.")
        return

    for file in files1:

        path1 = os.path.join(dir1, file)
        path2 = os.path.join(dir2, file)

        if os.path.getsize(path1) != os.path.getsize(path2):
            print(file, ": 파일 크기가 다릅니다.")
            return

        with open(path1, "r") as f1, open(path2, "r") as f2:

            content1 = f1.read()
            content2 = f2.read()

            if content1 != content2:
                print(file, ": 파일 내용이 다릅니다.")
                return

    print("두 디렉토리는 같습니다.")


dir1 = input("첫 번째 디렉토리: ")
dir2 = input("두 번째 디렉토리: ")

compare_dirs(dir1, dir2)