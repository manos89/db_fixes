import requests,json,pymongo



USERNAME='stats-user'
PASSWORD='congo-congo'
PORT='27017'
HOST='172.104.130.120'
MONGO_DATABASE = 'basketstats'
MONGO_URI='mongodb://'+USERNAME+':'+PASSWORD+'@'+HOST+':'+PORT+'/'+MONGO_DATABASE\

client = pymongo.MongoClient(MONGO_URI)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
db = client['basketstats']

results=db['players'].aggregate([
    { 
        "$group": { 
        	"_id": { "pid": "$pid"}, 
            "uniqueIds": { "$addToSet": "_id" },
            "count": { "$sum": 1 } 
        }
    }, 
    { "$match": { "count": { "$gt": 1 } } }
])
count=0
for r in results:
	noplayer=0
	oldpid=(r["_id"]["pid"])
	player_results=db['players'].find({'pid':oldpid})
	count+=1
	for r in player_results:
		name=r['pid']
		mongo_id=r['_id']
		if noplayer==0:
			pass
		else:
			db['players'].update_one({'_id':mongo_id},{'$set':{'pid':name+'_'+str(noplayer)}})
		noplayer+=1

	print(count)
