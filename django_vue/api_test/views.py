from django.forms import model_to_dict
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.core import serializers
from django.http import JsonResponse
import json
from .models import User
from .models import Movies
from .models import popular_movies
from .models import User_evaluate


@require_http_methods(["GET"])
def add_user(request):
    response = {}
    try:
        user = User(user_name=request.GET.get('user_name'),user_password=request.GET.get('user_password'))
        user.save()
        response['msg'] = 'success'
        response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def login_users(request):
    response = {}
    try:
        user_name = request.GET.get('user_name')
        user_password = request.GET.get('user_password')
        users = User.objects.get(user_name=user_name,user_password=user_password)
        if users != 'null':
            response['msg'] = 'success'
            response['error_num'] = 0
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
    return JsonResponse(response)


@require_http_methods(["GET"])
def init_data(request):
    response = {}
    try:
        num = request.GET.get('NUM')      #初始化数量
        print("this is init_num:",num)
        
        moive_data = popular_movies.objects.all()    #得到热门电影表中的前init_num个电影信息

        components = serializers.serialize("json", moive_data)


        if moive_data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)



@require_http_methods(["GET"])
def get_data(request):
    response = {}
    try:
        NAME = request.GET.get('NAME')      
        print("name",NAME)
        moive_data = Movies.objects.filter(NAME=NAME)   
      
        components = serializers.serialize("json", moive_data)

        if moive_data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)



@require_http_methods(["GET"])
def sos_data(request):
    response = {}
    try:
        name = request.GET.get('NAME')      #初始化数量
        print("this is name:",name)
        
        moive_data = Movies.objects.filter(NAME=name)    #得到热门电影表中的前init_num个电影信息

        components = serializers.serialize("json", moive_data)

  
        if moive_data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)



#保存用户评分
@require_http_methods(["GET"])
def save_evaluate(request):
    response = {}
    
    user_name = request.GET.get('USER_NAME')      #要用户名，电影名，评价的分数
    movie_name = request.GET.get('MOVIE_NAME')
    score = request.GET.get('SCORE')
    movie_id = request.GET.get('MOVIE_ID')

    print("查看能否这样传:",user_name,movie_name,score)
    #先获得数据库评价表中该用户对这个电影的评价数，若为>0,则进行更新，若无，则增加
    num = User_evaluate.objects.filter(MOVIE_ID=movie_id,USER_NAME=user_name,MOVIE_NAME=movie_name).count()    #得到热门电影表中的前init_num个电影信息

    if num > 0:
        User_evaluate.objects.filter(MOVIE_ID=movie_id,USER_NAME=user_name,MOVIE_NAME=movie_name).update(SCORE=score)
    else:
        User_evaluate.objects.create(MOVIE_ID=movie_id,USER_NAME=user_name,MOVIE_NAME=movie_name,SCORE=score)
        

    return JsonResponse(response,safe=False)
    

@require_http_methods(["GET"])
def get_evaluate(request):
    response = {}
    try:
        user_name = request.GET.get('USER_NAME')      #要用户名，电影名，评价的分数
        movie_name = request.GET.get('MOVIE_NAME')

        print("查看能否这样传:",user_name,movie_name)
        #先获得数据库评价表中该用户对这个电影的评价数，若为>0,则进行更新，若无，则增加
        num = User_evaluate.objects.filter(USER_NAME=user_name,MOVIE_NAME=movie_name).count()    #得到热门电影表中的前init_num个电影信息

        if num > 0:
            data = User_evaluate.objects.filter(USER_NAME=user_name,MOVIE_NAME=movie_name)
            components = serializers.serialize("json", data)
        

        if data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1
        
    return JsonResponse(response,safe=False)


@require_http_methods(["GET"])
def other_page(request):
    response = {}
    try:
        classify = request.GET.get('CLASSIFY')      #初始化数量
        page = request.GET.get('PAGE')
        size = request.GET.get('SIZE')
        print(classify,page,size)
        # page:请求的页数 如：1,2,3,4,5
        # size:请求页数的大小 如：10,20,30,40

        # data = Movies.objects.filter(GENRES__contains=classify)[10:30] 
        data = Movies.objects.filter(GENRES__contains=classify)[(int(page)-1)*int(size):(int(page)-1)*int(size)+int(size)] 
        length1 = Movies.objects.filter(GENRES__contains=classify)

        components = serializers.serialize("json", data)
        components[:2]+'\"totalnum\":'+str(len(length1))+','+components[2:]

        if data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)



@require_http_methods(["GET"])
def get_classify(request):
    response = {}
    try:
        classify = request.GET.get('CLASSIFY')      

        print("classify:",classify)

        data = Movies.objects.filter(GENRES__contains=classify)[0:20] 
        print("data:",data)
        print("len:",len(data))
        components = serializers.serialize("json", data)


        if data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)



@require_http_methods(["GET"])
def test_data(request):
    response = {}
    try:
        # NAME = request.GET.get('NAME')      #初始化数量
        # print("this is init_num:",NAME)
        
        moive_data = popular_movies.objects.filter(location="中国")    #得到热门电影表中的前init_num个电影信息

        components = serializers.serialize("json", moive_data)

        print("111components:",components)
        # data = json.dumps({"value": components})
        print("this is context:",moive_data)
        if moive_data != 'null':
            response = components
        else:
            response['msg'] = 'e'
            response['error_num'] = 0
    except  Exception as e:
        response['msg'] = str(e)
        response['error_num'] = 1

    return JsonResponse(response,safe=False)

# @require_http_methods(["GET"])
# def popular_movies(request):
#     pass