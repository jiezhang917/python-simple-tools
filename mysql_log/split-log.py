from pathlib import Path

data_folder = Path("C:/Users/tin.luo/Downloads/")
print(data_folder)
filepath = data_folder / "original.txt"
with open(filepath) as fp:
    cnt = 1
    line = fp.readline()
    while line:
        # print("Line {}: {}".format(cnt, line.strip()))
        column1 = line.split(' ')[0]
        try:
            date = int(column1)
            file = open('day' + str(date) + '.txt', 'a')
            file.write(line)
        except ValueError:
            file.write(line)
        line = fp.readline()
        cnt += 1
