#To do list
import sqlite3 as sq
import datetime


conn=sq.connect('to_do_item.db')

cursor=conn.cursor()

def create_table():
	query='''  create table if not exists TodoItem(todo_id INTEGER primary key autoincrement ,todo_item text ,todo_date date) '''
	cursor.execute(query)
	conn.commit()

def add_item():
	item=input('Enter the item::')
	d=datetime.date.today()
	query="insert into TodoItem('todo_item','todo_date') values('%s','%s')"%(item,d)
	cursor.execute(query)
	conn.commit()
def delete():
	item=int(input('enter no to delete item::'))
	query='''delete from TodoItem where todo_id='%d' '''%(item)
	cursor.execute(query)
	conn.commit()
def display():
	print("--------TO DO ITEM--------")
	print('NO.| Item     |    Date')
	print("-"*30)
	query="select * from TodoItem";
	cursor.execute(query)
	data=cursor.fetchall()
	for i in data:
		print(i[0]," | ",i[1]," | ",i[2])
def update():
	item=int(input('Enter the item no to update::'))
	d=datetime.date.today()
	new_item=str(input('Enter the new item::'))
	query=''' update TodoItem set todo_item='%s' , todo_date='%s'  where todo_id='%d' '''%(new_item,d,item)
	cursor.execute(query)
	conn.commit()
if __name__=='__main__':
	create_table()
	fetch_data()
	while True:
		print("1.add item\n2.delete item\n3.display item\n4.update")
		no=input()
		try:
			no=int(no)
		except:
			add_item_arg(no)
		if no==1:
			add_item()
		elif no==2:
			delete()
		elif no==3:
			display()
		elif no==4:
			update()
		else:
			print('invalid choice')
			