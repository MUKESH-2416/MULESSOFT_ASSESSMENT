import sqlite3
#connect to database
conn=sqlite3.connect('movies_details.db')
c=conn.cursor()

# movies details

print ("MOVIE-NAME"+"   "+"ACTOR"+"      "+"DIRECTOR"+"        "+"YEAR-OF RELEASE"+"          "+"ACTRESS")
print("----------"+"  "+"-----"+"      "+"--------"+"        "+"---------------"+"           "+"-------")
def details ():
	q="SELECT * FROM details"
	my_cursor=conn.execute(q)
	data_row=c.fetchall()
	for row in my_cursor:
		print(row)
	conn.commit()
	conn.close()
details()

#movies detail based on actors name
print("movies based on actor name")
print("----------------------------")
def movie_lookup (actor_name):
	conn=sqlite3.connect('movies_details.db')
	c=conn.cursor()
	c.execute("SELECT* FROM details WHERE actor=(?)",(actor_name,))
	a=c.fetchall()
	for i in a:
			print(i[0]+"'s actor is "+i[1])
		
	conn.commit()
	conn.close()
movie_lookup("Edward")
