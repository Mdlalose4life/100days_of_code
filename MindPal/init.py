from app import db, User, Conditions, Strategies, SpotifyContent, YoutubeContent

user1 = User(first_name='Sbusiso', last_name='Mdlalose',
             email='sbusiso@gmail.com', password='sbu123')
user2 = User(first_name='Ayo', last_name='hisysine',
             email='ayo@gmail.com', password='ayo123')
user3 = User(first_name='Karley', last_name='Moyo',
             email='Karly@gmail.com', password='karly123')
user4 = User(first_name='Jack', last_name='Zondo',
             email='jack@gmail.com', password='jact123')
user5 = User(first_name='Maswazi', last_name='Nzima',
             email='maswa@gmail.com', password='karly123')


condition1 = Conditions(condition_name='Anger', users=user1)
condition2 = Conditions(condition_name='stress', users=user3)
condition3 = Conditions(condition_name='Family issue', users=user2)
condition4 = Conditions(condition_name='Depression', users=user4)


strategy1 = Strategies(strategy_name='Self-reflection',
                       strategy_text='What role did you play in the conflit?',
                       conditions=condition1)
strategy2 = Strategies(strategy_name='Internal Errends',
                       strategy_text='What role did you play in the conflit?',
                       conditions=condition2)
strategy3 = Strategies(strategy_name='comfrontation',
                       strategy_text='Have a sitdown with the family mamber, Never stand up with no resolution',
                       conditions=condition3)
strategy4 = Strategies(strategy_name='Isolation',
                       strategy_text='Go, take a walk alone. breakdwon your problems int',
                       conditions=condition4)

podcast1 = SpotifyContent(
    podcast_title='willingess to vurnarable', podcast_content='file/audio010', strategies=strategy1)
podcast2 = SpotifyContent(
    podcast_title='The epression', podcast_content='file/audio020', strategies=strategy2)
podcast3 = SpotifyContent(
    podcast_title='willingess to vurnarable', podcast_content='file/audio040', strategies=strategy3)
podcast4 = SpotifyContent(
    podcast_title='sit and stand', podcast_content='file/audio050', strategies=strategy4)

youtubeVideo1 = YoutubeContent(
    video_title='be personal', youtube_content='www.youtube/personal', strategies=strategy1)
youtubeVideo2 = YoutubeContent(
    video_title='try to understand others', youtube_content='www.youtube/other', strategies=strategy1)
youtubeVideo3 = YoutubeContent(
    video_title='be personal', youtube_content='www.youtube/personal', strategies=strategy1)
youtubeVideo4 = YoutubeContent(
    video_title='No more tricky smile', youtube_content='www.youtube/smile', strategies=strategy3)

db.session.add_all([user1, user2, user3, user4, user5])
db.session.add_all([condition1, condition2, condition3, condition4])
db.session.add_all([strategy1, strategy2, strategy3, strategy4])
db.session.add_all([podcast1, podcast2, podcast3, podcast4])
db.session.add_all([youtubeVideo1, youtubeVideo2,
                   youtubeVideo3, youtubeVideo4])
db.session.commit()
