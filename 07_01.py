answer = 0

big = 100_000


class Directory:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.size = 0
        self.files = []
        self.directories = []
        # if parent == "None":
        #    print(f"creating root")
        # else:
        #    print(f"Creating {name} as child of {parent.name}")

    def add_file(self, name, size):
        self.files.append(File(name, size))
        self.size += size
        # print(f"adding {name} as file in {self.name} of size {size}")

    def add_dir(self, name):
        self.directories.append(Directory(self, name))
        # print(f"adding {name} as child dir of {self.name}")

    def get_total_size(self):
        total = self.size
        for dir in self.directories:
            total += dir.get_total_size()
        return total

    def get_name(self):
        return self.name

    def get_parent(self):
        return self.parent

    def get_child(self, name):
        for i in self.directories:
            if i.name == name:
                return i

    def dirs_included(self):
        returns = []
        for i in self.directories:
            returns.append(i.name)
        return returns

    def files_included(self):
        returns = []
        for i in self.files:
            returns.append(i.name)
        return returns

    def __str__(self):
        return f"{self.name}: {self.get_total_size()}"

    def print_all(self):
        if self.get_total_size() > 100_000:
            print(self)
        for i in self.directories:
            i.print_all()

    def find_answer(self):
        answer = 0
        if self.get_total_size() < big:
            for i in self.directories:
                answer += i.find_answer()
            return answer + self.get_total_size()
        else:
            for i in self.directories:
                answer += i.find_answer()
            return answer

    def nice_print(self, indent):
        blank = "    "
        print(f"dir:  {blank * indent}{self.name}: {self.get_total_size()}")
        for i in self.files:
            print(f"file: {blank * (indent+1)}{i.name}: {i.size}")
        for i in self.directories:
            i.nice_print(indent + 1)


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


def main():
    with open("07.txt") as f:
        lines = f.readlines()

    root = Directory("None", "/")
    current = root

    for i in lines[1:]:
        # print(i)
        if "$" in i:
            if "cd" in i:
                if ".." in i:
                    # print(f"moving from {current.name} to {current.get_parent().name}")
                    current = current.get_parent()
                else:
                    # print(f"moving from {current.name} to {current.get_child(i[5:-1]).name}")
                    current = current.get_child(i[5:-1])
        else:
            if i[0:3] == "dir":
                if i[4:-1] not in current.dirs_included():
                    current.add_dir(i[4:-1])
            else:
                blank = i.find(" ")
                if i[blank+1:] not in current.files_included():
                    print(f"{i[blank+1:-1]}, {i[:blank]}")
                    current.add_file(i[blank+1:-1], int(i[:blank]))
    print(root.find_answer())


main()
