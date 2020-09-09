from time import sleep

globalvar = "global"

def f():
    #グローバル変数を参照することはできる
    localvar = globalvar
    print(localvar)

    #しかし、普通にグローバル変数に代入することは無理(やるならglobal指定が必要)
    #同じ名前の変数を使いたいなら関数定義直後に初期化する必要がある
    #そこから先はまた別の変数として、ローカル変数として扱われる
    #globalvar = "hoge"
    #print(globalvar)


print(globalvar)

f()

print(globalvar)
