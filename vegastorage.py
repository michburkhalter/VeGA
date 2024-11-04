import sqlite3


class VegaStorage:
	
	def __init__(self):
		self.init_rides_table()
		print(self.get_rides())

	def add_one_ride(self):
		print("add_one_ride")
		cnt = self.get_rides()
		cnt = cnt + 1

		self.open_db()
		self.cursor.execute("UPDATE rides SET count = {} WHERE transportationmode is 'velo_ga'".format(cnt))
		self.connection.commit()	
		self.close_db()

	def get_rides(self):
		print("get_rides")
		self.open_db()

		self.cursor.execute("SELECT count FROM rides WHERE transportationmode is 'velo_ga'")
		count = self.cursor.fetchall()
		
		self.close_db()

		return count[0][0]

	def open_db(self):
		self.connection = sqlite3.connect("vegastorage.sqlite3")
		self.cursor = self.connection.cursor()

	def close_db(self):
		self.connection.close()

	def init_rides_table(self):
		self.open_db()

		self.cursor.execute("CREATE TABLE IF NOT EXISTS rides (id INTEGER not NULL, transportationmode TEXT, count INTEGER, PRIMARY KEY (id))")

		self.cursor.execute("SELECT * FROM rides")
		rows = self.cursor.fetchall()

		is_velo_ga_existing = False
		for row in rows:
			if 'velo_ga' in row:
				is_velo_ga_existing =True

		if not is_velo_ga_existing:		
			self.cursor.execute("INSERT INTO rides VALUES (0, 'velo_ga', 0)")
			self.connection.commit()			

		self.close_db()

	def print_db(self):
		self.open_db()

		self.cursor.execute("SELECT * FROM rides")
		rows = self.cursor.fetchall()
		
		print("DB ({} Elements):".format(len(rows)))
		for row in rows:
		    print(row)

		self.close_db()