import cv2

print("**임계값1 이하는 모두 제외**")
imgye1 = int(input("임계값 1 : "))
print("**임계값2 이상은 모두 간주**")
imgye2 = int(input("임계값 2 : "))

togi = cv2.imread("./togi.jpg", cv2.IMREAD_COLOR)

filecount = 1

for i in range(1, imgye1+1): 
    for j in range(1, imgye2+1):
        transtogi = cv2.Canny(togi, i, j)
        filename = "./file/file%d_(%d, %d).jpg" %(filecount, i, j)
        cv2.imwrite(filename, transtogi)
        print("%d" %filecount)
        filecount += 1

print("작업이 종료되었습니다.")