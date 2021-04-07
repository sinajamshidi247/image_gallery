from django.shortcuts import render , redirect
from .models import Category , Photo

def home(request):
    category = request.GET.get('category')
    
    if category == None :
        photos = Photo.objects.all()
    else:
       photos = Photo.objects.filter(category__name=category)

    categories = Category.objects.all()

    return render(request,'photo/home.html',{'photos':photos,'categories':categories})



def detail(request,pk):
    photo= Photo.objects.get(id=pk)


    return render(request,'photo/detail.html',{'photo':photo})




def addPhoto(request):
    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        images = request.FILES.getlist('images') #list of  images 

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
        else:
            category = None

        for image in images:
            photo = Photo.objects.create(
                category=category,
                description=data['description'],
                image=image,
            )

        return redirect('photo:home')

    context = {'categories': categories}
    return render(request, 'photo/add.html', context)
