

class StudyEntry003(object):
    def __init__(self) -> None:
        pass

    @staticmethod
    def run(*, execute: bool):
        if (not execute):
            return

        # ---------------栈----------
        obj = StudyEntry003()

        obj.example1(isWork=False)



    def example1(self, *, isWork: bool):
        if (not isWork):
            return
        print("")