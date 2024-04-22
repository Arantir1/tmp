class UserMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self, request):

        # before view
        print(dir(request))

        response = self.get_response(request)

        # after view

        return response
