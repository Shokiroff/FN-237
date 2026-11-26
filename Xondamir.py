def Juft():
    ls = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    cnt = 0
    for x in ls:
        if x % 2 == 0:
            cnt += 1
    if cnt == 0:
        print("Juft sonlar mavjud emas")
    else:
        print(f"Juft sonlar: {cnt}")
if __name__ == "__main__":
    Juft()
