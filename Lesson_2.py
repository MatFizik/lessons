# #Задание 1
# s=input("Введите фразу:")
# m=0
# temp=0
# index=0
# for i in range(len(s)):
#     if s[i]==" " :
#         if temp>m:
#             m=temp
#             index=i-1
#         temp=0
#     else:
#        temp+=1
#        if i==len(s)-1:
#            if temp>m:
#             m=temp
#             index=i
# print("Результат:",s[index-m+1:index+1])

#Задание 2

# s=input("Введите фразу:")
# m=0
# temp=0
# index=0
# for i in range(len(s)):
#     if s[i]==";" :
#         if temp>m:
#             m=temp
#             index=i-1
#         temp=0
#     else:
#        temp+=1
#        if i==len(s)-1:
#            if temp>m:
#             m=temp
#             index=i
# print("Результат:",s[index-m+1:index+1])

#Задание 3
# st=input("Введите фразу:")
# sim=input("Введите символ:")
# m=1000000
# temp=0
# index=0
# for i in range(len(st)):
#     if st[i]==sim :
#         if temp<m:
#             m=temp
#             index=i-1
#         temp=0
#     else:
#        temp+=1
#        if i==len(st)-1:
#            if temp<m:
#             m=temp
#             index=i
# print("Результат:",st[index-m+1:index+1])

#Задание 4
# st=input("Введите фразу:")
# slovo=input("Введите слово:")
# cn = 0
# for i in range(len(slovo)):
#     cn+=1
# print("Слово находится в диапозоне: ",st.find(slovo), ":", st.find(slovo)+cn)

#Задание 5
# s=input("Введите строку:")
# print("Результат:",s.count(' ')+1)