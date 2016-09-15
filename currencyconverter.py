# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.
import sys
def calc(a,b,c):
    no=a.replace(a,"please")+" "+b.replace(b,"enter")+" "+c.replace(c,"won, rupee or dollar")
    if b=="won":
        wdol=float(a)/1126.9
        wrup=float(a)/16.9
        if c=="rupee":
            print(a.replace(a,str(wrup))+" "+b.replace(b,"rupees")+" "+c.replace(c," "))
        elif c=="dollar":
            print(a.replace(a,str(wdol))+" "+b.replace(b,"dollars")+" "+c.replace(c," "))
        else:
            print(no)
    elif b=="rupees":
        rdol=float(a)/68.1
        rwon=float(a)*16.9
        if c=="dollar":
            print(a.replace(a,str(rdol))+" "+b.replace(b,"dollars")+" "+c.replace(c," "))
        elif c=="won":
            print(a.replace(a,str(rwon))+" "+b.replace(b,"won")+" "+c.replace(c," "))
        else:
            print(no)
    elif b=="dollars":
        drup=float(a)*68.1
        dwon=float(a)*1126.9
        if c=="rupee":
            print(a.replace(a,str(drup))+" "+b.replace(b,"rupees")+" "+c.replace(c," "))
        elif c=="won":
            print(a.replace(a,str(dwon))+" "+b.replace(b,"won")+" "+c.replace(c," "))
        else:
            print(no)
    else:
        print(no)
            
            
if __name__ == "__main__":
   calc(sys.argv[1],sys.argv[2],sys.argv[3])
