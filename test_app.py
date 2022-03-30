import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from database.models import set_up, Movies, Actors







class CapstoneTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_app"
        self.database_user='postgres'
        self.database_pasword='15963570'
        self.database_path = "postgresql://{}:{}@{}/{}".format(self.database_user,self.database_pasword,'localhost:5432', self.database_name)
        set_up(self.app, self.database_path)


    
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

      

      
        with open('auth0_jwt.json', 'r') as auth:
            self.auth = json.loads(auth.read())

        assistant_jwt = self.auth["roles"]["Casting Assistant"]["jwt_token"]
        director_jwt = self.auth["roles"]["Casting Director"]["jwt_token"]
        producer_jwt = self.auth["roles"]["Executive Producer"]["jwt_token"]
        self.auth_headers = {
            "Casting Assistant": f'Bearer {assistant_jwt}',
            "Casting Director": f'Bearer {director_jwt}',
            "Executive Producer": f'Bearer {producer_jwt}'
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

	    


    def test_get_movie_by_producer(self):
        header_item = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().get('/movie', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["movies"]), type([]))

    def test_get_actor_by_producer(self):
        header_item = {
            "Authorization": self.auth_headers["Executive Producer"]
        }
        res = self.client().get('/actor', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["actors"]), type([]))


    def test_a_post_actor_by_producer_1(self):
    	header_item={
    	"Authorization":self.auth_headers["Executive Producer"]
    	}
    	body={
    	'name':'Javlon',
    	'age':18,
    	'gender':'male'
    	}
    	res=self.client().post('/actor',headers=header_item,json=body) 
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,200) 
    
    	self.assertTrue(data['success']) 

    def test_a_post_actor_by_producer_2(self):
    	header_item={
    	"Authorization":self.auth_headers["Executive Producer"]
    	}
    	body={
    	'name':'Dilnoza Kubayeva',
    	'age':40,
    	'gender':'female'
    	}
    	res=self.client().post('/actor',headers=header_item,json=body) 
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,200) 
    	 
    	self.assertTrue(data['success']) 
    def test_a_post_movie_by_producer_1(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']
    	}	
    	body={
    	"title":"future",
    	"release_date":"2022-03-18-00-31"
    	}
    	res=self.client().post('/movie',headers=header_item,json=body)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,200)  
    	self.assertTrue(data['success'])
    	
    

    def test_a_post_movie_by_producer_2(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']
    	}	
    	body={
    	"title":"my_universty",
    	"release_date":"2022-06-18-08-05"
    	}
    	res=self.client().post('/movie',headers=header_item,json=body)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,200) 
    	
    	self.assertTrue(data['success']) 


    def test_patch_actor_by_producer(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']}	
    	body={
    	'name':'Jasur'
    	}
    	res=self.client().patch('/actor/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success'])
    def test_patch_movie_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']

    	}	
    	body={
    	'title':'good_name'
    	}
    	res=self.client().patch('/movie/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success']) 




    def test_delete_movie_by_producer(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']

    	}	
    	
    	res=self.client().delete('/movie/2',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success']) 

    def test_delete_actor_by_producer(self):
    	header_item={
    	"Authorization":self.auth_headers['Executive Producer']

    	}	
    	
    	res=self.client().delete('/actor/2',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success'])  	




    def test_get_movie_by_director(self):
        header_item = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().get('/movie', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["movies"]), type([]))

    def test_get_actor_by_director(self):
        header_item = {
            "Authorization": self.auth_headers["Casting Director"]
        }
        res = self.client().get('/actor', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["actors"]), type([]))

    def test_b_post_actor_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers["Casting Director"]
    	}
    	body={
    	'name':'Javlon',
    	'age':18,
    	'gender':'male'
    	}
    	res=self.client().post('/actor',headers=header_item,json=body) 
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,200)  
    	self.assertTrue(data['success']) 

    def test_b_post_movie_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Director']
    	}	
    	body={
    	"title":"future",
    	"release_date":"2021-03-18-00-31"
    	}
    	res=self.client().post('/movie',headers=header_item,json=body)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,403)  
    	self.assertFalse(data['success']) 


    def test_patch_actor_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Director']}	
    	body={
    	'name':'Jasur'
    	}
    	res=self.client().patch('/actor/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success'])
    def test_patch_movie_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Director']

    	}	
    	body={
    	'title':'no_name'
    	}
    	res=self.client().patch('/movie/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success']) 




    def test_delete_movie_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Director']

    	}	
    	
    	res=self.client().delete('/movie/1',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,403)
    	self.assertFalse(data['success']) 

    def test_delete_actor_by_director(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Director']

    	}	
    	
    	res=self.client().delete('/actor/3',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,200)
    	self.assertTrue(data['success'])     	




    def test_get_movie_by_assistant(self):
        header_item = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/movie', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["movies"]), type([]))

    def test_get_actor_by_assistant(self):
        header_item = {
            "Authorization": self.auth_headers["Casting Assistant"]
        }
        res = self.client().get('/actor', headers=header_item)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])
        self.assertEqual(type(data["actors"]), type([]))

    def test_post_actor_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers["Casting Assistant"]
    	}
    	body={
    	'name':'Javlon',
    	'age':18,
    	'gender':'male'
    	}
    	res=self.client().post('/actor',headers=header_item,json=body) 
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,403)  
    	self.assertFalse(data['success']) 
    def test_post_movie_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Assistant']
    	}	
    	body={
    	"title":"future",
    	"release_date":"2021-03-18-00-31"
    	}
    	res=self.client().post('/movie',headers=header_item,json=body)
    	data=json.loads(res.data)

    	self.assertEqual(res.status_code,403)  
    	self.assertFalse(data['success']) 

    def test_patch_actor_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Assistant']}	
    	body={
    	'name':'Jasur'
    	}
    	res=self.client().patch('/actor/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,403)
    	self.assertFalse(data['success'])
    def test_patch_movie_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Assistant']

    	}	
    	body={
    	'name':'Jasur'
    	}
    	res=self.client().patch('/movie/1',headers=header_item,json=body)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,403)
    	self.assertFalse(data['success'])



    def test_delete_movie_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Assistant']

    	}	
    	
    	res=self.client().delete('/movie/1',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,403)
    	self.assertFalse(data['success']) 

    def test_delete_actor_by_assistant(self):
    	header_item={
    	"Authorization":self.auth_headers['Casting Assistant']

    	}
    		
    	
    	res=self.client().delete('/actor/1',headers=header_item)
    	data=json.loads(res.data)
    	self.assertEqual(res.status_code,403)
    	self.assertFalse(data['success'])   	  	


 

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()

