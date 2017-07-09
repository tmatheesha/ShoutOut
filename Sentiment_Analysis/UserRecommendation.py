from pymongo import MongoClient
import random

def prefered_users(domain):
    if domain == 'politic':
        connection=MongoClient('localhost',27017)
        db=connection.Recommandation #db name
        collection1=db.PoliticsPosts # collection name
        Post_ID=[]
        for object in collection1.find():
            id=object['OwnerUserId']
            Post_ID.append(id)

        word_counter = {}
        for word in Post_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_posts = sorted(word_counter, key = word_counter.get, reverse = True)
        top_posts = popular_posts[:100]

        collection2=db.PoliticsComments # collection name
        Comment_ID=[]
        for object in collection2.find():
            id=object['UserId']
            Comment_ID.append(id)

        word_counter = {}
        for word in Comment_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_comments = sorted(word_counter, key = word_counter.get, reverse = True)
        top_comments = popular_comments[:100]

        collection3=db.PoliticsUsers
        Reputation_ID=[]
        for object in collection3.find({"Reputation": {"$lt": "100"}}):
            id=object['Id']
            Reputation_ID.append(id)

        Post_Comment_ID=list(set(Post_ID).intersection(Comment_ID))
        Post_Comment_Reputation_ID = Post_Comment_ID + Reputation_ID
        Unique_elements=[]
        for i in Post_Comment_Reputation_ID:
            if i not in Unique_elements:
                Unique_elements.append(i)
        Random_ID=random.sample(Unique_elements,20)
        a=[]
        for id in Random_ID:
            ab=''
            for ob in collection3.find({"Id": id}, {"DisplayName": 1}):
                ab=ob
            a.append(ab)
        j=0
        b =[]
        while j<a.__len__():
            # print (a[j]['DisplayName'])
            b.append(a[j]['DisplayName'])
            j=j+1
        temp = ''
        for s in b:
            if temp == '':
                temp = s
            else:
                temp = temp + "\n" + s
        return temp

    elif domain == 'sport':
        connection=MongoClient('localhost',27017)
        db=connection.Recommandation #db name
        collection1=db.SportsPosts # collection name
        Post_ID=[]
        for object in collection1.find():
            id=object['OwnerUserId']
            Post_ID.append(id)

        word_counter = {}
        for word in Post_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_posts = sorted(word_counter, key = word_counter.get, reverse = True)
        top_posts = popular_posts[:100]

        collection2=db.SportsComments # collection name
        Comment_ID=[]
        for object in collection2.find():
            id=object['UserId']
            Comment_ID.append(id)

        word_counter = {}
        for word in Comment_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_comments = sorted(word_counter, key = word_counter.get, reverse = True)
        top_comments = popular_comments[:100]

        collection3=db.SportsUsers
        Reputation_ID=[]
        for object in collection3.find({"Reputation": {"$lt": "100"}}):
            id=object['Id']
            Reputation_ID.append(id)

        Post_Comment_ID=list(set(Post_ID).intersection(Comment_ID))
        Post_Comment_Reputation_ID = Post_Comment_ID + Reputation_ID
        Unique_elements=[]
        for i in Post_Comment_Reputation_ID:
            if i not in Unique_elements:
                Unique_elements.append(i)
        Random_ID=random.sample(Unique_elements,20)
        a=[]
        for id in Random_ID:
            ab=''
            for ob in collection3.find({"Id": id}, {"DisplayName": 1}):
                ab=ob
            a.append(ab)
        j=0
        b =[]
        while j<a.__len__():
            # print (a[j]['DisplayName'])
            b.append(a[j]['DisplayName'])
            j=j+1
        temp = ''
        for s in b:
            if temp == '':
                temp = s
            else:
                temp = temp + "\n" + s
        return temp






    elif domain == 'Other':
        temp = 'No recommendation'
        return temp

    elif domain == 'movie':
            connection = MongoClient('localhost', 27017)
            db = connection.Recommandation  # db name
            collection1 = db.MoviesPosts  # collection name
            Post_ID = []
            for object in collection1.find():
                id = object['OwnerUserId']
                Post_ID.append(id)

            word_counter = {}
            for word in Post_ID:
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1
            popular_posts = sorted(word_counter, key=word_counter.get, reverse=True)
            top_posts = popular_posts[:100]

            collection2 = db.MoviesComments  # collection name
            Comment_ID = []
            for object in collection2.find():
                id = object['UserId']
                Comment_ID.append(id)
            word_counter = {}
            for word in Comment_ID:
                if word in word_counter:
                    word_counter[word] += 1
                else:
                    word_counter[word] = 1
            popular_comments = sorted(word_counter, key=word_counter.get, reverse=True)
            top_comments = popular_comments[:100]

            collection3 = db.MoviesUsers
            Reputation_ID = []
            for object in collection3.find({"Reputation": {"$lt": "100"}}):
                id = object['Id']
                Reputation_ID.append(id)

            Post_Comment_ID = list(set(Post_ID).intersection(Comment_ID))
            Post_Comment_Reputation_ID = Post_Comment_ID + Reputation_ID
            Unique_elements = []
            for i in Post_Comment_Reputation_ID:
                if i not in Unique_elements:
                    Unique_elements.append(i)
            Random_ID = random.sample(Unique_elements, 20)
            a = []
            for id in Random_ID:
                ab = ''
                for ob in collection3.find({"Id": id}, {"DisplayName": 1}):
                    ab = ob
                a.append(ab)
            j = 0
            b =[]
            while j < a.__len__():
                # print (a[j]['DisplayName'])
                b.append(a[j]['DisplayName'])
                j = j + 1
            temp = ''
            for s in b:
                if temp == '':
                    temp = s
                else:
                    temp = temp + "\n" + s
            return temp

    elif domain == 'music':
        connection = MongoClient('localhost', 27017)
        db = connection.Recommandation  # db name
        collection1 = db.MusicPosts  # collection name
        Post_ID = []
        for object in collection1.find():
            id = object['OwnerUserId']
            Post_ID.append(id)

        word_counter = {}
        for word in Post_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_posts = sorted(word_counter, key=word_counter.get, reverse=True)
        top_posts = popular_posts[:100]

        collection2 = db.MusicComments  # collection name
        Comment_ID = []
        for object in collection2.find():
            id = object['UserId']
            Comment_ID.append(id)
        word_counter = {}
        for word in Comment_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_comments = sorted(word_counter, key=word_counter.get, reverse=True)
        top_comments = popular_comments[:100]

        collection3 = db.MusicUsers
        Reputation_ID = []
        for object in collection3.find({"Reputation": {"$lt": "100"}}):
            id = object['Id']
            Reputation_ID.append(id)

        Post_Comment_ID = list(set(Post_ID).intersection(Comment_ID))
        Post_Comment_Reputation_ID = Post_Comment_ID + Reputation_ID
        Unique_elements = []
        for i in Post_Comment_Reputation_ID:
            if i not in Unique_elements:
                Unique_elements.append(i)
        Random_ID = random.sample(Unique_elements, 20)
        a = []
        for id in Random_ID:
            ab = ''
            for ob in collection3.find({"Id": id}, {"DisplayName": 1}):
                ab = ob
            a.append(ab)
        j = 0
        b = []
        while j < a.__len__():
            # print (a[j]['DisplayName'])
            b.append(a[j]['DisplayName'])
            j = j + 1
        temp = ''
        for s in b:
            if temp == '':
                temp = s
            else:
                temp = temp + "\n" + s
        return temp

    elif domain == 'IT':
        connection = MongoClient('localhost', 27017)
        db = connection.Recommandation  # db name
        collection1 = db.ITPosts  # collection name
        Post_ID = []
        for object in collection1.find():
            id = object['OwnerUserId']
            Post_ID.append(id)

        word_counter = {}
        for word in Post_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_posts = sorted(word_counter, key=word_counter.get, reverse=True)
        top_posts = popular_posts[:100]
        # print top_posts

        collection2 = db.ITComments  # collection name
        Comment_ID = []
        for object in collection2.find():
            id = object['UserId']
            Comment_ID.append(id)
        word_counter = {}
        for word in Comment_ID:
            if word in word_counter:
                word_counter[word] += 1
            else:
                word_counter[word] = 1
        popular_comments = sorted(word_counter, key=word_counter.get, reverse=True)
        top_comments = popular_comments[:100]

        collection3 = db.ITUsers
        Reputation_ID = []
        for object in collection3.find({"Reputation": {"$lt": "100"}}):
            id = object['Id']
            Reputation_ID.append(id)

        Post_Comment_ID = list(set(Post_ID).intersection(Comment_ID))
        Post_Comment_Reputation_ID = Post_Comment_ID + Reputation_ID
        Unique_elements = []
        for i in Post_Comment_Reputation_ID:
            if i not in Unique_elements:
                Unique_elements.append(i)
        Random_ID = random.sample(Unique_elements, 20)
        a = []
        for id in Random_ID:
            ab = ''
            for ob in collection3.find({"Id": id}, {"DisplayName": 1}):
                ab = ob
                a.append(ab)
        j = 0
        b = []
        while j < a.__len__():
            # print (a[j]['DisplayName'])
            b.append(a[j]['DisplayName'])
            j = j + 1
        temp = ''
        for s in b:
            if temp == '':
                temp = s
            else:
                temp = temp + "\n" + s

        return temp





