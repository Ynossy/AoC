class Folder:
    def __init__(self, name, parent):
        self.name = name
        self.folders = {"..": parent}
        self.files = {}
        self.file_size = 0

    def add_folder(self, name):
        if name not in self.folders:
            self.folders[name] = Folder(name, self)

    def add_file(self, name, size):
        if name not in self.files:
            self.files[name] = size
            self.file_size += size


def check_folder_size(folder: Folder, folder_sizes):
    size = sum(i[1] for i in folder.files.items())
    size += sum(check_folder_size(f[1], folder_sizes) for f in folder.folders.items() if f[0] != "..")
    folder_sizes.append((folder.name, size))
    return size


def main():
    with open("input.txt") as f:
        lines = f.read().strip().split("\n")
    root = Folder("root", None)
    root.add_folder("/")
    current_folder = root
    for line in lines:
        cmd = line.split(" ")
        if cmd[0] == "$":
            if cmd[1] == "cd":
                current_folder = current_folder.folders[cmd[2]]
            # skip "ls"
        elif cmd[0] == "dir":
            current_folder.add_folder(cmd[1])
        else:
            current_folder.add_file(cmd[1], int(cmd[0]))

    l = []
    total = check_folder_size(root.folders["/"], l)
    print(f"Result 1: {sum(i[1] for i in l if i[1]<100000)}")  # 2031851

    clearable = total - 40000000
    print(f"Result 2: {min([x[1] for x in l if x[1]>clearable])}")  # 2568781


if __name__ == "__main__":
    main()
