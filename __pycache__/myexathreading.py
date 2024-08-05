import threading
class understand:
    def funct2(self):
        for i in range(65, 70):  # ASCII values for 'A' to 'E'
            char_value = chr(i)  # Convert i to corresponding character
            print(char_value)
    def funct3(self):
        for i in range(65,80):
            if(i%2==0):
                print(i)
    def combining(self):
        self.funct2()
        self.funct3()
obj=understand()
T1=threading.Thread(target=obj.combining)
T1.start()

