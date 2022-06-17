from local_lib.path import Path

def lets_go():
    dir = Path("dir")
    dir.mkdir_p()
    f = Path("dir/file.txt").touch()
    f.write_text("May the odds be ever in your favor.")
    text = f.read_text()
    print(text)

if __name__ == '__main__':
    lets_go()