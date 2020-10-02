# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys

#added constants so that at later point of time we have to change these constants at only one place

constant_1 = 1126.9
constant_2 = 16.9
constant_3 = 68.1


def calc(a,b,c):
    nb=a.replace(a,"please")+" "+b.replace(b,"enter")+" "+c.replace(c,"won, rupees or dollars in (2)")
    nc=a.replace(a,"please")+" "+b.replace(b,"enter")+" "+c.replace(c,"won, rupee or dollar in (3)")
    if b=="won":
        wdol=float(a)/constant_1
        wrup=float(a)/constant_2
        if c=="rupee":
            print(a.replace(a,str(wrup))+" "+b.replace(b,"rupees")+" "+c.replace(c," "))
        elif c=="dollar":
            print(a.replace(a,str(wdol))+" "+b.replace(b,"dollars")+" "+c.replace(c," "))
        else:
            print(nc)
    elif b=="rupees":
        rdol=float(a)/constant_3
        rwon=float(a)*constant_2
        if c=="dollar":
            print(a.replace(a,str(rdol))+" "+b.replace(b,"dollars")+" "+c.replace(c," "))
        elif c=="won":
            print(a.replace(a,str(rwon))+" "+b.replace(b,"won")+" "+c.replace(c," "))
        else:
            print(nc)
    elif b=="dollars":
        drup=float(a)*constant_3
        dwon=float(a)*constant_1
        if c=="rupee":
            print(a.replace(a,str(drup))+" "+b.replace(b,"rupees")+" "+c.replace(c," "))
        elif c=="won":
            print(a.replace(a,str(dwon))+" "+b.replace(b,"won")+" "+c.replace(c," "))
        else:
            print(nc)
    else:
        print(nb)
            
            
if __name__ == "__main__":
   calc(sys.argv[1],sys.argv[2],sys.argv[3])
