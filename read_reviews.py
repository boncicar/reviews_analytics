# reviews.txt裡面有一百萬筆留言
# 如果檔案裏面有一大堆資料，最好建立一個空清單，以便之後可以印出第0,1 ,2...筆資料

data = []                             
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)  # 每一行加進data空清單裡面 
		print(len(data))   # 如果此寫在for回圈內，代表每讀一筆留言就印1次單位長度，1百萬筆留言就會印1百萬次單位長度，程式會跑很慢。
