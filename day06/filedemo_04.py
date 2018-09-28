# filedemo_04.py
import os, time
# 사용자로부터 디렉토리(폴더)명을 입력받은 후 파일목록(폴더목록 포함) 출력

def listDir(dir):
    files = os.listdir(dir)
    print('\t\t{0} 디렉토리 내용입니다.'.format(dir))
    print("-" * 50)
    fileList = []
    dirList = []
    for file in files:
        # 파일? 디렉토리? -> os.path.isfile(), os.path.isdir()
        # 디렉토리 출력, 파일 출력 (이름순)
        if os.path.isfile(file) == True:
            fileList.append(file)
        else:
            dirList.append(file)

    for dirName in dirList:
        print("{0}\t<DIR>\t-\t{1}".format(
                    time.ctime(os.path.getmtime(dirName)), 
                    dirName))
    
    totalSize = 0
    for fileName in fileList:
        totalSize = totalSize + os.path.getsize(fileName)  
        print("{0}\t-\t{1}\t{2}".format(
                    time.ctime(os.path.getmtime(fileName)), 
                    os.path.getsize(fileName),
                    fileName))
    print("-" * 50)   
    print("전체 디렉토리 개수:", len(dirList))
    print("전체 파일 개수:", len(fileList))
    print("전체 파일 용량:", totalSize)

def main():
    user_input = input("디렉토리명->")
    listDir(user_input)
    # dir = "c:\\Work\\github\\python"
    # file = "c:\\Work\\github\\python\\the_little_prince.txt"
    # print('파일여부:', os.path.isfile(file))
    # print('파일크기:', os.path.getsize(file))
    # print('파일마지막수정일:', os.path.getmtime(file))
    # print('파일마지막수정일:', time.ctime(os.path.getmtime(file)))
    
main()