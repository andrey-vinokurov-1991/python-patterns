"""Single Responsibility Principle.

"A class should have one, and only one, reason to change"

"You had one job. Just the one.". Loki.

A class should have only one job. If a
class has more than one responsibility, it becomes coupled. A change to one
responsibility results to modification of the other responsibility.
"""
import os


class Diary:
    def __init__(self):
        self.tasks = list()

    def add_task(self, description: str):
        self.tasks.append(description)

    def remove_task(self, task_id: int):
        del self.tasks[task_id]

    def remove_all_tasks(self):
        self.__init__()

    def __str__(self) -> str:
        return "\n".join(self.tasks)


class DiaryBrokenSRP(Diary):
    # breaking SRP
    def save(self, filename: str):
        with open(filename, "w") as f:
            f.write(str(self))

    def load(self, filename: str):
        with open(filename) as f:
            lines = f.readlines()
        self.tasks = [line.strip() for line in lines]

    def clear(self, filename: str):
        os.remove(filename)
        super().__init__()


class FileManager:
    def __init__(self):
        pass

    @staticmethod
    def save_to_file(diary: Diary, filename: str):
        with open(filename, "w") as f:
            f.write(str(diary))

    @staticmethod
    def load_from_file(diary: Diary, filename: str):
        with open(filename) as f:
            lines = f.readlines()
        diary.tasks = [line.strip() for line in lines]

    @staticmethod
    def remove_file(filename: str):
        os.remove(filename)


if __name__ == '__main__':
    print("Broken Diary testing...")
    diary_broken_srp = DiaryBrokenSRP()
    diary_broken_srp.add_task("Explore the Universe")
    diary_broken_srp.add_task("Enjoy")
    diary_broken_srp.save("temp.txt")
    diary_broken_srp.load("temp.txt")
    print(f"tasks:\n{str(diary_broken_srp)}")
    diary_broken_srp.clear("temp.txt")
    print(f"tasks:\n{str(diary_broken_srp)}")
    print("\n")

    print("Correct Diary testing...")
    diary_object = Diary()
    file_manager = FileManager()
    diary_object.add_task("Explore the Universe")
    diary_object.add_task("Enjoy")
    file_manager.save_to_file(diary_object, "temp.txt")
    file_manager.load_from_file(diary_object, "temp.txt")
    print(f"tasks:\n{str(diary_object)}")
    file_manager.remove_file("temp.txt")
    diary_object.remove_all_tasks()
    print(f"tasks:\n{str(diary_object)}")
