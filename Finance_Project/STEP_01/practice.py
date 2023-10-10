import matplotlib.pyplot as plt

#plt.plot([1, 2, 3, 4])
#plt.show()

# 이때까지 그렸던 plot 지우기
#plt.clf()


# x, y가 다를 때
x = [1, 2, 3, 4]
y = [2, 4, 8, 16]
plt.plot(x, y)
#plt.show()
plt.clf()

# 제목 + 각 축의 설명
plt.plot(x, y)
plt.title("TEST")

plt.ylabel('y label')
plt.xlabel('x label')

#plt.show()

# 파일로 저장하기
# 주의사항 : show()를 하지 말고 저장해야 함
plt.savefig('filename.png')