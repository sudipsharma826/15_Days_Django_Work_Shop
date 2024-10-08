from django.shortcuts import render,redirect,get_object_or_404
from ..models import Blogs
from django.contrib.auth.decorators import login_required


def home(request):
    blogs = Blogs.objects.all()
    return render(request,'main/home.html',{'blogs' : blogs})

def single_blog(request,blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id);
    return render(request,"main/single_blog.html",{"blog":blog})

@login_required
def edit_blog(request, blog_id):
    # Retrieve the blog object before processing the request
    blog = get_object_or_404(Blogs, pk=blog_id)

    # Check if the current user is the author of the blog
    if request.user != blog.author:
        return redirect("home")  # Redirect if user is not authorized

    if request.method == "POST":
        title = request.POST.get("title")
        subtitle = request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        # Update the blog object with new data
        blog.title = title
        blog.subtitle = subtitle
        blog.description = description
        if image:
            blog.image = image
        
        blog.save()  # Save the updated blog object
        return redirect("home")  # Redirect after saving

    # Render the edit blog template with the blog data
    return render(request, "main/edit_blog.html", {"blog": blog})
@login_required
# Login to get acess to the create blog page
def create_blog(request):
    if request.method == "POST":
        title = request.POST.get("title")
        subtitle =  request.POST.get("subtitle")
        description = request.POST.get("description")
        image = request.FILES.get("image")
        blog = Blogs(title=title,subtitle=subtitle,description=description,image=image,author=request.user)
        blog.save()
        return redirect("home")
  
    return render(request,"main/create_blog.html")
@login_required
def delete_blog(request,blog_id):
    blog = get_object_or_404(Blogs,pk=blog_id)
    if request.method == "POST" and request.user == blog.author:
        # We need to deleted the blog if delete request is triggeded from the form post request
      blog.delete()
      return redirect("home")
    else:
       return redirect ("blog/"+str(blog_id))
    