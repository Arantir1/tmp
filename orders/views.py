from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from rest_framework import generics, authentication, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .forms import LoginUser, MakeOrder, BookForm
from .models import Book
from .serializers import BookSerializer, LoginSerializer

from django.views.decorators.cache import cache_page

from django_celery_beat.models import PeriodicTask, IntervalSchedule


class BookPostListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = "pk"


class BookAPI(APIView):
    # authentication_classes = [authentication.TokenAuthentication]

    def get(self, request, add):
        books = Book.objects.all()
        total_cost = sum(map(lambda b: b.price, books)) + add
        return Response({"total_cost": total_cost})


class LoginView(APIView):
    # This view should be accessible also for unauthenticated users.
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        print(request.data)
        serializer = LoginSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return Response(None, status=status.HTTP_202_ACCEPTED)


def index(request):
    return HttpResponse("<h1>Home Page</h1>")


def login_page(request):
    log = LoginUser()
    if request.method == "POST":
        log = LoginUser(request, data=request.POST)
        if log.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect("/catalog/")
    return render(request, "login.html", {"login": log})


def logout_page(request):
    logout(request)
    return redirect("/login/")


@cache_page(60 * 15)
def catalog(request):
    if request.method == "POST":
        return redirect("/order/")
    books = Book.objects.filter(available__gt=0)
    return render(request, "catalog.html", {"books": books})


def order(request):
    ord = MakeOrder()
    print("order")
    if request.method == "POST":
        print("order post")
        ord = MakeOrder(request.POST)
        if ord.is_valid():
            ord.save()
    return render(request, "order.html", {"ord": ord})


def code(request):
    book = Book.objects.get(title="code")
    post = BookForm(instance=book)
    return render(request, "post.html", {"post": post})


from .task import my_task


def test_cel(request):
    my_task.delay()
    return HttpResponse("Started!")


def schedule_task(request):
    interval, err = IntervalSchedule.objects.get_or_create(
        every=30, period=IntervalSchedule.SECONDS
    )

    PeriodicTask.objects.create(
        interval=interval,
        name="evgen-schedule",
        task="orders.task.my_task",
        # args=json.dump(["arg1", True]),
        # on_off=True,
    )
    return HttpResponse("Scheduled!")


# celery -A project beat -l INFO --scheduler django-celery-beat.schedulers:DatabaseScheduler
