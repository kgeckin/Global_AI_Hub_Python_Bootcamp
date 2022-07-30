import pandas as pd
import numpy as np
import openpyxl

#matematik dersi notları
ogrenci_adi=np.array(["Sinan","Harun","Talha","Kardelen","Melisa"])
ogrenci_soyadi=np.array(["Şahin","Çakılcı","Meydanal","Geçkin","Kavak"])
ogrenci_okulnum=np.array([1,2,3,4,5])
ogrenci_sinavpuani=np.array([20,90,78,50,65])

dictionary={"Ad":ogrenci_adi,
            "Soyad":ogrenci_soyadi,
            "Okul Numarası":ogrenci_okulnum,
            "Sınav Puanı":ogrenci_sinavpuani}

df=pd.DataFrame(dictionary)
df

df2=[]
for i in ogrenci_sinavpuani:
  if i >= 80:
    df2.append("Geçti")
    print("A ile Geçti")

  elif i<80 and i>69:
    df2.append("Geçti")
    print("B ile Geçti") 
  elif i<70 and i>59:
    df2.append("Geçti")
    print("C ile Geçti") 
  elif i<60 and i>49:
    df2.append("Kaldı")
    print("D ile Kaldı") 
  else:
    df2.append("Kaldı")
    print("F ile Kaldı")

df2

df["Geçti mi?"]=df2

df

df.to_excel("GlobAIHubProje1.xlsx")
