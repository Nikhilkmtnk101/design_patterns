from abc import ABC, abstractmethod


class FileSystem(ABC):
    @abstractmethod
    def ls(self):
        pass


class File(FileSystem):
    def __init__(self, file_name):
        self.file_name = file_name

    def ls(self):
        print(self.file_name)


class Folder(FileSystem):
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.file_system_list = []

    def add(self, file_system: FileSystem):
        self.file_system_list.append(file_system)

    def ls(self):
        print(f"Folder: {self.folder_name}")
        for file_system in self.file_system_list:
            file_system.ls()


if __name__ == "__main__":
   f1 = Folder("Movies")
   m1 = File("Border.mp4")
   f2 = Folder("Comedy")
   m2 = File("Hungama.mp4")
   f1.add(f2)
   f1.add(m1)
   f2.add(m2)
   f1.ls()
