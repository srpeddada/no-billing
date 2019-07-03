list1=list(map(int,input().split(",")))
list2=[];count=0;dict1={};flag=0;poss=1;done=0
list3=[1,2,3,4,5,6,7,8,9,10,11,12]
list4=[31,28,31,30,31,30,31,31,30,31,30,31]
dict1=dict(zip(list3,list4))
#print(dict1)
def dele(n):
    for j in range(len(list1)):
        if list1[j]==n:
            list2.append(list1[j])
            del list1[j]
            break
i1=0
for i in range(1,-2,-1):
    if done==1:
        break
    if i1==1:
        i1=0
        list1.append(list2[len(list2)-1])
        del list2[len(list2)-1] 
    if i in list1:
        dele(i)
        i1=1
        k1=0
        for k in range(9,-2,-1):
            if done==1:
                break
            if k1==1:
                k1=0
                list1.append(list2[len(list2)-1])
                del list2[len(list2)-1]
            if k in list1:
                if (i*10)+k<=12 and (i*10)+k > 0:
                    dele(k)
                    #print((i*10)+k,list1,list2,"month")
                    if len(list2)==0:
                        done=1
                    k1=1
                    l1=0
                    for l in range(3,-2,-1):
                        if done==1:
                            break
                        if l1==1:
                            l1=0
                            list1.append(list2[len(list2)-1])
                            del list2[len(list2)-1]
                            #print("helo")
                        if l in list1:
                            dele(l)
                            l1=1
                            m1=0
                            for m in range(9,-2,-1):
                                if done==1:
                                    break
                                #print(m)
                                if m1==1:
                                    m1=0
                                    list1.append(list2[len(list2)-1])
                                    del list2[len(list2)-1]
                                if m in list1:
                                    #print(dict1[(i*10)+k])
                                    if (l*10)+m <= dict1[(i*10)+k] and (l*10)+m > 0:
                                        dele(m)
                                        m1=1
                                        #print((l*10)+m,list1,list2,"date")
                                        if len(list2)==2:
                                            done=1
                                        o1=0
                                        for o in range(2,-2,-1):
                                            if done==1:
                                                break
                                            if o1==1:
                                                o1=0
                                                list1.append(list2[len(list2)-1])
                                                del list2[len(list2)-1]
                                            if o in list1:
                                                #print(o)
                                                dele(o)
                                                o1=1
                                                r1=0
                                                for r in range(9,-2,-1):
                                                    if done==1:
                                                        break
                                                    if r1==1:
                                                        r1=0
                                                        list1.append(list2[len(list2)-1])
                                                        del list2[len(list2)-1]
                                                    if r in list1:
                                                        if (o*10)+r<=23 and (o*10)+r > 0 :
                                                            dele(r)
                                                            r1=1
                                                            #print((o*10)+r,list1,list2,"hour")
                                                            if len(list2)==4:
                                                                done=1
                                                            p1=0
                                                            for p in range(6,-2,-1):
                                                                if done==1:
                                                                    break
                                                                if p1==1:
                                                                    p1=0
                                                                    list1.append(list2[len(list2)-1])
                                                                    del list2[len(list2)-1]
                                                                if p in list1:
                                                                    dele(p)
                                                                    p1=1
                                                                    q1=0
                                                                    for q in range(9,-2,-1):
                                                                        if q1==1:
                                                                            q1=0
                                                                            list1.append(list2[len(list2)-1])
                                                                            del list2[len(list2)-1]
                                                                        if q in list1:
                                                                            if (p*10)+q<=60:
                                                                                dele(q)
                                                                                q1=1
                                                                                #print((p*10)+q,list1,list2,"min")
                                                                                done=1
                                                                                break


if len(list2)<8:
    print(0)  
else:                                     
    print(list2[0],list2[1],"/",list2[2],list2[3]," ",list2[4],list2[5],":",list2[6],list2[7],sep='')
