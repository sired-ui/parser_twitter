# parser_twitter

Запуск:

uvicorn main:app

# Test POST /

links = ["https://twitter.com/elonmusk", "https://twitter.com/VitalikButerin"]

r = requests.post('http://127.0.0.1:8000/', json={"links":links})

# Result:
{"sessiond_id": 2}

# Test GET /api/users/status

r = requests.get('http://127.0.0.1:8000/api/users/status', json={'session_id': 2})

# Result:
[{'username': 'elonmusk', 'status': 'success'}, {'username': 'vitalikbuterin', 'status': 'success'}]

# Test GET /api/user/{username}

r = requests.get('http://127.0.0.1:8000/api/user/elonmusk')

# Result:
{"twitter_id":44196397,"name":"Elon Musk","username":"elonmusk","following_count":165,"followers_count":124808111,"description":"@BillyM2k @KevinChunilal Nice"}

# Test GET /api/tweets/{twitter_id}

r = requests.get('http://127.0.0.1:8000/api/tweets/44196397')

# Result:
{"data":[{"edit_history_tweet_ids":["1611674157716213761"],"id":"1611674157716213761","text":"@WholeMarsBlog @ValerianIlies People still don’t get it"},{"edit_history_tweet_ids":["1611673521528410115"],"id":"1611673521528410115","text":"@_TheRealTony3_ @MercedesBenz @Tesla @SawyerMerritt Good for them"},{"edit_history_tweet_ids":["1611669863097069569"],"id":"1611669863097069569","text":"@RichardGarriott Tanks are a deathtrap now. With neither side having air superiority, you’re left with infantry &amp; artillery – essentially WW1."},{"edit_history_tweet_ids":["1611668491253481472"],"id":"1611668491253481472","text":"@BillyM2k 🤣"},{"edit_history_tweet_ids":["1611433974035017729"],"id":"1611433974035017729","text":"@TheRabbitHole84 An actual Jurassic Park would be awesome"},{"edit_history_tweet_ids":["1611431254091763714"],"id":"1611431254091763714","text":"(JCO was joking btw)"},{"edit_history_tweet_ids":["1611423667107549184"],"id":"1611423667107549184","text":"8 years later &amp; still no laws … 😢 https://t.co/9fjb24XvFG"},{"edit_history_tweet_ids":["1611421164265672704"],"id":"1611421164265672704","text":"@TheBabylonBee 🤣"},{"edit_history_tweet_ids":["1611298376737492992"],"id":"1611298376737492992","text":"@pmarca Twitter has at least 10 million Wokeys"}],"meta":{"result_count":9,"newest_id":"1611674157716213761","oldest_id":"1611298376737492992","next_token":"7140dibdnow9c7btw450qn8il9k8fv59ye50smwpw516a"}}
