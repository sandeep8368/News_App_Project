from django.shortcuts import render



# Create your views here.
def news_view(request):
    msg1 = "India to face New Zealand in Champions Trophy Final, check possible playing XIs for IND vs NZ summit clash"
    msg2 = "Mitchell Santner gives final update on Matt Henry's injury and availability for Champions Trophy final against India"
    type = "news"
    my_dict = {"msg1":msg1,
               "msg2":msg2,
               "type":type}
    
    return render(request,'html/home.html',context=my_dict)


def sports_view(request):
    msg1 = "India to face New Zealand in Champions Trophy Final, check possible playing XIs for IND vs NZ summit clash"
    msg2 = "Mitchell Santner gives final update on Matt Henry's injury and availability for Champions Trophy final against India"
    type = "sports"
    my_dict = {"msg1":msg1,
               "msg2":msg2,
               "type":type}
    return render(request,'html/index.html',context=my_dict)


def movie_view(request):
    msg1 = "'Chhaava' crosses Rs 500 crore at the box office on day 23, the Vicky Kaushal starrer will now chase the record of Sunny Deol's 'Gadar 2'"
    msg2 = "5 Must-Watch Malayalam Thriller Movies On OTT: Watch Rekhachithram, Bramayugam, Sookshmadarshini And More"
    type = "movie"
    my_dict = {"msg1":msg1,
               "msg2":msg2,
               "type":type}
    return render(request,'html/index.html',context=my_dict)


def business_view(request):
    msg1 = "Namita Thapar breaks the bank for Shark Tank India pitchers rejected twice on the show, offers whopping Rs 150 crore valuation"
    msg2 = "A rooftop pool and city views in the technology district"
    type = "business"
    my_dict = {"msg1":msg1,
               "msg2":msg2,
               "type":type}
    return render(request,'html/index.html',context=my_dict)