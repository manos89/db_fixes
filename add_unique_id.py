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
# results=db['players'].create_index([('pid', pymongo.ASCENDING)],unique=True)

 
# results=db['players'].update_many({}, {'$unset':{"pid":1}})
# quit()
# print(results)
results=db['players'].find()
for r in results:
	mongo_id=r['_id']
	name=r['BasicInfo']['playerName'].replace(' ','_').lower()
	count=1
	while True:
		try:
			results=db['players'].count_documents({'pid':name})
			resultscount= results
		except Exception as E:
			print(E)
			resultscount=0
		if resultscount>0:
			name=name+'_'+str(count)
			count+=1
		else:
			db['players'].update_one({'_id':mongo_id},{'$set':{'pid':name}})
			break
	spot+=1
	if spot%10==0:
		print(spot)
