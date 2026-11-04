from django.shortcuts import render


class FrontCtlMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print('Front Ctl Middleware')

        if request.path_info in ['/', '/ors/Login/', '/ors/Registration/', '/ors/welcome/', '/ors/logout/','/ors/ForgetPassword/']:
            return self.get_response(request)

        if request.session.get('first_name', None) == None:
            message = 'Session expired... plz login again..!!'
            return render(request, 'login.html', {'message': message})

        return self.get_response(request)