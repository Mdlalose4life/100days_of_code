from app import app, db, User, Conditions, Strategies, SpotifyContent, YoutubeContent

user1 = User(first_name='Sbusiso', last_name='Mdlalose',
             email='sbusiso@gmail.com', password='sbu123')
user2 = User(first_name='Ayo', last_name='hisysine',
             email='ayo@gmail.com', password='ayo123')
user3 = User(first_name='Karley', last_name='Moyo',
             email='Karly.com', password='karly123')

condition1 = Conditions(condition_name='Anger', users=user1)
condition2 = Conditions(condition_name='Family_issue', users=user2)
condition1 = Conditions(condition_name='Depression', users=user3)

strategy1 = Strategies(strategy_name='Self-reflection',
                       strategy_text='What role did you play in the conflit?',
                       conditions=condition1)
strategy2 = Strategies(strategy_name='comfrontation',
                       strategy_text='Have a sitdown with the family mamber, Never stand up with no resolution',
                       conditions=condition2)
strategy3 = Strategies(strategy_name='Self-reflection',
                       strategy_text='What role did you play in the conflit?',
                       conditions=condition1)

podcast1 = SpotifyContent(
    podcast_title='willingess to vurnarable', podcast_id=0, strategies=strategy1)
podcast2 = SpotifyContent(
    podcast_title='The epression', podcast_id=1, strategies=strategy2)
podcast3 = SpotifyContent(
    podcast_title='willingess to vurnarable', podcast_id=2, strategies=strategy3)

youtubeVideo1 = YoutubeContent(
    video_title='be personal', video_url='www.youtube/personal', strategies=strategy1)
youtubeVideo2 = YoutubeContent(
    video_title='try to understand others', video_url='www.youtube/other', strategies=strategy1)
youtubeVideo3 = YoutubeContent(
    video_title='be personal', video_url='www.youtube/personal', strategies=strategy1)

db.session.add_all([user1, user2, user3])
db.session.add_all([condition1, condition2, user3])
db.session.add_all([strategy1, strategy2, strategy3])
db.session.add_all([podcast1, podcast2, podcast3])
db.session.add_all([youtubeVideo1, youtubeVideo2, youtubeVideo3])
db.session.commit()
