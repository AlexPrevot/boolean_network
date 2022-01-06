import numpy as np

class agent:
    def __init__(self):
       self.matrice = np.zeros((8,8))
       #print(self.matrice)
       

       self.matrice[0][2] = True;
       self.matrice[0][3] = True;

    def modify_r(self,step):
        self.matrice[step%4 + 4][step%4 + 4] = True;

        for i in range(5):
            if i != step%5:
                self.matrice[4 + i][4 + i] = False
            

    def modify_e(self, b):
        self.matrice[0][1] = b
        self.matrice[0][0] = b
        self.matrice[1][1] = b


mathieu = agent()

mathieu.modify_r(3)

print(mathieu.matrice)
