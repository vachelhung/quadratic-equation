'''
此程式可簡易繪製一元二次方程式圖形並顯示極點座標
請按照程式提示輸入相關數值
______________________________
有關特性：
y=x**2+2*x+2
轉換成
y=a(x+h)**2+k
a!=0 && (h,k)為二次曲線頂點
a>0表示開口向上
a<0表示開口向下
a的絕對值越大，開口越小
y=(x+1)**2+1
______________________________
2018/10/18 by vachelhung
email：vachelhung@gmail.com
'''
import matplotlib.pyplot as plt
import numpy as np
x=np.arange(-10,11,1)
y=np.empty(21)
try:
    print("請將方程式轉換為指定形式，並輸入x，y之外的未知數：y=a(x+h)**2+k")
    func1__matrix = np.array([float(input("a=")), float(input("h=")), float(input("k="))])
    print(func1__matrix)
    a, h, k = func1__matrix[0], func1__matrix[1], func1__matrix[2]
    if a==0:
        print("二次項係數為0，不適用此方程式求圖形，請重新輸入")
    else:
        y=a*(x+h)**2+k
        if a>0:
            print("曲線開口向上")
        else:
            print("曲線開口向下")
        print("極點發生在：[",-1*h,",",k,"]的位置上")
        plt.plot(x,y)
        plt.grid()
        plt.show()
except ValueError:
    print("請重新執行程式並輸入阿拉伯數字")