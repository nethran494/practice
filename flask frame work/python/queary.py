import sqlite3
con = sqlite3.connect("data.db")
cr = con.cursor()
fname = 'Nethra'
lname = 'vathi'
email = 'nethran494@gmail.com'
username = 'nethravijay'
password = 'nethra@123'

# cr.execute("create table if not exists User(id integer primary key, fname TEXT,lname TEXT, email TEXT,username TEXT,password TEXT)")
# cr.execute("insert into user(fname,lname, email,username,password) values('"+fname+"','"+lname+"','"+email+"','"+username+"','"+password+"')")
# con.commit()
# cr.execute("delete from user where id=2")
# con.commit()
# cr.execute("select * from user")
data=[['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123'],
      ['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123'],
      ['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123'],
      ['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123'],
      ['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123'],
      ['Nethra','vathi','nethran494@gmail.com','nethravijay','nethra@123']]


# for row in data:
#     cr.execute("insert into user(fname,lname,email,username,password) values(?,?,?,?,?)",row)
#     con.commit()
cr.execute("select * from user")


var = cr.fetchall() 
print(var)
# con.commit()