for i in range(3): #コロンが入っていることに注意
    
    
    name=input("名前を教えて下さい")
    waist=float(input("腹囲は？"))
    age=int(input("年齢は？"))


    print(name, "さんは腹囲", waist, "cmで年齢は",age, "才ですね。")


    if age>=40 and waist>=85:
        print(name,"さん、内臓脂肪蓄積注意です")
    elif age>=40 and waist<=50:
        print(name,"さん、痩せ気味")
    else:
        print(name,"さん、腹囲は問題ありません")


