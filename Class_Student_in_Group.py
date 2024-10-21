class Studnt:
    def __init__(self, studnt_id, name, grds=None):
        self.studnt_id = studnt_id
        self.name = name
        self.grds = grds if grds is not None else []

    def add_grde(self, grd):
        self.grds.append(grd)

    def avrg_grde(self):
        if len(self.grds) == 0:
            return 0
        return sum(self.grds) / len(self.grds)

    def __str__(self):
        return f"ID: {self.studnt_id}, Name: {self.name}, Mid grade: {self.avrg_grde():.2f}"

    def __del__(self):
        print(f"Studnt {self.name} killed")

class Group:
    def __init__(self):
        self.studnts = []

    def add_studnt(self, studnt):
        self.studnts.append(studnt)
        print(f"Studnt {studnt.name} added to group")

    def rmv_studnt(self, studnt_id):
        for studnt in self.studnts:
            if studnt.studnt_id == studnt_id:
                self.studnts.remove(studnt)
                print(f"Studnt {studnt.name} killed")
                return
        print(f"Studnt in Id {studnt_id} not foundud")

    def show_ranks(self):
        sortd_studnts = sorted(self.studnts, key=lambda s: s.avrg_grde(), reverse=True)
        print("Studnt's raiting:")
        for i, studnt in enumerate(sortd_studnts, 1):
            print(f"{i}. {studnt}")

    def __del__(self):
        print(f"Group with - {len(self.studnts)} studnts been alliminated")

def main():

    studnt1 = Studnt(1, "Max", [90, 85, 80])
    studnt2 = Studnt(2, "Bax", [91, 90, 90])
    studnt3 = Studnt(3, "Tax", [89, 80, 70])
    
    group = Group()

    group.add_studnt(studnt1)
    group.add_studnt(studnt2)
    group.add_studnt(studnt3)

    #Student Max added
    #Student Bax added
    #Student Tax added

    #Done correctly

    group.show_ranks()

    #ranks in group

    #Done correcly

    group.rmv_studnt(2)

    #killing Bax?

    #Done correctly

    group.show_ranks()

    # + ranking without Bax

    # Last - killing group and students


    # seems ok but 100% smth bad will hapn

if __name__ == "__main__":
    main()

