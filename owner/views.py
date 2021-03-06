from django.shortcuts import render,redirect
from django.http import HttpResponse
from owner import  forms
from owner.models import  Book
from django.contrib.auth import authenticate,login,logout
from owner.decorators import signin_required
from django.views.generic import View,ListView,TemplateView,CreateView,DetailView,UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator


#ListView rednder list all objects
#TemplateView
#DetailView
#UpdateView
#DeleteView

# Create your views here.

# books = [
#     {"id": 1, "book_name": "randamoozham", "author": "mt", "price": 450, "copies": 50,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 2, "book_name": "halfgf", "author": "chethan", "price": 500, "copies": 45,
#      "image": "https://encrypted-tbn1.gstatic.com/images?q=tbn:ANd9GcTHSXYG7XIi8PEuu8zqes8MWFgmKtRiv0gjmJJN402siII5uXE6"},
#     {"id": 3, "book_name": "alchmist", "author": "paulo", "price": 550, "copies": 50,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 4, "book_name": "indhuleka", "author": "chandhu", "price": 650, "copies": 20,
#      "image": "https://upload.wikimedia.org/wikipedia/en/a/af/Randamoozham_30th_edition_cover.jpg"},
#     {"id": 5, "book_name": "harry", "author": "jkr", "price": 650, "copies": 20,
#      "image": "https://i.guim.co.uk/img/media/1d4b16d4c6703e9bec9174f1cadc278026de0647/0_75_1280_768/master/1280.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=d036928c5974e9e8bfd87be5dcf37dd7"
# },
#
#
# ]

# @signin_required
# def owner_home(request):
#
#     return render(request, "owner_home.html")
@method_decorator(signin_required,name="dispatch")
class OwnerHome(TemplateView):
    template_name="owner_home.html"


#
# @signin_required
# def add_book(request,*args,**kwargs):
#     form=forms.BookForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.BookForm(request.POST,files=request.FILES)
#         if form.is_valid():
#             form.save()
#
#             # book=Book(book_name=form.cleaned_data["book_name"],
#             #           author=form.cleaned_data["author"],
#             #           price=form.cleaned_data["price"],
#             #           copies=form.cleaned_data["copies"]
#             #           )
#             # book.save()
#             return  redirect("listallbooks")
#         else:
#             return render(request,"add_book.html",{"form":form})
#
#
#     return render(request, "add_book.html",context)
@method_decorator(signin_required,name="dispatch")

class AddBook(CreateView):
    model=Book
    template_name="add_book.html"
    form_class=forms.BookForm
    success_url = reverse_lazy("listallbooks")
    # context={}
    # def get(self,request,*args,**kwargs):
    #     form=self.form_class()
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    #
    # def post(self,request,*args,**kwargs):
    #     form=self.form_class(request.POST,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listallbooks")
    #     else:
    #         self.context["form"]=form
    #         return render(request,self.template_name,self.context)


#
# def list_books(request,*args,**kwargs):
#     books=Book.objects.all()
#     context = {"products": books}
#
#     return render(request, "book_list.html", context)
@method_decorator(signin_required,name="dispatch")
class AllBooks(ListView):
    model=Book
    template_name="book_list.html"
    context_object_name = "products"


    # def get(self,request,*args,**kwargs):
    #     books=self.model.objects.all()
    #     self.context["products"]=books
    #     return render(request,self.template_name,self.context)

# def book_details(request,*args,**kwargs):
#     print(args)
#     id=kwargs["id"]
#     products =Book.objects.get(id=id)
#
#     context = {"book": products}
#     return render(request, "book_detail.html", context)
@method_decorator(signin_required,name="dispatch")
class BookDetail(DetailView):
    model=Book

    template_name="book_detail.html"
    context_object_name = "book"
    pk_url_kwarg = "id"
    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     book=self.model.objects.get(id=id)
    #     self.context["book"]=book
    #     return render(request,self.template_name,self.context)

#
# def change_book(request,*args,**kwargs):
#     id=kwargs[id]
#     item=Book.objects.get(id=id)
#     # book={
#     #     "book_name":item.book_name,
#     #     "author":item.author,
#     #     "price":item.price,
#     #     "copies":item.copies
#     # }
#
#
#     form=forms.BookForm(instance=item)
#     conetxt={"form":form}
#     if request.method=="POST":
#         form=forms.BookForm(request.POST,instance=item,files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect("listallbooks")
#         else:
#             return redirect(request,"edit_book.html",{"form":form})
#     return render(request,"edit_book.html",conetxt)

# books(book_name,author,copies,price)
@method_decorator(signin_required,name="dispatch")
class BookUpdate(UpdateView):
    template_name="edit_book.html"
    model=Book
    pk_url_kwarg = "id"
    success_url = reverse_lazy("listallbooks")

    form_class=forms.BookForm

    # def get(self,request,*args,**kwargs):
    #     id=kwargs["id"]
    #     book=self.model.objects.get(id=id)
    #     form=self.form_class(instance=book)
    #     self.context["form"]=form
    #     return render(request,self.template_name,self.context)
    # def post(self,request,*args,**kwargs):
    #     id = kwargs["id"]
    #     book = self.model.objects.get(id=id)
    #     form=self.form_class(request.POST,instance=book,files=request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect("listallbooks")
    #     else:
    #         self.context["form"]=form
    #         return render(request, self.template_name, self.context)
    #


class Registration(CreateView):
    model=User
    template_name = "register.html"
    form_class = forms.UserRegistrationForm
    success_url = reverse_lazy("signin")


#
# def user_registration(request):
#     form=forms.UserRegistrationForm()
#     context={"form":form}
#     if request.method=="POST":
#         form=forms.UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print("user hasbeen crerated")
#             return render(request,"login.html")
#         else:
#             context={"form":form}
#             return render(request, "register.html", context)
#
#     return render(request,"register.html",context)


class SignIn(TemplateView):
    template_name = "login.html"
    context = {}

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        form=forms.SigninForm()
        context["form"]=form

        return context
    def post(self,request,*args,**kwargs):
        form=forms.SigninForm(request.POST)
        if form.is_valid():
            u_name=form.cleaned_data["username"]
            pwd=form.cleaned_data["password"]
            user=authenticate(request,username=u_name,password=pwd)
            if user:
                login(request,user)
                if user.is_superuser:
                    return redirect("ownerindex")
                else:
                    return redirect("customerhome")


            else:
                print("invalid")
                self.context["form"]=form
                return render(request,self.template_name,self.context)


#
# def signin(request):
#     form=forms.SigninForm()
#     context={"form":form}
#     if request.method=="POST":
#
#         form=forms.SigninForm(request.POST)
#         if form.is_valid():
#             u_name=form.cleaned_data["username"]
#             pwd=form.cleaned_data["password"]
#             user=authenticate(request,username=u_name,password=pwd)
#             if user:
#                 login(request,user)
#                 return redirect("ownerindex")
#             else:
#                 return render(request, "login.html", context)
#
#     return render(request,"login.html",context)

@signin_required
def signout(requset,*args,**kwargs):
    logout(requset)
    return redirect("signin")



