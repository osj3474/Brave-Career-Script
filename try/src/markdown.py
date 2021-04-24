# markdown 특정 부분에 글쓰기
name = "\t용감한 친구들\n"

with open('./test.md', 'r') as f:
    new_file = list()
    while True:
        line = f.readline()
        if not line:
            break
        if "[name]"==line.strip():
            line.replace('[name]','')
            line = name
            print("pass")
        new_file.append(line)

with open('./output.md', 'w') as doc:
    doc.writelines(new_file)


