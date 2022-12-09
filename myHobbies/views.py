from django.shortcuts import render

hobbies_list = {
    "Tech Savvy": [
        "One of my favorite passions is tecnology, I'm keen in knowing the best of companies new products, such as Apple, Samsung, Google, ... I love to dive deep in each new feature from software updates and make the best of it.",
        "images/hobbies_img1.png"
    ],
    "Cycling": [
        "By fare, one of my deepest affections has been watching the Tour de France every year and as well hoping that one day a French/Italian wins!",
        "images/hobbies_img2_2.jpeg"
    ],
    "Puzzles": [
        "Challenges has to be among the biggest affections of mine, the ultimate goal is to successfully complete, finish some task. Until now. my greatest jigsaw-puzzle has been a 5000 pc. from a sewing studio",
        "images/hobbies_img3.jpg"
    ],
    "Sports": [
        "The diversity among sports might facinate you, because from curling, skiing to american sports (basketball, hockey, football, baseball) or even to tennis, golf, you name it!",
        "images/hobbies_img4.jpg"
    ],
    "Movie Enthusiastic": [
        "What a better way to get inspired and meditate on some social topic than watching a movie and raking it?",
        "images/hobbies_img5.jpg"
    ],
    "High-Functional Social Analytical": [
        "TBD jaklsd;fjasdl;kjfasdlk jkasdfjksdjf iweruwdn dfa sdjfh eiwi fdnsfiw nfasdoiuhdpudfiu ifdfiasdifjs di fosdijpqoweinv fd  sdf",
        "images/hobbies_img6.jpeg"  # Sherlock Holmes Photo
    ]

}

# Create your views here.
def index(request):
    my_hobbies = hobbies_list.items()
    # return HttpResponse("Hello World! This is My Hobbies webpage!")
    return render(request, "myHobbies/index.html", {
        "hobbies": my_hobbies
    })
