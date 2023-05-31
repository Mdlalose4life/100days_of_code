from app import db, Post, Comment, app

post1 = Post(title='The late work', content='The art of going to bed late')
post2 = Post(title='The bird song',
             content='Playing for the king, in black suit')
post3 = Post(title='The zebra kick', content='Twice the speed of the sound')
post4 = Post(title='The Bullet train', content='It whisles like the devel')

comment1 = Comment(content='I am so in love with your writing sir', post=post1)
comment2 = Comment(content='Be more descriptive', post=post2)
comment3 = Comment(content='Pretty cool huh ?????', post=post3)
comment4 = Comment(content='I says nothing', post=post4)

db.session.add_all([post1, post2, post3, post4])
db.session.add_all([comment1, comment2, comment3, comment4])
db.session.commit()
