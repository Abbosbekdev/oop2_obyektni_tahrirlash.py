class Massiv :
    def __init__(self,a):
        self.massiv = a
    def __add__(self, other):
        res = []
        for i in range(len(self.massiv)):
            res.append(self.massiv[i]+other.massiv[i])
        return Massiv(res)
    def __sub__(self, other):
        res = []
        for i in range(len(self.massiv)):
            res.append(self.massiv[i]-other.massiv[i])
        return Massiv(res)
    def __mul__(self, other):
        res = []
        if type(other)==type(1):
           for i in range(len(self.massiv)):
               res.append(self.massiv[i]*other)
        else:
            for i in range(len(self.massiv)):
                res.append(self.massiv[i]*other.massiv[i])
        return Massiv(res)
    def __truediv__(self, other):
        res = []
        if type(other) == type(1) :
            for i in range(len(self.massiv)):
                res.append(self.massiv[i] / other)
        else:
            for i in range(len(self.massiv)):
                res.append(self.massiv[i]/other.massiv[i])
        return Massiv(res)
    def max(self):
        return Massiv(max(self.massiv))
    def min(self):
        return Massiv(min(self.massiv))
    def sum(self):
        return Massiv(sum(self.massiv))
    def indeks(self):
        max = self.massiv[0]
        j = 0
        for i in range(len(self.massiv)):
            if max < self.massiv[i] :
                max = self.massiv[i]
                j = i
        return Massiv(j)
    def joylashtir(self):
        res1 = []
        res2 = []
        for i in range(len(self.massiv)):
            if self.massiv[i] > 0 :
                res2.append(self.massiv[i])
            else:
                res1.append(self.massiv[i])
        return Massiv(res1+res2)
    def sana(self):
        j = 0
        k = 0
        for i in range(len(self.massiv)):
            if self.massiv[i] > 0 :
                j+=1
            else:
                k+=1
        return Massiv(str(f'musbat sonlar soni : {j},\nmanfiy sonlar soni : {k}'))
    def propel(self,n):
        res = []
        for i in range(-n,len(self.massiv)) :
            res.append(self.massiv[i])
        self.massiv = res
    def propel1(self,n):
        res = []
        for i in range(n,len(self.massiv)):
            res.append(self.massiv[i])
        for i in range(n) :
            res.append(self.massiv[i])
        self.massiv = res
    def teskari(self,n):
        res = []
        for i in range(n) :
            res.append(i)
        self.massiv = res
        return Massiv(self.massiv.sort(reverse=True))
    def __str__(self):
        return str(self.massiv)
