import numpy as np



class agent:
    def __init__(self):
       self.matrice = np.zeros((8,8))
       #print(self.matrice)
       

       self.matrice[0][2] = 1;
       self.matrice[0][3] = 1;


    def modify_r(self,step):

        self.matrice[step%5 + 3][step%5 +3] = 1

        for i in range(5):
            if 3 + i != step%5 + 3:
                self.matrice[3 + i][3 + i] = 0

            

            

    def modify_e(self, b):
        self.matrice[0][1] = b
        self.matrice[0][0] = b
        self.matrice[1][1] = b


mathieu = agent()

pas_maximum = 11

for i in range(1,pas_maximum):
    mathieu.modify_r(i)
    print("--------------------")
    print(mathieu.matrice)
