def _contrast(userName,piaKey):
    print("%s try to login, password is %s"%(userName,piaKey))
    pubKey=open("public.key",'r',encoding='utf-8').read()
    pubKey , piaKey=list(pubKey),list(piaKey)
    for i in range(len(pubKey)):
        pubKey[i]=ord(pubKey[i])
    for i in range(len(piaKey)):
        piaKey[i]=ord(piaKey[i])
    if len(piaKey)<len(pubKey):
        while len(piaKey)<len(pubKey): piaKey.append(0)
    else:
        while len(piaKey)>len(pubKey): pubKey.append(0)
    pwd=[]
    ganyupwd=[1027, 1124, 1144, 1144, 1099, 1105, 1134, 1176, 1112, 1115, 1165, 1257, 1204, 1204, 1256, 1170, 1190, 1187, 1279, 1257, 1251, 1256, 1277, 1252, 1185, 1198, 1183, 1185, 1152, 1251, 1183, 1279, 1152, 1204, 1190, 1251, 1257, 1167]
    #yclpwd=[1100, 1209, 1212, 1092, 1090, 1104, 1124, 1175, 1190, 1185, 1251, 1257, 1204, 1204, 1256, 1170, 1190, 1187, 1279, 1257, 1251, 1256, 1277, 1252, 1185, 1198, 1183, 1185, 1152, 1251, 1183, 1279, 1152, 1204, 1190, 1251, 1257, 1167]
    if userName=="Gan_yu":
        pwd.append(ganyupwd)
    #elif userName=="quest":
    #    pwd.append(yclpwd)
    else:
        return False
    PWDsymbol=True
    for ls in pwd:
        PWDsymbol=True
        for i in range(len(pubKey)):
            if ls[i]!=(piaKey[i]+pubKey[i])^5+1213:
                PWDsymbol=False
                break
        if PWDsymbol:
            return True
    return False
def loginAndCommand(string):
    string=string.split(sep='&')
    if string[0].lower()!="login":
        return False
    if _contrast(string[1],string[2].lower()):
        return "OK"
    return "Password Wrong"