import psycopg2

con = psycopg2.connect(
    database ="mydatabase",
    user ="postgres",
    password ="sandesh",
    host ="localhost",
    port ="5432"
)

cursor_obj = con.cursor()
cursor_obj.execute("SELECT * FROM userdata")
selectall = cursor_obj.fetchall()
print ("result set =","\n",selectall)

cursor_obj.execute("""
delete from userdata where email in ('abc2057@gmail.com','abcdef@gmail.com')
""")

cursor_obj.execute("""
    Insert into userdata (email,username,password,otp) 
    values
    ('abc2057@gmail.com', 'abc2057', 'abc1234', ''),
    ('abcdef@sxc.edu.np','abcdef','121212121','');
    """ )

cursor_obj.execute("""
update userdata
set password = 'pathak2058'
where email = 'pathak2057@gmail.com'
""")



con.commit()
con.close()

