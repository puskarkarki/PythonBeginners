
first_name = ["krishna", "Amit" "Rupesh", "Bishnu", "Sandesh", "kamal", "Hari", "Sita", "Geeta", "Aman", "Purna","Binita", "Sabina","Rabina", "Anil", 'Krishna','Rupesh','Anish','Puskar','Arjun','usha','binayak','pradip','nirajan','rakesh', 'Ram','Shyam','Hari','Pradip','Lila','Keshav','Ashmita','Binita','Asha','Manita', 'Bibek','Dev','Manish','Ram','Shyam','Isha','Binaya','Pradip','Birajan','Rohit','Anish']

last_name = ["Aryal","Maharjan", "Shrestha", "Joshi", "GC", "KC", "Adikari", "Neupane", "Sharma", "Maskey","Baral","Dangol","Khadka", "Subedi", "Shakya", 'aryal','shrestha','bhattarai','karki','bhattarai','pokhrel','lamichanne','giri','basnet','kc','Rai','Pradhan','Katwal','Sherpa','Tamang','Joshi','K.C','Shrestha','Lama','Adhikary', 'Thapa','Shrestha','Bhattarai','Karki','Bhattarai','Pokhrel','Lamichanne','Giri','Basnet','KC']

address = ["Balaju","Suryabinak","Baneshwor", "Koteshwor","Jamal", "Patan", "sunakothi", "Pesicola","Kupando", "sanepa", "Gwarko", "satdobato", "Jorpati","maitidevi", "nayabazar", 'Balaju','Suryabinayak','Pepsicola','Tinkune','Pepsicola','Itahari','Pepsicola','Pepsicola','Pepsicola','Pepsicola', 'Okhaldhunga','Suryabinayak','Swyambhu','Tinkune','Kapan','Pokhara','Solukhumbu','Baneshwor','Ramechaap','Sitapaila', 'Balaju','Suryabinayak','Pepsicola','Tinkune','Jorpati','Itahari','Gaurighat','Baneshwor','Balaju','Okhaldhungha']

count = 1

for i in range(len(first_name)):

    for j in range(len(last_name)):

        for k in range(len(address)):

            print("person"+str(count)+"{​​​​'first_name':'"+first_name[i]+"', 'last_name': '"+ last_name[j]+"', 'address':'"+address[k]+"'}​​​​")

            count+=1

