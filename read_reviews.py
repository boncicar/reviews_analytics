# reviews.txt裡面有一百萬筆留言
# 如果檔案裏面有一大堆資料，最好建立一個空清單，以便之後可以印出第0,1 ,2...筆資料

data = []                             
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)  # 每一行加進data空清單裡面 
print(len(data))           # 印出reviews.txt有幾行留言(一行會有一筆留言)。print(data)會印出全部的留言
print(data[0])             # 印出第一筆留言
print('--------------')    # 印出分隔線
print(data[1])             # 印出第二筆留言

