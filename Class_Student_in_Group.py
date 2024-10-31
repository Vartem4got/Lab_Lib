class Studnt:

    def __init__(self, studnt_id=None, name="", grds=None):

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
        
        
    # Add Unvrsty
    
class Unvrsty:
    def __init__(self):
        self.groups = []

    def add_group(self, group):
        self.groups.append(group)
        print(f"Group added to unvrsty")

    def get_loosers(self):
        loosers = []
        for group in self.groups:
            for studnt in group.studnts:
                if studnt.avrg_grde() < 50:
                    loosers.append(studnt)
        return loosers

    def print_loosers(self):
        loosers = self.get_loosers()
        if loosers:
            print("Loosers <50 lol:")
            for looser in loosers:
                print(looser)
        else:
            print("No loosers found :(")

    def kill_loosers(self):
        loosers = self.get_loosers()
        for group in self.groups:
            for looser in loosers:
                group.rmv_studnt(looser.studnt_id)
        print("All loosers have been killed yappi")

    def __del__(self):
        print(f"Unvrsty with {len(self.groups)} groups has been eliminated.")



def main():

    studnt1 = Studnt(1, "Max", [90, 85, 80])
    studnt2 = Studnt(2, "Bax", [91, 90, 90])
    studnt3 = Studnt(3, "Tax", [89, 80, 70])
    
    studnt4 = Studnt(4, "Lax", [40, 50, 20])
    studnt5 = Studnt(5, "Fax", [45, 45, 15])
    studnt6 = Studnt(6, "Aks", [35, 35, 5])
    
    group1 = Group()
    group2 = Group()

    group1.add_studnt(studnt1)
    group1.add_studnt(studnt2)
    group1.add_studnt(studnt3)
    
    group2.add_studnt(studnt4)
    group2.add_studnt(studnt5)
    group2.add_studnt(studnt6)

    #########
    '''
    group1.show_ranks()
    group2.show_ranks()
    '''
    #########
    '''
    group1.rmv_studnt(2)
    group2.rmv_studnt(5)
    '''
    #########
    '''
    group1.show_ranks()
    group2.show_ranks()
    '''
    #########
    
    university = Unvrsty()
    university.add_group(group1)
    university.add_group(group2)

    university.print_loosers()
    
    university.kill_loosers()
    
    university.print_loosers()
    
    group2.show_ranks()

    
    print("__________")
if __name__ == "__main__":
    main()

