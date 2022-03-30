import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from database.models import set_up,Movies,Actors 

from auth.auth import AuthError, requires_auth

def create_app(test_config=None):
  # create and configure the app
 
  app = Flask(__name__)
  CORS(app,resources={"/":{"origins":"*"}})
 
  set_up(app)

  @app.after_request
  def after_request(response):
  	response.headers.add(
  		'Acces-Control-Allow-Headers',"Content-Type,Authorization,true")
  	response.headers.add(
  		"Acces-Control-Allow-Methods","GET,POST,PATCH,DELETE,OPTIONS")
  	return response



  @app.route('/actor',methods=['GET'])
  @requires_auth("get:actor")
  def view_actors(payload):

  	db_actors=Actors.query.all()
  	actors=[actor.format() for actor in db_actors]



  	return jsonify({
  		'success':True,
  		'actors':actors
  		})

  	
  @app.route('/movie',methods=['GET'])
  @requires_auth("get:movie")
  def view_movies(payload):
  	db_movies=Movies.query.all()
  	movies=[movie.format() for movie in db_movies]


  	return jsonify({
  		'success':True,
  		'movies':movies
  		})
  @app.route('/actor',methods=['POST'])
  @requires_auth("post:actor")
  def create_actors(payload):
  	new_actors=request.get_json()
    

   
  	try:
  		actor=Actors(
  			name=new_actors.get('name'),
  			age=new_actors.get('age'),
  			gender=new_actors.get('gender')
  		)	
  		actor.insert()
  	except:
  		abort(400)	
  	return jsonify({
  		'success':True,
  		'actor':actor.format()
  	})	
  @app.route('/movie',methods=['POST'])
  @requires_auth("post:movie")
  def create_movies(payload):
  	new_movies=request.get_json()
  	try:
  		movie=Movies(
  			title=new_movies.get('title'),
  			release_date=new_movies.get('release_date')

  			)
  		movie.insert()
  	except:
  		abort(400)	
  	return jsonify({
  		'success':True,
  		'movie':movie.format()
  	})	

  @app.route('/actor/<int:id>',methods=['DELETE'])
  @requires_auth('delete:actor')  
  def delete_item(payloaad,id):
    actor=Actors.query.get(id)
    if actor is None:
      abort(404)
    actor.delete()  
    return jsonify({
      'success':True,
      'id':id
      })
  @app.route('/movie/<int:id>',methods=['DELETE']) 
  @requires_auth('delete:movie') 
  def delete_movie(payload,id):
    movie=Movies.query.get(id)
    if movie is None:
      abort(404)
    movie.delete()  
    return jsonify({
      'success':True,
      'id':id
      }) 

  @app.route('/movie/<int:id>',methods=['PATCH']) 
  @requires_auth('patch:movie') 
  def update_movie(payload,id):
    upg_movie_items=request.get_json()
    try:
      title=upg_movie_items.get('title',None)
      release_date=upg_movie_items.get('release_date',None)
    except:
      abort(400)  
    movie=Movies.query.get(id)
    if movie is None:
      abort(404)
    if title:  
      movie.title=title
    if release_date:  
      movie.release_date=release_date
    movie.update() 
    return jsonify({
      'success':True,
      'title':movie.title,
      'release_date':movie.release_date
      }) 




  @app.route('/actor/<int:id>',methods=['PATCH']) 
  @requires_auth('patch:actor') 
  def update_actor(payload,id):
    upg_actor_items=request.get_json()
    
    try:

      name=upg_actor_items.get('name',None)
      age=upg_actor_items.get('age',None)
      gender=upg_actor_items.get('gender',None)

    except:
      abort(400)  
    actor=Actors.query.get(id)
    if actor is None:
      abort(404)
    if name:  
      actor.name=name
    if age:  
      actor.age=age
    if gender:  
      actor.gender=gender
    actor.update()   
    return jsonify({


      'success':True,

      'name':actor.name,
      'age':actor.age,
      'gender':actor.gender

      })  


  @app.errorhandler(422)
  def unprocessable(error):
      return jsonify({
          "success": False,
          "error": 422,
          "message": "unprocessable"
      }), 422


  @app.errorhandler(404)
  def not_found(error):
      return jsonify({
          "success": False,
          "error": 404,
          "message": "resource not found"
      }), 404


  @app.errorhandler(AuthError)
  def auth_error(error):
      print(error)
      return jsonify({
          "success": False,
          "error": error.status_code,
          "message": error.error['description']
      }), error.status_code


  @app.errorhandler(401)
  def unauthorized(error):
      print(error)
      return jsonify({
          "success": False,
          "error": 401,
          "message": 'Unathorized'
      }), 401


  @app.errorhandler(500)
  def internal_server_error(error):
      print(error)
      return jsonify({
          "success": False,
          "error": 500,
          "message": 'Internal Server Error'
      }), 500


  @app.errorhandler(400)
  def bad_request(error):
      print(error)
      return jsonify({
          "success": False,
          "error": 400,
          "message": 'Bad Request'
      }), 400


  @app.errorhandler(405)
  def method_not_allowed(error):
      print(error)
      return jsonify({
          "success": False,
          "error": 405,
          "message": 'Method Not Allowed'
      }), 405













  return app

APP = create_app()

if __name__ == '__main__':
    APP.run(host='0.0.0.0', port=8080, debug=True)


#https://web-developer.us.auth0.com/authorize?audience=capstone&response_type=token&client_id=h94V9LpySMAqb81TbOcmFNzWCB4njgkj&redirect_uri=https://127.0.0.1:8080/ 