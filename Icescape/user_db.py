from user_model import Base, User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import copy

engine = create_engine('sqlite:///user.db?check_same_thread=False')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
        
def add_user(name, surname, phone, date, email, nationality):
	new_user = User(name = name, surname = surname, phone = phone, date = date, email = email, nationality = nationality)
	session.add(new_user)
	session.commit()
                
def query_all():
	return(session.query(User).all())

def query_by_name(name):
        return(session.query(User).filter_by(name=name).first())

def query_by_nationality(nationality):
	return(session.query(User).filter_by(nationality = nationality)).all()

def query_by_date(date):
	return(session.query(User).filter_by(date = date)).all()

def delete_all():
	session.query(User).delete()
	session.commit()
        
                
def delete_by_name(name):
        session.query(User).filter_by(name=name).delete()
        session.commit()

def mix_and_match(date):
	users = query_by_date(date)
	
	if(len(users) > 5):
		pal_num = 0
		isr_num = 0

		team = []
		users_copy = copy.copy(users)

		for user in users_copy:
			if user.nationality == 'Israeli' and isr_num < 4:
				isr_num += 1
				team.append(user)
				users.remove(user)
			elif user.nationality == 'Palestinian' and pal_num < 4:
				pal_num += 1
				team.append(user)
				users.remove(user)

		print("Len of the team: " + str(len(team)))
		print("Pal : " + str(pal_num) + ", Isr: " + str(isr_num))
		if(len(team) < 6):
			if(pal_num<2 or isr_num < 2):
				print('Less then 2')
				team = []
			else:
				team.append(users[0])	
				print(users[0].name)
				for user in team:
					user.playing = True
					session.commit()
					print(user.playing)
		else:
			for user in team:
				user.playing = True
				session.commit()
				print(user.playing)

		session.commit()

if __name__ == '__main__':
	mix_and_match("00/00/00")
