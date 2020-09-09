def hoge():
    hogestr = 'hoge'
    return 1

i = hoge()
#関数内でただ単に宣言された変数はローカルであり、
#関数の外ではスコープ外になる
#アクセスできない
#print(hogestr)
