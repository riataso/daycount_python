#佐藤　来
T,S,E = map(int,input().split()) #ある時刻、開始と終了時刻の値、取得
mft = 0

def time_check(S,E): #時間を一直線上にそろえる
    if S > E:
        return S + (24-S) + E 
    else :
        return E

        
def time_set(T):
    return T + (24-T) + T
    

if T >= S and T < E :
    print("含まれる") 
elif T == E == S :
    print("含まれる")
elif T > S or T < E :
    mft =time_check(S,E)
    T = time_set(T)
    if T >= S and T < int(mft):
         print("含まれる") 
    else :
        print("含まれない")
else :
    print("含まれない")
