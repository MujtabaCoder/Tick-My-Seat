from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse,HttpResponseRedirect
from .models import Movie,Cinema, Genre, Language, Format,Cast,Crew
from django.db.models import Q

# Create your views here.
class MovieCls():
    
    def base(self,request):
        return render(request,"base.html")
    
    def add_movie_page(self,request):
        cinemas = Cinema.objects.all()
        genres = Genre.objects.all()
        languages = Language.objects.all()
        formats = Format.objects.all()
        return render(request,"add-movie.html", {'cinemas': cinemas, 'genres': genres, 'languages': languages, 'formats': formats})
    

    def add_movie(self, request):
        if request.method == 'POST':
            print(request.POST)
            # Extract data from the form
            movienain = request.POST.get('movienain')
            movienaar = request.POST.get('movienaar')
            redate = request.POST.get('redate')
            tedate = request.POST.get('tedate')
            mduration = request.POST.get('mduration')
            mdiscription = request.POST.get('mdiscription')
            mdiscriptionar = request.POST.get('mdiscriptionar')
            Rating = request.POST.get('Rating')
            trailer = request.POST.get('trailer')

            cinema_ids = request.POST.get('cinemas')
            cinemas = [Cinema.objects.get(id=int(cinema_id)) for cinema_id in cinema_ids]
            # Handle multiple cinemas
            # cinema_ids = request.POST.get('cinema')
            # print("Cinemas:", cinema_ids,"---------_++++++++++++++++++-------------------------")
            # cinema_id = [Cinema.objects.get(id=int(cinema_id)) for cinema_id in cinema_ids]
            # print("Cinemas:", cinema_id,"-----------------------------------------------")
            # Handle multiple genres
            genre_ids = request.POST.get('genres')
            genres = [Genre.objects.get(id=int(genre_id)) for genre_id in genre_ids]

            # Handle multiple languages
            language_ids = request.POST.get('languages')
            languages = [Language.objects.get(id=int(language_id)) for language_id in language_ids]

            # Handle multiple formats
            format_ids = request.POST.get('formats')
            formats = [Format.objects.get(id=int(format_id)) for format_id in format_ids]

            # Handle multiple casts
            cast_instances = []
            cast_name_english = request.POST.getlist('cast_name_english')
            cast_name_arabic = request.POST.getlist('cast_name_arabic')
            cast_role_english = request.POST.getlist('cast_role_english')
            cast_role_arabic = request.POST.getlist('cast_role_arabic')

            for i in range(len(cast_name_english)):
                cast_instance = Cast.objects.create(
                    name_english=cast_name_english[i],
                    name_arabic=cast_name_arabic[i],
                    role_english=cast_role_english[i],
                    role_arabic=cast_role_arabic[i]
                )
                cast_instances.append(cast_instance)

            # Handle multiple crews
            crew_instances = []
            crew_name_english = request.POST.getlist('crew_name_english')
            crew_name_arabic = request.POST.getlist('crew_name_arabic')
            crew_role_english = request.POST.getlist('crew_role_english')
            crew_role_arabic = request.POST.getlist('crew_role_arabic')

            for i in range(len(crew_name_english)):
                crew_instance = Crew.objects.create(
                    name_english=crew_name_english[i],
                    name_arabic=crew_name_arabic[i],
                    role_english=crew_role_english[i],
                    role_arabic=crew_role_arabic[i]
                )
                crew_instances.append(crew_instance)

            # Create Movie instance
            movie = Movie.objects.create(
                movienain=movienain,
                movienaar=movienaar,
                redate=redate,
                tedate=tedate,
                mduration=mduration,
                mdiscription=mdiscription,
                mdiscriptionar=mdiscriptionar,
                Rating=Rating,
                trailer=trailer,
                cinema_id=cinema_ids,
                genre_id=genre_ids,
                language_id=language_ids,
                format_id=format_ids,
                
            )
            movie.casts.add(*cast_instances)
            movie.crews.add(*crew_instances)
            print("Cinemas:", cinemas,"-----------------------------------------------")
            print("Genres:", genres)
            print("Languages:", languages)
            print("Formats:", formats)
            print("Cast Instances:", cast_instances)
            print("Crew Instances:", crew_instances)
            print("Movie Instance:", movie)


            # Associate the Movie with the selected objects
            
            


            return redirect('movie_data_page')
                

       
    
    def update_movie_page(self,request):
        movie_id= request.GET.get('movie_id')
        movie = Movie.objects.get(id=movie_id)

        cinema_name = movie.cinema.name if movie.cinema else "N/A"
        genre_name = movie.genre.name if movie.genre else "N/A"
        language_name = movie.language.name if movie.language else "N/A"
        format_name = movie.format.name if movie.format else "N/A"

        cinemas = Cinema.objects.all()
        genres = Genre.objects.all()
        languages = Language.objects.all()
        formats = Format.objects.all()
        return render(request,"update_movie.html", {'movie': movie ,'cinema_name': cinema_name,'genre_name': genre_name,'language_name': language_name,'format_name': format_name,'cinemas': cinemas, 'genres': genres, 'languages': languages, 'formats': formats })
    
    
    def movie_data_page(self,request):
        query = request.GET.get('q', '')  # Get the search query from the URL parameter 'q'
        movies = Movie.objects.filter(Q(movienain__icontains=query))
        
        return render(request, 'movie_list.html', {'movies':movies, 'query': query})
    
    def update_movie(self,request):
        if request.method == 'POST':
            movie_id = request.POST.get('movie_id')
            
                        
            Movie.objects.filter(id=movie_id).update(
            cinema_id=request.POST.get('cinema'),
            genre_id=request.POST.get('genere'),
            language_id=request.POST.get('language'),
            format_id=request.POST.get('format'),
            movienain = request.POST.get('movienain'),
            movienaar  = request.POST.get('movienaar'),
            redate= request.POST.get('redate'),
            tedate = request.POST.get('tedate'),
            mduration = request.POST.get('mduration'),
            mdiscription = request.POST.get('mdiscription'),
            mdiscriptionar  = request.POST.get('mdiscriptionar'),
            Rating  = request.POST.get('Rating'),
            trailer  = request.POST.get('trailer'),
            )
            
        # Handle form submission
            

        return redirect('movie_data_page')
        
    def delete_movie(self,request):
        
        movie_id= request.GET.get('movie_id')
        Movie.objects.filter(id=movie_id).delete()
        return redirect('movie_data_page')
    
    def movie_profile(self,request):
       
            movie_id = request.GET.get('movie_id')
            movie = Movie.objects.get(id=movie_id) 

            cinema_name = movie.cinema.name if movie.cinema else "N/A"
            genre_name = movie.genre.name if movie.genre else "N/A"
            language_name = movie.language.name if movie.language else "N/A"
            format_name = movie.format.name if movie.format else "N/A"

            
            return render(request, 'movies_details.html', {'movie': movie,'cinema_name': cinema_name,'genre_name': genre_name,'language_name': language_name,'format_name': format_name,})
