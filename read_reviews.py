# reviews.txt裡面有一百萬筆留言
# 如果檔案裏面有一大堆資料，最好建立一個空清單，以便之後可以印出第0,1 ,2...筆資料
# 改成每讀1千筆印出1千次單位長度

data = []
count = 0   # 計數開始等於0一定要寫在with之外                          
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)  # 把line加進data空清單，因為在for回圈內所以每跑一行就加進data空清單裡面
		count += 1         # 每跑一次for迴圈就計數一次
		if count % 1000 == 0: # 1000除以count所得之餘數 == 0(即count是1000的倍數。例如7 % 3 == 1 )。不要忘記指令後要加冒號。
			print(len(data))   # 如果此寫在for回圈內，代表每讀一筆留言就印1次單位長度，1百萬筆留言就會印1百萬次單位長度，程式會跑很慢。
print('檔案讀取完了，組共有', len(data), '筆留言')

# 求每一筆留言的平均字數
sum_word = 0
for word in data:  # 為什麼不是in f或 in line? 因為我們要讀取f裡的每筆留言，而每筆留言又存進了data空清單內，故現在要求data空清單內每筆留言的字數
	sum_word += len(word)  # sum_word = sum_word + len (word)。不可以寫sum_word += word，因為要求word的長度。
print('每筆留言的平均字數為', sum_word / len(data),'個字')	
