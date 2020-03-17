

class Tech_Enth:
    enth_count = 0

    def _init_(self, Name, Role, Avltime, Interest):
        self.Role = None
        self.Avltime = None
        self.Interest = []
        enth_count += 1

    def addStacks(self):
            self.Interest.append(value)        # stacking each individuals intrest

    def setMentorOrLearner(self, Rol):
        self.Role = Rol

    def setAvailableTime(self, time):
        self.Avltime = time

    def getMentor(self, stack, time):
        for x in self.Interest:
            if x is stack:
                if self.Avltime is time:
                    print("mentor found")
                else:
                    print("mentor not available, sorry")
            else:
                print("mentor not available, sorry")

