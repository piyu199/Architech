from django.shortcuts import render,redirect
from .models import BlogPost
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from rest_framework.decorators import api_view
from .serializers import BlogPost_serializers
from rest_framework.response import Response
from rest_framework import status
from django.contrib import auth
from io import BytesIO
from django.core.files.base import ContentFile

# Create your views here.
@login_required(login_url='login')
def blog_home(request):
    try:
        blogs=BlogPost.objects.all()
    except ObjectDoesNotExist:
        pass 
    context={
        "blogs":blogs
    }
    return render(request,'blog_home.html',context)

@login_required(login_url='login')
def article_view(request,pk):
    try:
        post=BlogPost.objects.get(pk=pk)
    except ObjectDoesNotExist:
        pass
    context={
        "post":post
    }
    return render(request,"article_details.html",context)

@login_required(login_url='login')
def create(request):
    if request.method=='POST':
        title=request.POST['title']
        content=request.POST['content']
        blog=BlogPost(title=title,body=content)
        if len(request.FILES) !=0:
            blog.photo=request.FILES['photo']
            blog.save()
            messages.info(request,"Created Successfully.")
            return redirect('blog_home')
    return render(request,'createpost.html')

@login_required(login_url='login')
def update(request,pk):
    if request.method=='POST':
        blog=BlogPost.objects.get(pk=pk)
        blog.title=request.POST['title']
        blog.body=request.POST['content']
        if len(request.FILES) !=0:
            blog.photo=request.FILES['photo']
            blog.save()
            messages.info(request,"Created Successfully.")
            return redirect('blog_home')
    else:
        blog=BlogPost.objects.get(pk=pk)
        context={
            "blog":blog
        }
        return render(request,"update.html",context)

@login_required(login_url='login')
def delete(request,pk):
    blog=BlogPost.objects.get(pk=pk)
    blog.delete()
    messages.info(request,"Deleted Successfully")
    return redirect('blog_home')


@api_view(['GET','POST'])
def blog_list(request):

    if request.method=="GET":
        blog=BlogPost.objects.all()
        serializer=BlogPost_serializers(blog,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=BlogPost_serializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','POST'])
def blog_details(request,pk):
    try:
        blog=BlogPost.objects.get(pk=pk)
    except BlogPost.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method=="GET":
        blog_serializer=BlogPost_serializers(blog)
        return Response(blog_serializer.data)
    
    elif request.method=="PUT":
        blog_serializer=BlogPost_serializers(blog,data=request.data)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return Response(blog_serializer.data,status=status.HTTP_200_OK)
        return Response(blog_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method=="DELETE":
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            