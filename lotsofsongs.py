from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db_setup import Base, Band, Album, Song

engine = create_engine('sqlite:///catalogs.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession();

# New Found Glory
new_found_glory = Band(name="New Found Glory")

session.add(new_found_glory)
session.commit()

resurrection = Album(name="Resurrection", band=new_found_glory)
session.add(resurrection)
session.commit()

song1 = Song(name="Selfless", band=new_found_glory,
				length="3:28", album=resurrection)

song2 = Song(name="The Worse Person", band=new_found_glory,
				length="3:31", album=resurrection)

song3 = Song(name="Ready And Willing II", band=new_found_glory,
				length="3:24", album=resurrection)

song4 = Song(name="Viscious Love", band=new_found_glory,
				length="3:17", album=resurrection)

song5 = Song(name="Persistent", band=new_found_glory,
				length="3:06", album=resurrection)

session.add(song1)
session.add(song2)
session.add(song3)
session.add(song4)
session.add(song5)
session.commit()

catalyst = Album(name="Catalyst", band=new_found_glory)
session.add(catalyst)
session.commit()

song1 = Song(name="All Downhill From Here", band=new_found_glory,
				length="3:12", album=catalyst)

song2 = Song(name="At Least I'm Known for Something", band=new_found_glory,
				length="3:30", album=catalyst)

song3 = Song(name="Failure's Not Flattering", band=new_found_glory,
				length="3:51", album=catalyst)

song4 = Song(name="Doubt Full", band=new_found_glory,
				length="3:36", album=catalyst)

song5 = Song(name="I'd Kill to Fall Asleep", band=new_found_glory,
				length="3:36", album=catalyst)

session.add(song1)
session.add(song2)
session.add(song3)
session.add(song4)
session.add(song5)
session.commit()

# New Found Glory
blink_182 = Band(name="Blink 182")

session.add(blink_182)
session.commit()

california = Album(name="California", band=blink_182)
session.add(california)
session.commit()

song1 = Song(name="Cynical", band=blink_182,
				length="1:56", album=california)

song2 = Song(name="Bored To Death", band=blink_182,
				length="3:56", album=california)

song3 = Song(name="Built This Pool", band=blink_182,
				length="0:17", album=california)

song4 = Song(name="Kings of The Weekend", band=blink_182,
				length="2:56", album=california)

song5 = Song(name="Sober", band=blink_182,
				length="3:00", album=california)

session.add(song1)
session.add(song2)
session.add(song3)
session.add(song4)
session.add(song5)
session.commit()

print "added Bands, Albums, and Songs!"