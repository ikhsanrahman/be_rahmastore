from user import models as us
from buyer import models as by


class Auth:

	@staticmethod
	def get_logged_in_user(request):
		# get the auth token
		# print(request.headers.get, 'headers')
		auth_token = request.headers.get('Authorization')
		if auth_token:
			resp = us.MyUser.decode_auth_token(auth_token)
			if resp['blacklisted'] == False:
				user = us.MyUser.objects.get(id=resp['msg'])
				response_object = {
						'status': 'success',
						'data': user
				}
				return response_object, 200
			else:
				response_object = {
						'status': 'fail',
						'message': resp
				}
				return response_object, 401
		else:
				response_object = {
						'status': 'fail',
						'message': 'Provide a valid auth token.'
				}
				return response_object, 401

	@staticmethod
	def get_logged_in_buyer(request):
		# get the tutor auth token
		auth_token = request.headers.get('Authorization')
		if auth_token:
			resp = by.Buyer.decode_auth_token(auth_token.split(" ", 1)[1])
			if resp['blacklisted'] == False:
				buyer = Buyer.objects.get(id=resp['msg']).first()
				response_object = {
						'status': 'success',
						'data': buyer
				}
				return response_object, 200
			else:
				response_object = {
						'status': 'fail',
						'message': resp
				}
				return response_object, 401
		else:
			response_object = {
					'status': 'fail',
					'message': 'Provide a valid auth token.'
			}
			return response_object, 401
							
	# @staticmethod
	# def get_logged_in_admin(new_request):
	# 	# get the admin auth token
	# 	auth_token = new_request.headers.get('Authorization')
	# 	if auth_token:
	# 		resp = Admin.decode_auth_token(auth_token.split(" ", 1)[1])
	# 		if not isinstance(resp, str):
	# 				admin = Admin.query.filter_by(id=resp).first()
	# 				response_object = {
	# 						'status': 'success',
	# 						'data': admin
	# 				}
	# 				return response_object, 200
	# 		response_object = {
	# 				'status': 'fail',
	# 				'message': resp
	# 		}
	# 		return response_object, 401
	# 	else:
	# 			response_object = {
	# 					'status': 'fail',
	# 					'message': 'Provide a valid auth token.'
	# 			}
	# 			return response_object, 401	

		

	# @staticmethod
	# def logout_Student(data):
	# 	if data:
	# 		auth_token = data.split(" ")[1]
	# 	else:
	# 		auth_token = ''

	# 	if auth_token:
	# 		resp = Student.decode_auth_token(auth_token)
	# 		if not isinstance(resp, str):
	# 			# mark the token as blacklisted
	# 			return TokenService().save_token(token=auth_token)
	# 		else:
	# 				response_object = {
	# 						'status': 'fail',
	# 						'message': resp
	# 				}
	# 				return response_object, 401
	# 	else:
	# 			response_object = {
	# 					'status': 'fail',
	# 					'message': 'Provide a valid auth token.'
	# 			}
	# 			return response_object, 403




# def generate_token(user):
# 		try:
# 				# generate the auth token
# 				auth_token = user.encode_auth_token(user.id)
# 				response_object = {
# 						'status': 'success',
# 						'message': 'Successfully registered.',
# 						'Authorization': auth_token.decode()
# 				}
# 				return response_object, 201
# 		except Exception as e:
# 				response_object = {
# 						'status': 'fail',
# 						'message': 'Some error occurred. Please try again.'
# 				}
# 				return response_object, 401


# @staticmethod
# def login_user(data):
# 		try:
# 				# fetch the user data
# 				user = User.query.filter_by(email=data.get('email')).first()
# 				if user and user.check_password(data.get('password')):
# 						auth_token = user.encode_auth_token(user.id)
# 						if auth_token:
# 								response_object = {
# 										'status': 'success',
# 										'message': 'Successfully logged in.',
# 										'Authorization': auth_token.decode()
# 								}
# 								return response_object, 200
# 				else:
# 						response_object = {
# 								'status': 'fail',
# 								'message': 'email or password does not match.'
# 						}
# 						return response_object, 401

# 		except Exception as e:
# 				print(e)
# 				response_object = {
# 						'status': 'fail',
# 						'message': 'Try again'
# 				}
# 				return response_object, 500
