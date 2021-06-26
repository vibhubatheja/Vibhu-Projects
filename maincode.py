import numpy
import math
import os
import ast 
def create_nodes(ro):
  x=[]
  n=input("Enter the Nodal Values")
  
  li=[]
  lee=n.split(",")
  
  for i in lee :
    li.append(float(i))
  x=li
 
  
  for i in ro :
      if i==x :
       print("node exists")
       x=[]
       return(x)
  return(x)

def newallloadenterfunny(i,j) : #i is conn pair 

   dkr=[]
   for bad in i :
     print("Member Currently being Modified",bad)
     
     if len(bad)>5 :
      del(bad[6])
      del(bad[5])

      n3=bad[2]
      n5=bad[4]
      
      
      udl=n3/n5    #Udl Load ENtry 
      udl=25*udl
      udl2=float(input("Enter the SUM of UDL throughtout the Span"))
      udl=udl+udl2
      n6=udl
      pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
      if (pointloadwant==1) :
            habata=[]
            print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
            etala=int(input(" \n Enter the N.o of Point Loads You want to enter" ))           
            for nodooi in range(etala) :
                        nrairi=float(input("Enter Load Intensity")   )
                        oiisaaa=float(input("Enter Load Distance from first node Side"))
                        habata.append(nrairi)
                        habata.append(oiisaaa)              
            n7=[]
            n7=habata
      if pointloadwant!=1 :
       n7=[]


      bad.append(n6)
      bad.append(n7)
    
      print(bad)
      dkr.append(bad)
                   
      
     if len(bad)==5 :
      
      n3=bad[2]
      n5=bad[4]
      
      udl=n3/n5           #Udl Load ENtry 
      udl=25*udl
      udl2=float(input("Enter the SUM of UDL throughtout the Span"))
      udl=udl+udl2
      n6=udl
      pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
      if (pointloadwant==1) :
            habata=[]
            print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
            etala=int(input("Enter the N.o of Point Loads You want to enter" ))           
            for nodooi in range(etala) :
                        nrairi=float(input("Enter Load Intensity")   )
                        oiisaaa=float(input("Enter Load Distance from first node Side"))
                        habata.append(nrairi)
                        habata.append(oiisaaa)              
            n7=[]
            n7=habata
      if pointloadwant!=1 :
       n7=[]
      bad.append(n6)
      bad.append(n7)

      print(bad)
      dkr.append(bad)    
   
   return(dkr)
   #new print layout
   #checkif load is there aldready 
  
def updateloadismorefunny9(i,j) :   #See i  and j, i is conn pair
  ionlyprinttheconnectednodes(j,i)
  
  kaka=int(input("Enter The N.o of nodes you want to Modify Load on"))
  unclesam=[]         
  for isak in range (kaka) :
      inkpen=int(input("Enter the Member you want to modify"))-1
      unclesam.append(inkpen)
      print(unclesam)
  bad=[]    
  dono=0
  for bad in i  :
    
   if(dono in unclesam) : 
    
    
    print(bad)
    del(i[dono])
    print("Modifying Currently This Member",bad)
    
    if len(bad)>5 :
      del(bad[6])
      del(bad[5])
      n3=bad[2]
      n5=bad[4]
      
      udl=n3/n5           #Udl Load ENtry 
      udl=25*udl
      udl2=float(input("Enter the SUM of UDL throughtout the Span"))
      udl=udl+udl2
      n6=udl
      pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
      if (pointloadwant==1) :
            habata=[]
            print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
            etala=int(input("\n Enter the N.o of Point Loads You want to enter" ))           
            for nodooi in range(etala) :
                        nrairi=float(input("Enter Load Intensity")   )
                        oiisaaa=float(input("Enter Load Distance from first node Side"))
                        habata.append(nrairi)
                        habata.append(oiisaaa)              
            n7=[]
            n7=habata
      if pointloadwant!=1 :
       n7=[]
      bad.append(n6)
      bad.append(n7)
        #if(len(bad)>7):
       #unagi=len(bad)-8
      # for amagi in range (unagi) :
         #print("in it 1",amagi+7)
         #print("in it 2",len(bad))
         #del(bad[amagi+7])    
      print(bad)
      i.append(bad)
    if len(bad)==5 :
      n3=bad[2]
      n5=bad[4]
      
      udl=n3/n5           #Udl Load ENtry 
      udl=25*udl
      udl2=float(input("Enter the SUM of UDL throughtout the Span"))
      udl=udl+udl2
      n6=udl
      pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
      if (pointloadwant==1) :
            habata=[]
            print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
            etala=int(input("\n Enter the N.o of Point Loads You want to enter" ))           
            for nodooi in range(etala) :
                        nrairi=float(input("Enter Load Intensity")   )
                        oiisaaa=float(input("Enter Load Distance from first node Side"))
                        habata.append(nrairi)
                        habata.append(oiisaaa)              
            n7=[]
            n7=habata
      if pointloadwant!=1 :
       n7=[]
      bad.append(n6)
      bad.append(n7)
         
      print(bad)
      i.append(bad)               
   dono=dono+1
    
    
  return(i)

def ionlyprintthenodes(i) :
  q=1
  for j in i :
   print(q,")",j)
   q=q+1

def ionlyprinttheconnectednodes(i,j):  #See i  and j, j is conn pair 
 q=1
 
 for s in j :
   
   if len(s)>5 :
    print(q,")      Points Connceted are ",i[s[0]]," and ",i[s[1]]," With Loading of",s[5],"As UDL",s[6],"As Point Load")
   
   
   
   if len(s)==5 :
     print(q,")     Points Connceted are ",i[s[0]]," and ",i[s[1]])
   q=q+1  

def connected_nodes(cnv,cnn,ko) :  #make a function to delete conected pair use del command 
  if ko!=0 :
    print("Genral Instructuion if You dont want to add any more pairs and Exit option dosnt show up keep entering previous data upto the point Exit Option Shows")
    B1=float(input("Enter Width of Beam in m"))
    D1=float(input("Enter Depth of Beam in m")) 
    E1=float(input("Enter E value in KN "))
    B2=float(input("Enter Width of Column in m"))
    D2=float(input("Enter Depth of Column in m "))
    E2=float(input("Enter E  of Column in KN "))
    
    AE1=B1*D1*E1
    EI1=(E1*B1*D1*D1*D1)/12
    AE2=B2*D2*E2
    EI2=(E2*B2*D2*D2*D2)/12

    print("/n")
    loadmaster99=int(input("Would You Like To Enter Loads Now if YES Press 1 or any other Digit"))
    
    j=len(cnv)

    dj=j-1
    for s in range(math.factorial(j)) :
     if(ko==0):
       break 
     x=[]
     l=0
     g=0
     ionlyprintthenodes(cnv) #Can Use New Print Feature here
          
     n1,n2=input("Nodes That are connected Enter ',' seprate  ").split(",")
     n1=int(n1)-1
     n2=int(n2)-1
     if n1<0 or n2<0 or n1>dj or n2>dj :
        print("Enter Nodes that are defined ")
        g=1
        l=1

        
     if n1==n2 :
         s=s-1
         
         g=1
         l=1
         print("You Can Not Connect The Same Node")
     if g!=1 :    
      x.append(n1)
      x.append(n2)
      tommy=n1     #cx and cy calculation 
      moose=n2
      qwerty=cnv[tommy]
      rass=cnv[moose]
    
      air=(rass[0]-qwerty[0])
      blast=(rass[1]-qwerty[1])
      air=air*air
      blast=blast*blast
      longle=math.sqrt(air+blast)
      cx=(rass[0]-qwerty[0])/longle
      cy=(rass[1]-qwerty[1])/longle
      

      if cy==0:   #H case 
        n3=EI1
        n4=AE1
        n5=E1
        if(loadmaster99==1) :
          udl=25*B1*D1
          udl2=float(input("Enter the SUM of UDL throughtout the Span"))
          udl=udl+udl2
          n6=udl
          pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
          if (pointloadwant==1) :
                habata=[]
                print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
                etala=int(input(" \n Enter the N.o of Point Loads You want to enter"))          
                for nodooi in range(etala):
                            nrairi=float(input("Enter Load Intensity")  )  
                            oiisaaa=float(input("Enter Load Distance from first node Side"))
                            habata.append(nrairi)
                            habata.append(oiisaaa)              
                n7=[]
                n7=habata
          if pointloadwant!=1 :
            
           n7=[]
                                              
      if cx==0 :   #v case 
        n3=EI2
        n4=AE2
        n5=E2
        if(loadmaster99==1) : #UDL Load Entry 
          udl=25*B2*D2
          udl2=float(input("Enter the SUM of UDL throughtout the Span"))
          udl=udl+udl2
          n6=udl
          pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
          if (pointloadwant==1) :
                habata=[]
                print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
                etala=int(input(" \n Enter the N.o of Point Loads You want to enter"))            
                for nodooi in range(etala) :
                            nrairi=float(input("Enter Load Intensity")    )
                            oiisaaa=float(input("Enter Load Distance from first node  Side"))
                            habata.append(nrairi)
                            habata.append(oiisaaa)              
                n7=[]
                n7=habata

          if pointloadwant!=1 :
            
           n7=[]
                                                
                     
      if cy!=0 and cx!=0  :
       n3=float(input("enter EI of the member in KN-m^2 "))
       n4=float(input("enter AE of the member in KN "))
       n5=float(input("Enter E  of the member  in KN "))
       if(loadmaster99==1) :
          udl=n4/n5           #Udl Load ENtry 
          udl=25*udl
          udl2=float(input("Enter the SUM of UDL throughtout the Span"))
          udl=udl+udl2
          n6=udl
          pointloadwant=int(input("\n Do you want to Enter Point Load Press 1"))
          if (pointloadwant==1) :
                habata=[]
                print("\n IF you are entering lateral load Along X Enter in Column Element and Vice Versa")            
                etala=int(input("\n Enter the N.o of Point Loads You want to enter" ))           
                for nodooi in range(etala) :
                            nrairi=float(input("Enter Load Intensity")   )
                            oiisaaa=float(input("Enter Load Distance from first node Side"))
                            habata.append(nrairi)
                            habata.append(oiisaaa)              
                n7=[]
                n7=habata
          if (pointloadwant!=1) :
                
                n7=[]
                 
                                          
      x.append(n4)
      x.append(n3)
      x.append(n5)# Here you can put only E if you want
      if(loadmaster99==1) :
       
       x.append(n6)
        
       x.append(n7)                                    
      for i in cnn :

        if ((i[0]==x[0])  and (i[1]==x[1])) :
          l=1
          print("Pair Aldready Exists")

        if  ((i[0]==x[1]) and (i[1]==x[0])) :
          l=1
          print("Pair Aldready Exists")
        
     if l!=1 :
      cnn.append(x)
     print("list of connected pairs currently",cnn)
     more="y"
     if s>=(ko-1) :
      more=input("want to connect more nodes y/n")
     if more=='n' or more=='N' or more=='No'  :
      break 
    return(cnn)
    
    
    
def transform_mat(cxx,cyy):
   trs=[cxx,cyy,0,0,0,0,-cyy,cxx,0,0,0,0,0,0,1,0,0,0,0,0,0,cxx,cyy,0,0,0,0,-cyy,cxx,0,0,0,0,0,0,1]
   trs=numpy.asarray(trs) 
   trs=trs.reshape(6,6)

   return(trs)
   
def stiffness_mat(L,EI,AE) :
    stf=[]
    stf=[(AE/L),0,0,(-AE/L),0,0,0,((12*EI)/(L*L*L)),((6*EI)/(L*L)),0,((-12*EI)/(L*L*L)),((6*EI)/(L*L)),0,((6*EI)/(L*L)),((4*EI)/(L)),0,((-6*EI)/(L*L)),((2*EI)/(L)),(-AE/L),0,0,(AE/L),0,0,0,((-12*EI)/(L*L*L)),((-6*EI)/(L*L)),0,((12*EI)/(L*L*L)),((-6*EI)/(L*L)),0,((6*EI)/(L*L)),((2*EI)/(L)),0,((-6*EI)/(L*L)),((4*EI)/(L))]
    stf=numpy.asarray(stf) 
    stf=stf.reshape(6,6)

    return(stf)

def matmulti(T,K) :
   Ttranspose=T.transpose()

   result=numpy.matmul(Ttranspose,K)
   result2=numpy.matmul(result,T)
   
   result2=numpy.asarray(result2) 
   result2=result2.reshape(6,6)
   
   return(result2)



def matdevloper(i,j):
 
 provider=len(j)
 godzilla=[]
 for drdo in range (provider) :
  for drda in range (provider) :
     x=[drdo,drda,0,0]
     godzilla.append(x)
 
 for x in godzilla :
  techy=0
  techy2=0
  for drdr in i  : 
    
   
    if ((drdr[0]==x[0])  and (drdr[1]==x[1])) :
       techy=1
       
         
    if  ((drdr[0]==x[1]) and (drdr[1]==x[0])) :
       techy=1
  if ((techy==0) and (x[0]!=x[1])and (techy2==0)) :
       
       i.append(x)
       
      


 localguy={}   
 jugaad={}
 rain={}
 for s in i :
     arrE=s[2]
     Eii=s[3]
 
     t=[]
     m=[]
     q=[]
     r=[]
     t=s[0]
     m=s[1]
     
     q=j[t]
     r=j[m]
     
     a=(r[0]-q[0])
     b=(r[1]-q[1])
     a=a*a
     b=b*b
     l=math.sqrt(a+b)
     cx=(r[0]-q[0])/l
     cy=(r[1]-q[1])/l
     key1="Klocal"+str(t)+str(m)
     EI=s[2]
      
     
     

     t_mat=transform_mat(cx,cy) #Sending to function to make transformation matrix 
     K_matloc=stiffness_mat(l,Eii,arrE) #Sending to function to make local matrix
     
     K_tran_matloc=matmulti(t_mat,K_matloc)  #Sending to function to multiply matrix
     
     zoozoogo={}
     zombie=("Kloc"+str(t)+str(m))
     zoozoogo={zombie:K_matloc}
     localguy.update(zoozoogo)
     
     sos=[t,m]
     gog=["u","v","w"]
     f=[]
     food=[]
     
     for jos in sos :   #error was using same name again and aGAIN like jklm 
       for kos in  gog :
        for los in sos :
           for mos in gog :
              food.append(kos+str(jos)+mos+str(los))   #Name of Dictionary Key
     food=numpy.asarray(food) 
     food=food.reshape(6,6)    
     
      
     for jake in range (6):
      for jake1 in range (6):
        
           rain={food[jake][jake1]:K_tran_matloc[jake][jake1]}
           if food[jake][jake1]in jugaad.keys(): #if to check if that key is present in jugaad and
              ramos=jugaad.get(food[jake][jake1])
              ramos=ramos+K_tran_matloc[jake][jake1]
              rain={food[jake][jake1]:ramos}
              
           
           jugaad.update(rain)
 keysList=[]
 valuesList=[]
 globalaraysize=(len(j)*3)

 ui=[] #sorting of matrix from 0 to N 
 for hog in range (len(j)):
  ui.append(hog)
  
 sos=ui
 gog=["u","v","w"]
 f=[]
 food=[]
 sortedjugaad={}
 rain={}
 for jos in sos :   #error was using same name again and aGAIN like jklm 
  for kos in  gog :
    for los in sos :
      for mos in gog :
         food.append(kos+str(jos)+mos+str(los))   #Name of Dictionary Key
 for jake in food:
      
      if jake in jugaad.keys(): #if to check if that key is present in jugaad and
              ramos=jugaad.get(jake)
              
              rain={jake:ramos}
              
              sortedjugaad.update(rain)



 return(localguy,sortedjugaad)
def reducermatdev(fp2,thatdictionary) :
   u="u"
   v="v"
   w="w"
   food=[]
   for i in fp2 :
       food.append(u+str(i))
       food.append(v+str(i))
       food.append(w+str(i))
   kewl=[]
   kewl=list(thatdictionary.keys())
   for ina in food :
      for jina in kewl : #checking if that subscript is in the  key is 
         if ina in jina:
            kewl2=[]
            kewl2=list(thatdictionary.keys())
            
            if jina in kewl2 :                      #need to add an exists condition as some keys are previously deleted 
             
             del thatdictionary[jina]
   
   keysList=[]
   valuesList=[]
   #globalaraysize=((len(j)-len(fp2))*3)
   keysList=list(thatdictionary.keys())
   globalaraysize=len(keysList)
   globalaraysize=math.sqrt(globalaraysize)
   globalaraysize=int(globalaraysize)
   valueList=list(thatdictionary.values())
   keysList=numpy.asarray(keysList) 
   keysList=keysList.reshape(globalaraysize,globalaraysize)
   valueList=numpy.asarray(valueList) 
   valueList=valueList.reshape(globalaraysize,globalaraysize) 
   print(keysList)
   print(valueList)
   return(thatdictionary)
    
    
def valueremoverpng() :
 
    nodal_values=[]
    connected_pairs=[]    
    xa=[]
    with open('nodalval.txt','r') as file:
       for line in file:
        
        
         row=ast.literal_eval(line)
         xa.append(row)
       
    nodal_values=xa
    xaa=[]
    with open('conpair.txt','r') as file:
       for line in file:
        
        
         row=ast.literal_eval(line)
         xaa.append(row)
       
    connected_pairs=xaa
    xa=[]
    return(nodal_values,connected_pairs)
    
def deletetheconnectedpair(i,j): #i is conn pair
 ionlyprinttheconnectednodes(j,i) ###################################################
 seeyouagain=int(input("Enter the Node No you want to delete"))-1
 del(i[seeyouagain])
 return(i)

 
def allconnectormagic(nodal_values,connected_pairs) :
  jaabber=0
  jjj=int(input("enter the number of Nodes you want to enter "))
  while(jaabber<jjj) :
 
   x=create_nodes(nodal_values)
   if x==[] :
    jjj=jjj+1
   if x!=[] :
    nodal_values.append(x)
   jaabber=jaabber+1

  print("The Nodal Values are ",nodal_values)  #for loop here for Pairs of Diff D,D,E
  lo_number=int(input("enter the No of Pairs You want to connect of Same Specs Like B,D,E"))
  
  cp=connected_pairs
  length_of_nodalvalues=(nodal_values)
  connected_pairs=connected_nodes(length_of_nodalvalues,cp,lo_number)
  if os.path.exists("nodalval.txt"):
   os.remove("nodalval.txt")
  nnnvalues=nodal_values
   # open file
  with open('nodalval.txt','w+') as f:
    	# write elements of list
   for items in nnnvalues:
        f.write('%s\n' %items)
   f.close()        
  if os.path.exists("conpair.txt"):
   os.remove("conpair.txt")
  cnnpair=connected_pairs
   # open file
  with open('conpair.txt','w+') as f:
      # write elements of list
    for items in cnnpair:
      f.write('%s\n' %items)	# close the file
  f.close()

  return(connected_pairs,nodal_values)



def allidoisjustsave(connected_pairs,nodal_values):
  
  if os.path.exists("nodalval.txt"):
    
    os.remove("nodalval.txt")
  nnnvalues=nodal_values
   # open file
  with open('nodalval.txt','w+') as f:
    	# write elements of list
   for items in nnnvalues:
        f.write('%s\n' %items)
        
   f.close()        
  if os.path.exists("conpair.txt"):
   os.remove("conpair.txt")
  cnnpair=connected_pairs
   # open file
  with open('conpair.txt','w+') as f:
      # write elements of list
    for items in cnnpair:
      f.write('%s\n' %items)	# close the file
  f.close() 

def fixerofpoints(fixedpoints) :
       kasukabe=int(input("Enter No of Fixed Points"))
       for kasukabe2 in range (kasukabe) :
        kasukabe3=int(input("Enter Fixed Point"))
        kasukabe3=kasukabe3-1
        fixedpoints.append(kasukabe3)    
       return(fixedpoints)
    

#def leftoutrightup(i,j)
def loadmakergod(quo,T) :
   
   Ttranspose=T.transpose()
   result=numpy.matmul(Ttranspose,quo)
   
   return(result)
   

def udlloadmaker(l,udl) :
    asf=[]
    w=udl
    asf=[0,(-w*l/2),(-w*l*l/12),0,(-w*l/2),(w*l*l/12)]
    asf=numpy.asarray(asf) 
    asf=asf.reshape(6,1)
 
    
    return(asf)



def dictionarysimplifierop007(t,m,thatloadmatrix,jugaad) :
    
    sos=[t,m]
    gog=["u","v","w"]
    f=[]
    food=[]     
    for jos in sos :   #error was using same name again and aGAIN like jklm 
       for kos in  gog :

              food.append(kos+str(jos))   #Name of Dictionary Key
    food=numpy.asarray(food) 
    food=food.reshape(6,1) #making  a matrix of keys for dictionary    
     
      
    for jake in range (6):
      for jake1 in range (1):
        
           rain={food[jake][jake1]:thatloadmatrix[jake][jake1]}
         
           if food[jake][jake1]in jugaad.keys(): #if to check if that key is present in jugaad and
              ramos=jugaad.get(food[jake][jake1])
              ramos=ramos+thatloadmatrix[jake][jake1]
              rain={food[jake][jake1]:ramos} 
      
      jugaad.update(rain)
    return(jugaad)  
def pointloadmaker(l,too):
    
    kobra=len(too)-1
    
    i=0
    a=0
    b=0
    c=0
    d=0
    asf=[]
    while i<=kobra :
          
          
          w=too[i]
          LS=too[i+1]
          RS=l-LS
          a=a+((-w*RS*RS*(RS+(3*LS)))/(l*l*l))
          b=b+((-w*LS*RS*RS)/(l*l))
          c=c+((-w*LS*LS*(LS+(3*RS)))/(l*l*l))
          d=d+((-w*RS*LS*LS)/(l*l))
          
          i=i+2
          
    asf=[0,a,b,0,c,d] 
    

    asf=numpy.asarray(asf) 
    asf=asf.reshape(6,1)
    return(asf)                                                
                                                    


   
def loadmatrixgene(i,j):
 jugaad={}
 sortedjugaad={}
 localguy={}
 rain={}
 for s in i :
    if len(s)==5 :
     boo=0
     too=[]
    if len(s)>5 : 
     boo=s[5]  #better to make a fiffrent function to add all weights #while calculating if no loads can give an option to enter 
     if s[6]!=[] : 
      too=s[6]  #Need to put a checker that length is < then Calculated length # in further steps make sure that length is not 
     if s[6]==[] :
      too=[]

    t=[]
    m=[]
    q=[]
    r=[]
    t=s[0]
    m=s[1]
     
    q=j[t]
    r=j[m]
     
    a=(r[0]-q[0])
    b=(r[1]-q[1])
    a=a*a
    b=b*b
    l=math.sqrt(a+b)
    cx=(r[0]-q[0])/l
    cy=(r[1]-q[1])/l
    t_mat=transform_mat(cx,cy)
   
    kokomelon=[]
    kokomelon=udlloadmaker(l,boo) #need to return reshaped matrix
    thatloadmaker=[]
    thatloadmatrix=loadmakergod(kokomelon,t_mat)

    
    jugaad=dictionarysimplifierop007(t,m,thatloadmatrix,jugaad)  #function to put array values to the dictionary 
    
    kokomelon2=[]
    kokomelon2=pointloadmaker(l,too)
    thatloadmaker=[]
    thatloadmatrix=loadmakergod(kokomelon2,t_mat)
    jugaad=dictionarysimplifierop007(t,m,thatloadmatrix,jugaad)
    
    greatkokomelon=[]
    greatkokomelon=kokomelon+kokomelon2
    
    
    zoozoogo={}  
    zombie=("Klocload"+str(t)+str(m))
    zoozoogo={zombie:greatkokomelon}
    localguy.update(zoozoogo)
    


    
    
    
 

 #To Arrange Jugaad

 ui=[] #sorting of matrix from 0 to N 
 for hog in range (len(j)):
  ui.append(hog)
  
 sos=ui
 gog=["u","v","w"]
 f=[]
 food=[]
 sortedjugaad={}
 rain={}
 for jos in sos :   #error was using same name again and aGAIN like jklm 
  for kos in  gog :

         food.append(kos+str(jos))   #Name of Dictionary Key
 for jake in food:
      
      if jake in jugaad.keys(): #if to check if that key is present in jugaad and
              ramos=jugaad.get(jake)
              
              rain={jake:ramos}
              
              sortedjugaad.update(rain)
 
  #return Local Matrix also
 return(localguy,sortedjugaad)    
def ijustfixtheloadtofixedpoints(fp2,thatdictionary) :
   u="u"
   v="v"
   w="w"
   food=[]
   
   for i in fp2 :
       food.append(u+str(i))
       food.append(v+str(i))
       food.append(w+str(i))
   kewl=[]
   kewl=list(thatdictionary.keys())
   for ina in food :
      for jina in kewl : #checking if that subscript is in the  key is 
         if ina in jina:
            kewl2=[]
            kewl2=list(thatdictionary.keys())
            
            if jina in kewl2 :                      #need to add an exists condition as some keys are previously deleted 
             
             del thatdictionary[jina]
   
   
   keysList=[]
   valuesList=[]
   #globalaraysize=((len(j)-len(fp2))*3)
   keysList=list(thatdictionary.keys())
   valueList=list(thatdictionary.values())
   globalaraysize=len(keysList)
   globalaraysize=int(globalaraysize)
   keysList=numpy.asarray(keysList) 
   keysList=keysList.reshape(globalaraysize,1)
   valueList=numpy.asarray(valueList) 
   valueList=valueList.reshape(globalaraysize,1) 
   print(keysList)
   print(valueList)
            
   return(thatdictionary)
  
def ijustmultiplytheloadandstiffnessmatrix(load,stf):
 keyst=list(stf.values())
 globalaraysize1=len(keyst)
 
 globalaraysize1=math.sqrt(globalaraysize1)
 globalaraysize1=int(globalaraysize1)
 keyst=numpy.asarray(keyst)
 keyst=keyst.reshape(globalaraysize1,globalaraysize1)
 keylo=list(load.values())
 globalaraysize=len(keylo)
 globalaraysize=int(globalaraysize)
 keylo=numpy.asarray(keylo)
 keylo=keylo.reshape(globalaraysize,1)
 

 
 keysti=numpy.linalg.inv(keyst)
 keysti=numpy.asarray(keysti)
 keysti=keysti.reshape(globalaraysize1,globalaraysize1)
 
 
 
 result=numpy.matmul(keysti,keylo)
 print("THIS IS THE FINAL RESULT")
 print(result)

 
 sortedresult={}
 resultkeys=list(load.keys())

 for iso in range(len(resultkeys)) :
    zabuza={}
    zabuza={resultkeys[iso]:result[iso][0]}
    sortedresult.update(zabuza)
 print(sortedresult)
 return(sortedresult)
 
 


 
def itsnotoveryetlocalguy(defle,loclo,locstf,i,j) :
   
   jessica={}
   for s in i :
     
    t=[]
    m=[]
    q=[]
    r=[]
    t=s[0]
    m=s[1]


    harvey={}
    
    mike=0
    rachel=0
    
    zombie=("Kloc"+str(t)+str(m))
    zombie2=("Klocload"+str(t)+str(m))
    
    if (s[2]!=0 and s[3]!=0):
        
        
        if zombie2 in loclo :
           
           harvey=loclo.get(zombie2)
           harvey=list(harvey)
           harvey=numpy.asarray(harvey)
           harvey=harvey.reshape(6,1)
           louis=harvey
           
           
           
           mike=1

        if zombie in locstf :
          
           harvey=locstf.get(zombie)
           harvey=list(harvey)
           harvey=numpy.asarray(harvey)
           harvey=harvey.reshape(6,6)
           litt=harvey
           
           
           ross=1


        sos=[t,m]
        gog=["u","v","w"]
        f=[]
        food=[]     
        for jos in sos :   #error was using same name again and aGAIN like jklm 
           for kos in  gog :
        
              food.append(kos+str(jos))   #Name of Dictionary Key

        harry=[]

        for draco in food :


           if draco in defle :
              harvey=defle.get(draco)
              harry.append(harvey)

           if draco not in defle :
              harry.append(0)
              
        
        harry=numpy.asarray(harry)
        
        harry=harry.reshape(6,1)
        
        rachel=numpy.matmul(litt,harry)
        
        rachel=rachel-louis
        
        

        sos=[t,m]
        gog=['R1','R2','M']
        drake=[]
        for jos in sos :   #error was using same name again and aGAIN like jklm 
           for kos in  gog :
              drake.append(kos+str(t)+str(m)+str(jos))  #need some change out here to cut overlapping  encrypt key use this to get value then compare using cx cy l 
              
          
        
         
        for jonny in range(len(drake)) :
           walker={}
           walker={drake[jonny]:rachel[jonny][0]}
           jessica.update(walker)

              

  

   
        
   print(jessica)
   return(jessica)




       #extract values from defle and then calculate

           
    


    



    

    





 


def iamreallyprintingnotcalculating(i,j,a,b,c,d,e,f,g) :  #(connected_pairs,nodal_values,stmglobal,stmlocal,stmglobalr,loadglobal,loadlocal,loadlocalr,resultnaruto)  
   son=1
   while son==1 :
     
     print("\n \n1)    Press 1 to print nodes and loading ")
     print("2)         Press 2 to print global stiffness matrix  ")
     print("3)         Press 3 to print reduced global stiffness matrix")
     print("4)         Press 4 to print global load matrix and reduced load matrix")
     print("5)         Press 5 to print Deflection ")
     print("6)         Press 6 to Exit ")

     # use # while changing print in the math function 




  

    
#Main  
nodal_values=[] 
connected_pairs=[]
stmglobal={}
stmlocal={}
stmglobalr={}
loadlocal={}
loadglobal={}
loadglobalr={}
defle={}
reaxandmoms={}
doyouwannaexit='y'
while(doyouwannaexit!='n' or doyouwannaexit!='N'):
 print("\n \n1)   If you want to use old values from previous session  Press 1")
 print("2)   If you want to enter new nodes Press 2")
 print("3)   If you want to do Normal Maths Press 3")
 print("4)   If you want to Modify Loading or Delete Connected Nodes  Press 4")
 print("5)   If  you want to View Nodes and Connected Nodes Press 5")
 
 print("6)   To exit Press 6")
 
 sks=int(input("\n Enter Your Selection"))
 if sks== 1 :
    
    (nodal_values,connected_pairs)=valueremoverpng()
    print(" \n The Connected  Nodes are ",connected_pairs)   #Need to create a function to print these values in a proper way 
    print("\n The Nodal Values are",nodal_values)
    
    #Ask if they want to enter new values to the previous values
    #sks=int(input("\n If you want to enter  more values Press 2 or Enter any other No")) 
    #if sks!=2 :
     #sks=1
  
 if sks==2  :
    (connected_pairs,nodal_values)=allconnectormagic(nodal_values,connected_pairs)
    print("\n The Connected  Nodes are ",connected_pairs)
    print("\n The Nodal Values are",nodal_values)  #Need to create a function to print these values in a proper way 
    #sks= int(input("\n If you want to use the given memebr and noal values to calculate further 3 Enter any other No"))
    #if sks!=3 :
     #sks=2
 
 if sks==5 :
   print(connected_pairs)
   ionlyprinttheconnectednodes(nodal_values,connected_pairs)


#Normal Code to Save and Make Nodes Upto This Point 

 if (sks==3) :

     
     #stmglobal={}
     #stmlocal={}
     #stmglobalr={} all are predefined at start of Main 
     print((" \n Press 1 if You want to enter fixed points for the above case" ))
     fixedbarsinit=int(input("Enter Your Choince"))
     fixedpoints=[]               
     if fixedbarsinit==1 :
         fixedpoints=fixerofpoints(fixedpoints) 
     
     if fixedbarsinit!=1 :
       fixedpoints=[]
     
     (stmlocal,stmglobal)=matdevloper(connected_pairs,nodal_values) #to get Local and  Total Global Matrix 
      #To get Fixed Points   #ask and make a function


     stmglobalr=reducermatdev(fixedpoints,stmglobal) #Global Matrix   #Need to make change that nodal values dont go
     (loadlocal,loadglobal)=loadmatrixgene(connected_pairs,nodal_values)
     (loadglobalr)=ijustfixtheloadtofixedpoints(fixedpoints,loadglobal)
     
     defle=ijustmultiplytheloadandstiffnessmatrix(loadglobalr,stmglobalr)
     
     reaxandmoms=itsnotoveryetlocalguy(defle,loadlocal,stmlocal,connected_pairs,nodal_values)

     
     jackma=int(input("Do you want to print out the results Press 1"))
     if jackma==1 :
             iamreallyprintingnotcalculating(connected_pairs,nodal_values,stmglobal,stmlocal,stmglobalr,loadglobal,loadlocal,loadlocalr,resultnaruto)   
     #loadlocal={}
     #loadglobal={}
     #loadglobalr={}
     #defle
     #reaxandmoms        

 if sks==4:
    print("\n \n1)   If you want to Enter Loads to all Press 1")
    print("2)   If you want to Enter orModify Loads to Seected Members Press 2 2")
    print("3)   If you want to Delete a Member Press 3")
    givingmoreoptions=int(input("Enter Your Choice"))
    if givingmoreoptions==2 :
      connceted_pairs=updateloadismorefunny9(connected_pairs,nodal_values)
    if givingmoreoptions==1 :
     connected_pairs=newallloadenterfunny(connected_pairs,nodal_values)
    if givingmoreoptions==3 :
      deletetheconnectedpair(connected_pairs,nodal_values)

    
    allidoisjustsave(connected_pairs,nodal_values)
 
    #Make a Saving Funciton 
 
 if sks==6 :
    doyouwannaexit=input("Do you want to exit the Process Y/N")
    
    if ((doyouwannaexit=='Y') or (doyouwannaexit=='y')) :
        break
    print("The Values of this session will be used in the further process of continuing the session")
    doyouwannadomath='N'
    if ((doyouwannadomath=='N') or (doyouwannadomath=='n')) :
      donothing=0 #Goes Back to start of Loop





 if ((sks!=1) and (sks!=2)and (sks!=3) and (sks!=4)): #To go to Main loop start 
   donothing=0     #Goes Back to start of Loop 
   
 

#Add instruction that the Program shows your entered value of 1 as 0 but you enter 1 only 



 
