# markdown 특정 부분에 글쓰기
def update_md_file(input, keyword, content):
    with open(input, 'r') as f:
        new_file = list()
        while True:
            line = f.readline()
            if not line: break
            if keyword==line.strip():
                new_file.append(line)
                new_file.append(content)
                new_file.append('\n')
                while True:
                    line = f.readline()
                    if "<br /><br /><br />" == line.strip():
                        print('pass')
                        new_file.append('\n')
                        break
            new_file.append(line)

    with open(input, 'w') as doc:
        doc.writelines(new_file)

if __name__ == "__main__":
    print(1)