import requests,json,pymongo



USERNAME='stats-user'
PASSWORD='congo-congo'
PORT='27017'
HOST='172.104.130.120'
MONGO_DATABASE = 'basketstats'
MONGO_URI='mongodb://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+MONGO_DATABASE
client = pymongo.MongoClient(MONGO_URI)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['basketstats']
spot=0 


results=db['players'].find()
for r in results:
	mongo_id=r['_id']
	name=r['BasicInfo']['playerName'].replace(' ','_').lower()
	db['players'].update_one({'_id':mongo_id},{'$set':{'pid':name}})
	spot+=1
	if spot%10==0:
		print(spot)