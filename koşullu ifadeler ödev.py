#!/usr/bin/env python
# coding: utf-8

# # 1. şık cevabı

# In[11]:


A= float(input("SICAKLIK DEĞERİNİ GİRİNİZ:"))
B= str(input("SICAKLIK BİRİMİNİ YAZINIZ(C YADA F):"))
D= float(A)
C= float((5/9) * (D - 32))
F= float((D*9/5))+32
if  B == ("C"):
    print("GİRMİŞ OLDUĞUNUZ {}C= {}'DİR.".format(D,F))
elif B==("F"):
    print("GİRMİŞ OLDUĞUNUZ {}F= {}'DİR'.".format(D,C))
else :
    print ("HATALI BİRİM GİRDİNİZ.DOĞRU DEĞERİ GİRİNİZ( C YADA F)")
    B= str(input("SICAKLIK BİRİMİNİ YAZINIZ(C YADA F):"))
    if   B == ("C"):
         print("GİRMİŞ OLDUĞUNUZ {}C= {}'DİR.".format(D,F))
    elif B==("F"):
         print("GİRMİŞ OLDUĞUNUZ {}F= {}'DİR'.".format(D,C))


# In[12]:


A= float(input("SICAKLIK DEĞERİNİ GİRİNİZ:"))
B= str(input("SICAKLIK BİRİMİNİ YAZINIZ(C YADA F):"))
D= float(A)
C= float((5/9) * (D - 32))
F= float((D*9/5))+32
if  B == ("C"):
    print("GİRMİŞ OLDUĞUNUZ {}C= {}'DİR.".format(D,F))
elif B==("F"):
    print("GİRMİŞ OLDUĞUNUZ {}F= {}'DİR'.".format(D,C))
else :
    print ("HATALI BİRİM GİRDİNİZ.DOĞRU DEĞERİ GİRİNİZ( C YADA F)")
    B= str(input("SICAKLIK BİRİMİNİ YAZINIZ(C YADA F):"))
    if   B == ("C"):
         print("GİRMİŞ OLDUĞUNUZ {}C= {}'DİR.".format(D,F))
    elif B==("F"):
         print("GİRMİŞ OLDUĞUNUZ {}F= {}'DİR'.".format(D,C))


# # 2.ŞIK CEVABI

# In[56]:


A=input("BİR KELİME YAZINIZ:")
for x in range(len(A)-1,-1,-1):
    print(A[x], end ="")  #SOR: LEN KARAKTER SAYISI DEĞİLMİ NEDEN RANGE DÖNGÜSÜNDE HARF OLARAK ALGILANIYOR.
 

    


# #  3.ŞIK CEVABI

# In[67]:


A=1
B=1
print(A)
print(B)
İ=2
while İ<=50:
    A,B=B,A+B
    print(B)
    İ=İ+1


# # 4. ŞIK CEVABI

# In[83]:


A=input("BİR SAYI GİRİNİZ:")
B=0
while B<10:
    for İ in range(1,11):
        print(str(A),"x",str(İ),"=",int(A)*İ)
        B=B+1
    


# # 5. ŞIK CEVABI

# In[86]:


ALİ=[x**3 if x%2==0 else x**2 for x in range(1,20)]
print(ALİ)

