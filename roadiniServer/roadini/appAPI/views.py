from django.shortcuts import render
from rest_framework import viewsets
from .models import PathsTable
from .serializers import PathsTableSerializer
import requests
import json
import os
from random import randint

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse # Create your views here.

class PathsTableView(viewsets.ModelViewSet):
    queryset = PathsTable.objects.all()
    serializer_class = PathsTableSerializer


def feed(request):
    
    feed = {"feed" :[ {"username" : "Tiago Ramalho", "location" : "Croacia", "description" : "Esta viagem foi muito fixe", "postId" : "1", "ownerId" : "1", "urlImage" : "https://scontent.flis7-1.fna.fbcdn.net/v/t1.0-9/20258438_1893652067570862_4019107659665964412_n.jpg?_nc_cat=111&oh=b69b337a86923445d87ed7b445acd224&oe=5C4F4156" },
        {"username" : "Luís Silva", "location" : "Belgica", "description" : "Esta viagem foi muito fixe", "postId" : "1", "ownerId" : "2", "urlImage" : "https://scontent.flis7-1.fna.fbcdn.net/v/t31.0-8/23735995_1674280279312175_7527285910664902411_o.jpg?_nc_cat=100&oh=52a827ec4e8488cf3664c944853e0d1c&oe=5C4C4ADB"}]}

    response = JsonResponse(feed, content_type='application/json')
    return response

def magicRoute(request):

    route = {"route" : [ {"categoryName" : "Restaurant", "categoryId" : "1", "placeName" : "Azur", "placeId" : "23", "placeDescription" : "This superbly located newbie sits by the entrance of Buža II, and quickly went to number one on TripAdvisor in its very first season. Here you can tuck into a reasonably priced, Med-and-Asian-influenced main here – fragrant meatballs in a chicken-coconut broth, perhaps, or Adriatic prawn pouches on grilled aubergine in a red-curry-and-coconut sauce – before an afternoon's sunbathing or nightcap overlooking the waves. Starters include mussels in beer butter and chili, and Dalmatian tom yum soup.", "urlImage" : "https://media.timeout.com/images/102323695/380/285/image.jpg" },
  {"categoryName" : "Beaches", "categoryId" : "2", "placeName" : "Banje Beach", "placeId" : "40", "placeDescription" : "Located in the extreme south coast of Croatia, Dubrovnik is one the country’s top travel destinations, in part because of the city’s many beaches. Banja Beach, located to the east of the city’s Old Town district, is particularly popular. The pebble beach is surrounded by some of Dubrovnik’s best hotels and is equipped with all the amenities that upscale travelers expect, including deck chairs, umbrellas and ranging rooms equipped with showers. The beach favored by celebrities is a great in-town spot to enjoy water sports like jet skiing and paragliding too.", "urlImage" : "https://www.touropia.com/gfx/d/best-beaches-in-croatia/banje_beach.jpg?v=1" } ]}

    response = JsonResponse(route, content_type='application/json')
    return response


def personalTrips(request):

    trips = {"trips" :[ {"name" : "Tiago Ramalho", "location" : "Croacia", "description" : "Um dos destinos de praia queridinhos dos viajantes low-cost é a Croácia, famosa pelas praias paradisíacas e águas cristalinas com preços muito mais atrativos que a Grécia e Itália. Fizemos uma viagem de 7 dias cruzando o país todinho e separamos aqui o roteiro completinho pra vocês.", "postId" : 1, "ownerId" : 1, "stars" : 72, "urlImage" : "http://3.bp.blogspot.com/-TmtrrRFfyic/UwUEz55bHkI/AAAAAAAAHxE/zrWxzfiKL9s/s1600/Navigator-Split-Return_mapa.jpg" },
  {"username" : "Tiago Ramalho", "location" : "Londres", "description" : " Nosso roteiro de 3 em Londres começa pela Tower Bridge, ponte que se levanta para passagens de barcos grandes, e pela Torre de Londres, um castelo medieval que abriga, entre outras coisas, a jóias da Coroa. Siga até a Catedral de Saint Paul, onde foi realizado o casamento Príncipe Charles e a Princesa Diana.  Você pode entrar na Catedral pra ver as criptas, e subir até o Domo (que tem uma vista linda de Londres). Em tempo, o caminho da Torre de Londres para a Catedral é bem bonito, com construções tradicionalmente inglesas misturadas com arranha-céus modernos. Catedral visitada, atravesse a Millennium Bridge vá explorar o Borough Market,um mercado bem típico de Londres. Você pode almoçar aqui, inclusive.", "postId" : 2, "ownerId" : 1, "stars" : 125, "urlImage" : "https://minhasviagensedestinos.files.wordpress.com/2012/07/roteiro-londres.jpg" },
  {"username" : "Tiago Ramalho", "location" : "Barcelona", "description" : "Plaça de La Catedral: é onde fica a Catedral de Barcelona. É cheia de gente e animada a qualquer hora. a Plaça Reial, que fica próxima as Ramblas e é uma pedida para sair a noite. Anote que os arredores da Plaça Reial estão cheios de bons restaurantes para uma pausa pro almoço. Uma das indicações é o Los Caracoles, com pratos típicos catalões Els Quatre Gats: o bar inspirado no Le Chat Noir de Paris teve entre seus frequentadores Pablo Picasso e Antoni Gaudi. É um clássico, e que serve delicias ", "postId" : 3, "ownerId" : 1, "stars" :93, "urlImage" : "http://www.mundoemprosa.com.br/site/wp-content/uploads/2016/05/roteiro-barri-gotic.jpg" } ]}

    response = JsonResponse(trips, content_type='application/json')
    return response

##GEO
def get_user_lists(request):
    headers = {'Content-type': 'application/json'}
    r = requests.get('http://geoclust_api:3001/api/v1/lists/user/1', headers=headers)
    if(r.status_code==200):
        json_response = {}
        json_data = json.loads(r.text) 
        list_lists = []
        for l in json_data["result"]:
            json_tmp = {}
            json_tmp["listName"] = l["list_name"]
            json_tmp["listId"] = l["id"]
            json_tmp["userId"] = l["user_id"]

            url1 = 'http://geoclust_api:3001/api/v1/visits/list/' + str(l["id"])
            print(url1)
            r1 = requests.get(url1, headers=headers)
            list_items = []
            if(r1.status_code == 200):
                json_tmp1 = {}
                json_data1 = json.loads(r1.text)
                l1 = json_data1["result"]
                print(l1)
                if(l1["review"] != ""):
                    description = l1["review"] 
                else:
                    description = None 


                url2 = 'http://geoclust_api:3001/api/v1/gspots/' + str(l1["internal_id_place"])
                print(url2)
                r2 = requests.get(url2, headers=headers)
                if(r2.status_code == 200):
                    json_data2 = json.loads(r2.text)
                    l2 = json_data2["result"]
                    json_tmp1["location"] = l2["address"]
                    json_tmp1["name"] = l2["name"]
                    json_tmp1["listId"] = l["id"]
                    json_tmp1["stars"] = randint(0, 9)
                    json_tmp1["urlImage"] = "https://www.google.pt/images/branding/googlelogo/1x/googlelogo_white_background_color_272x92dp.png"
                    json_tmp1["postId"] = l2["id"]
                    json_tmp1["description"] = description

                    list_items.append(json_tmp1)
            json_tmp["listItem"] = list_items
            list_lists.append(json_tmp)
        json_response["result"] = list_lists
        print(json_response)
        response = JsonResponse(json_response, content_type='application/json')
    return response

def near_places(request):
    headers = {'Content-type': 'application/json'}
    r = requests.get(' http://geoclust_api:3001/api/v1/gspots', headers=headers)
    if(r.status_code==200):
        json_response = {}
        json_data = json.loads(r.text) 


        json_response["listPlaces"] = json_data["result"]
        print(json_response)
        response = JsonResponse(json_response, content_type='application/json')
    response = JsonResponse(json_response, content_type='application/json')
    return response

def list_name(request, user_id):
    headers = {'Content-type': 'application/json'}
    r = requests.get('http://geoclust_api:3001/api/v1/lists/user/1', headers=headers)
    if(r.status_code==200):
        json_response = {}
        json_data = json.loads(r.text) 
        list_lists = []
        for l in json_data["result"]:
            json_tmp = {}
            json_tmp["listName"] = l["list_name"]
            json_tmp["listId"] = l["id"]
            json_tmp["userId"] = l["user_id"]
            list_lists.append(json_tmp)

        json_response["result"] = list_lists
        print(json_response)
        response = JsonResponse(json_response, content_type='application/json')
    return response

@csrf_exempt
def add_item_list(request):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    new_list = {"list_id":int(request.POST["listId"]), "internal_id_place":int(request.POST["itemId"]), "review": request.POST["review"]}
    jsonData = json.dumps(new_list)
    r = requests.post('http://geoclust_api:3001/api/v1/visits', data=jsonData, headers=headers)
    print(r.text)
    if(r.status_code == 200):
        json_data = json.loads(r.text) 
    else:
        json_data = {"status":False}
    
    response = JsonResponse(json_data, content_type='application/json')
    return response


@csrf_exempt
def create_list(request):
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

    name = request.POST["name"];
    new_list = {"user_id":1, "list_name":name}
    jsonData = json.dumps(new_list)
    r = requests.post('http://geoclust_api:3001/api/v1/lists', data=jsonData, headers=headers)
 
    if(r.status_code == 200):
        json_data = json.loads(r.text) 
        print(json_data)
    else:
        json_data = {"status":False}
        response = JsonResponse(json_data, content_type='application/json')
        return response
    response = JsonResponse(json_data, content_type='application/json')
    return response

##CDN
def save_on_cdn(request):
    module_dir = os.path.dirname(__file__)  # get current directory
    file_path = os.path.join(module_dir, 'transferir.jpeg')
    data = open(file_path,'rb').read()
    r = requests.post('http://cdnapi:9001/api/v1_0/user',data=data)

    print(type(r))
    print(r.status_code)
    print(r.headers)
    print(r)
