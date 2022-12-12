class Solution():
    def XparseFilesystemX(self,filename):
        with open(filename, 'r') as f:
            string = f.read()

            fs_dict = {}
            groups = string.split('$ cd')
            groups.remove('')
            for group in groups:
                data = group.strip().split("\n")
                if data != ['..']:
                    fs_dict[data[0]] = []
                    for i in range(2,len(data)):
                        if data not in ('', '..\n', '..'):
                            first, second = data[i].split(" ")
                            if first == "dir":
                                fs_dict[data[0]].append([second,0])
                            else:
                                fs_dict[data[0]].append([second,int(first)])

            # print("======= DEBUG SIZE ========")
            # for key,val in fs_dict.items():
            #     for a in val:
            #         print(key,a)
            # print("======= DONE ========")    
            
            
            fs_size_dict = {fs:0 for fs in fs_dict.keys()}

            def caculateFileSystem(directory):
                for file_dict in fs_dict[directory]:
                    if file_dict.size != 0:
                        fs_size_dict[directory]+=file_dict.size
                    else:
                        caculateFileSystem(file_dict.name)
                        fs_size_dict[directory]+=int(fs_size_dict[file_dict.name])

            caculateFileSystem("/")

            # print("======= DEBUG SIZE ========")
            # for key,val in fs_size_dict.items():
            #     print(key,val)
            # print("======= DONE ========")    

            return fs_size_dict

    def getParentDir(self,currentDir):
        if currentDir == "/": return []

        dirs = currentDir.split(" ")[1:-1]
        parents = ["/"]
        for dir in dirs:
            parents.append(f"{parents[-1]} {dir}")
        return parents

    def parseFilesystem(self,filename):
        dir_size = {}
        with open(filename, "r") as f:            
            current_dir = ""
            lines = f.read().splitlines()
            for line in lines:
                if line.strip() == "$ cd ..":
                    current_dir = ' '.join(current_dir.split(" ")[:-1])
                elif "$ cd" in line.strip():
                    dir = line.strip().split(" ")[2]
                    if dir == "/":
                        current_dir += dir
                    else:
                        current_dir += f' {dir}'
                elif line.strip() != "$ ls" and "dir " not in line.strip():
                    size = int(line.strip().split(" ")[0])

                    parents = self.getParentDir(current_dir)
                    for parent in parents:
                       dir_size[parent] += size

                    if current_dir not in dir_size:
                        dir_size[current_dir] = size
                    else:
                        dir_size[current_dir] += size
                else:
                    if current_dir not in dir_size:
                        dir_size[current_dir] = 0
                    else:
                        dir_size[current_dir] += 0

        return dir_size

    def main(self,filename):
        dir_size = self.parseFilesystem(filename)
        output = 0
        for dir,value in dir_size.items():
            if value <= 100000:
                output+=value
        print(output)

    def main2(self,filename):
        dir_size = self.parseFilesystem(filename)
        minimum = abs(70000000 - dir_size["/"] -30000000)

        output = 0
        for dir,value in dir_size.items():
            if value == minimum:
                return output
            if output == 0 and value >= minimum:
                output = value
            elif output > value and  value >= minimum:
                output = value

        return output


sol = Solution()
print(sol.main2('input.txt'))