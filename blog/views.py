from django.shortcuts import render



posts = [
    {
    'poster': 'Ahmad Naji',
    'Title': 'Django framework',
    'content': 'django content goes here',
    'post_date': 'August 12 2023'
    },
    {
    'poster': 'Ali Naji',
    'Title': 'Java spring boot',
    'content': 'spring content goes here',
    'post_date': 'september 12 2023'
    }
]

context = {'posts': posts}
def home(request):
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')