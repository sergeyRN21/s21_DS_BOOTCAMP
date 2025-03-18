from collections import Counter, OrderedDict, defaultdict
import re
import datetime
import os
import requests
from bs4 import BeautifulSoup
import pytest

class Movies:
    """
    Analyzing data from movies.csv
    """
    _correct_file_read = True
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """    
        self.path_to_the_file = path_to_the_file
        self.lines = self.read_file()

    def read_file(self, count_lines=1000):
        if self._correct_file_read:
            try:
                with open(self.path_to_the_file, 'r') as file:
                    next(file)
                    lines = []
                    for i, line in enumerate(file):
                        if i == count_lines:
                            break
                        lines.append(line)
                return lines
            except FileNotFoundError:
                print(f"Файл {self.path_to_the_file} не найден")
                self._correct_file_read = False
            except Exception as e:
                print(f"Произошла ошибка:{e}")
                self._correct_file_read = False
        return None
        
    def dist_by_release(self):
        """
        The method returns a dict or an OrderedDict where the keys are years and the values are counts. 
        You need to extract years from the titles. Sort it by counts descendingly.
        """
        if self._correct_file_read:
            try:
                year_pattern = r'\b(?:\d{4})\b'
                counter = Counter()
                for line in self.lines:
                    title = line.split(',')[1].strip()
                    match = re.search(year_pattern, title)

                    if match:
                        year = int(match.group())
                        counter[year] += 1

                release_years = OrderedDict(
                    sorted(counter.items(), key=lambda item: item[1], reverse=True)
                )
                return release_years
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

    def dist_by_genres(self):
        """
        The method returns a dict where the keys are genres and the values are counts.
     Sort it by counts descendingly.
        """
        if self._correct_file_read:
            try:
                counter = Counter()
                for line in self.lines:
                    title = line.split(',')[2].strip()
                    genres = title.split('|')

                    for genre in genres:
                        genre = genre.strip().replace(':', '').replace(',', '')
                
                        if genre and genre.isalpha():  
                            counter[genre] += 1  

                genres = OrderedDict(
                    sorted(counter.items(), key=lambda item: item[1], reverse=True)
                )
                return genres
            except FileNotFoundError:
                print(f"Файл {self.path_to_the_file} не найден")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

    def most_genres(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and 
        the values are the number of genres of the movie. Sort it by numbers descendingly.
        """
        if self._correct_file_read:
            try:
                movies = {}
                for line in self.lines:
                    parts = line.strip().split(',')
                    title = parts[1]
                    genres = parts[2].strip().split('|')
                    genres = [g.strip().replace(':', '').replace(',', '') for g in genres if g.strip()]
                    if genres:
                        movies[title] = len(genres)

                sorted_movies = sorted(movies.items(), key=lambda x:x[1], reverse=True)
                movies = OrderedDict(sorted_movies[:n])

                return movies
            except FileNotFoundError:
                print(f"Файл {self.path_to_the_file} не найден")
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

class Ratings:
    """
    Analyzing data from ratings.csv
    """
    
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        self.path_to_the_file = path_to_the_file
        self.movies = self.Movies(self)
        self.users = self.Users(self)
        self._correct_file_read = True
        self.lines = self.movies.read_file()
        

    class Movies:
        def __init__(self, outter_object):
            self.outter_object = outter_object
            

        def read_file(self, count_lines=1000):
            if self.outter_object._correct_file_read:
                try:
                    with open(self.outter_object.path_to_the_file, 'r') as file:
                        next(file)
                        lines = []
                        for i, line in enumerate(file):
                            if i == count_lines:
                                break
                            lines.append(line)
                        lines = file.readlines()
                    return lines
                except FileNotFoundError:
                    print(f"Файл {self.outter_object.path_to_the_file} не найден")
                    self.outter_object._correct_file_read = False
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
                    self.outter_object._correct_file_read = False
            return None

        def dist_by_year(self):
            """
            The method returns a dict where the keys are years and the values are counts. 
            Sort it by years ascendingly. You need to extract years from timestamps.
            """
            if self.outter_object._correct_file_read:
                try:
                    counter = Counter()
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        timestamp = int(parts[3])
                        date = datetime.datetime.fromtimestamp(timestamp)
                        year = str(date.year)
                        counter[year] += 1
                    ratings_by_year = sorted(counter.items(), key=lambda x: x[0], reverse=False)
                    return ratings_by_year
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None

        def dist_by_rating(self):
            """
            The method returns a dict where the keys are ratings and the values are counts.
         Sort it by ratings ascendingly.
            """
            if self.outter_object._correct_file_read:
                try:
                    rating_counter = Counter()
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        rating = float(parts[2])
                        rating_counter[rating] += 1
                    ratings_distribution = sorted(rating_counter.items(), key=lambda x:x[0], reverse=False)
                    return ratings_distribution
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None

        def top_by_num_of_ratings(self, n):
            """
            The method returns top-n movies by the number of ratings. 
            It is a dict where the keys are movie titles and the values are numbers.
     Sort it by numbers descendingly.
            """
            if self.outter_object._correct_file_read:
                try:
                    movie_count = defaultdict(int)
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        title = parts[1]
                        movie_count[title] += 1

                    movie_sort = sorted(movie_count.items(), key=lambda x:x[1], reverse=True)
                    top_movies = OrderedDict(movie_sort[:n])
                    return top_movies
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None

        def top_by_ratings(self, n):
            """
            The method returns top-n movies by the average or median of the ratings.
            It is a dict where the keys are movie titles and the values are metric values.
            Sort it by metric descendingly.
            The values should be rounded to 2 decimals.
            """
            if self.outter_object._correct_file_read:
                try:
                    movie_ratings = defaultdict(list)
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        title = parts[1]
                        rating = float(parts[2])
                        movie_ratings[title].append(rating)
                    movie_metric = { title: round(sum(ratings) / len(ratings), 2) for title, ratings in movie_ratings.items()}                
                    sorted_movies = sorted(movie_metric.items(), key=lambda x:x[1], reverse=True)
                    top_movies = dict(sorted_movies[:n])
                    return top_movies
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None
        
        def top_controversial(self, n):
            """
            The method returns top-n movies by the variance of the ratings.
            It is a dict where the keys are movie titles and the values are the variances.
          Sort it by variance descendingly.
            The values should be rounded to 2 decimals.
            """
            if self.outter_object._correct_file_read:
                try:
                    movie_rating = defaultdict(list)
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        title = parts[1]
                        rating = float(parts[2])
                        movie_rating[title].append(rating)
                    movie_variance = {}
                    for title, ratings in movie_rating.items():
                        mean = sum(ratings) / len(ratings)
                        variance = sum((rating - mean)**2 for rating in ratings) / len(ratings)
                        movie_variance[title] = round(variance, 2)
                    sorted_movies = {k: v for k, v in sorted(movie_variance.items(), key=lambda x:x[1], reverse=True) }
                    top_movies = dict(list(sorted_movies.items())[:n])
                    return top_movies
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None
        
    class Users(Movies):
        """
        In this class, three methods should work. 
        The 1st returns the distribution of users by the number of ratings made by them.
        The 2nd returns the distribution of users by average or median ratings made by them.
        The 3rd returns top-n users with the biggest variance of their ratings.
     Inherit from the class Movies. Several methods are similar to the methods from it.
        """
        def get_count_user_rating_distribution(self):
            if self.outter_object._correct_file_read:
                try:
                    user_counter = Counter()
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        user_title = parts[0]
                        user_counter[user_title] += 1
                    user_distribution = sorted(user_counter.items(), key=lambda x:x[1], reverse=True)
                    return dict(user_distribution)
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None

        def user_top_by_ratings(self):
            if self.outter_object._correct_file_read:
                try:
                    user_movie_ratings = defaultdict(list)
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        user_title = parts[0]
                        user_ratings = float(parts[2])
                        user_movie_ratings[user_title].append(user_ratings)
                    user_movie_metric = { user_title: round(sum(user_ratings) / len(user_ratings), 2) for user_title, user_ratings in user_movie_ratings.items()}
                    sorted_user_movies = sorted(user_movie_metric.items(), key=lambda x:x[1], reverse=True)
                    top_user_rating = dict(sorted_user_movies)
                    return top_user_rating
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None
                
        def top_user_controversial(self, n):
            if self.outter_object._correct_file_read:
                try:
                    user_movie_rating = defaultdict(list)
                    for line in self.outter_object.lines:
                        parts = line.strip().split(',')
                        user_title = parts[0]
                        user_ratings = float(parts[2])
                        user_movie_rating[user_title].append(user_ratings)
                    user_variance = {}
                    for user_title, user_ratings in user_movie_rating.items():
                        mean = sum(user_ratings) / len(user_ratings)
                        variance = sum((rating - mean)**2 for rating in user_ratings) / len(user_ratings)
                        user_variance[user_title] = round(variance, 2)
                    sorted_user_variance = {k:v for k, v in sorted(user_variance.items(), key=lambda x:x[1], reverse=True)}
                    top_user_movies = dict(list(sorted_user_variance.items())[:n])
                    return top_user_movies
                except Exception as e:
                    print(f"Произошла ошибка: {e}")
            return None

class Tags:
    """
    Analyzing data from tags.csv
    """
    _correct_file_read = True
    def __init__(self, path_to_the_file):
        self.path_to_the_file = path_to_the_file
        self.lines = self.read_file()
        
    def read_file(self, count_lines=1000):
        if self._correct_file_read:
            try:
                with open(self.path_to_the_file, 'r') as file:
                    next(file)
                    lines = []
                    for i, line in enumerate(file):
                        if i == count_lines:
                            break
                        lines.append(line)
                return lines
            except FileNotFoundError:
                print(f"Файл {self.path_to_the_file} не найден")
                self._correct_file_read = False
            except Exception as e:
                print(f"Произошла ошибка:{e}")
                self._correct_file_read = False       
        return None

    def most_words(self, n):
        """
        The method returns top-n tags with most words inside. It is a dict 
        where the keys are tags and the values are the number of words inside the tag.
        Drop the duplicates. Sort it by numbers descendingly.
        """
        if self._correct_file_read:
            try:
                tags = []
                for row in self.read_file():
                    tags.append(row.split(',')[2])
                tag_word = {tag: len(tag.split()) for tag in tags}
                tag_word = sorted(tag_word.items(), key=lambda item: item[1], reverse=True)
                big_tags = dict(tag_word[:n])
                
                return big_tags
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

    def longest(self, n):
        """
        The method returns top-n longest tags in terms of the number of characters.
        It is a list of the tags. Drop the duplicates. Sort it by numbers descendingly.
        """
        if self._correct_file_read:
            try:
                tags = []
                seen_tags = set()
                for row in self.read_file():
                    tag = row.split(',')[2]
                    if tag not in seen_tags:   
                        seen_tags.add(tag)
                        tags.append(tag)
                tag_char = {tag: len(tag) for tag in tags}
                tag_char = sorted(tag_char.items(), key=lambda item: item[1], reverse=True)
                big_tags = tag_char[:n]
                return big_tags
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

    def most_words_and_longest(self, n):
        """
        The method returns the intersection between top-n tags with most words inside and 
        top-n longest tags in terms of the number of characters.
        Drop the duplicates. It is a list of the tags.
        """
        if self._correct_file_read:
            try:
                word = set(self.most_words(n).keys())
                long = set(dict(self.longest(n)).keys())
                big_tags = list(word & long)
                return big_tags
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

    def most_popular(self, n):
        """
        The method returns the most popular tags. 
        It is a dict where the keys are tags and the values are the counts.
        Drop the duplicates. Sort it by counts descendingly.
        """
        if self._correct_file_read:
            try:
                tags = []
                seen_tags = set()
                for row in self.read_file():
                    tags.append(row.split(',')[2])
                tag_count = {tag: tags.count(tag) for tag in tags}
                tag_count = sorted(tag_count.items(), key=lambda item: item[1], reverse= True)
                popular_tags = dict(tag_count[:n])
                return popular_tags
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None
        
    def tags_with(self, word):
        """
        The method returns all unique tags that include the word given as the argument.
        Drop the duplicates. It is a list of the tags. Sort it by tag names alphabetically.
        """
        if self._correct_file_read:
            try:
                tags = []
                tags_with_word = []
                seen_tags = set()
                for row in self.read_file():
                    tag = row.split(',')[2]
                    if tag not in seen_tags:   
                        seen_tags.add(tag)
                        tags.append(tag)
                for tag in tags:
                    if word in tag:
                        tags_with_word.append(tag)
                tags_with_word = sorted(tags_with_word)
                return tags_with_word
            except Exception as e:
                print(f"Произошла ошибка: {e}")
        return None

class Links:
    """
    Analyzing data from links.csv
    """
    _correct_file_read = True
    def __init__(self, path_to_the_file):
        """
        Put here any fields that you think you will need.
        """
        try:
            self.path_to_the_file = path_to_the_file
            list_of_movies = self.reader()
            list_of_fields = ["Director", "Budget", "Gross worldwide", "Runtime", "Stars", "Title"]
            self.imdb_info = self.get_imdb(list_of_movies, list_of_fields)
        except FileNotFoundError as e:
            print(f'Error: {str(e)}')
            self._correct_file_read = False
            self.imdb_info = []
        
       
    def reader(self, count_lines=50):
        if self._correct_file_read:
            links = {}
            with open(self.path_to_the_file) as f:
                next(f)
                for i, row in enumerate(f):
                    if i == count_lines:
                        break
                    movieid = row.split(',')[0]
                    imdbid = row.split(',')[1]
                    links[int(movieid)] = imdbid.strip()
            return links
        return {}
        
    @staticmethod
    def get_imdb(list_of_movies, list_of_fields):
        """
        The method returns a list of lists [movieId, field1, field2, field3, ...] for the list of movies given as the argument (movieId).
        For example, [movieId, Director, Budget, Cumulative Worldwide Gross, Runtime].
        The values should be parsed from the IMDB webpages of the movies.
        Sort it by movieId descendingly.
        """
        imdb_info = []
        for movie in list_of_movies:
            imdb = list_of_movies[movie]
            headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
            url = f'https://www.imdb.com/title/tt{imdb}/'
            movie_data = [imdb]
            r = requests.get(url, headers=headers)
            if r.status_code != 200:
                raise Exception(f"Error {r.status_code}: Unable to fetch data from URL {url}")
            
            soup = BeautifulSoup(r.text, 'html.parser')
            
            for field in list_of_fields:
                field_tag = soup.find(string=field)
                if field == "Writers":
                    item_string = (
                        ", ".join(
                            a.text.strip()
                            for a in field_tag.find_next("div").find_all("a")
                        )
                        if field_tag
                        else "n/a"
                    )
                elif field == "Director" and field_tag == None:
                    field_tag = soup.find(string="Directors")
                    item_string = (
                        field_tag.find_next("div").find_next("a").text.strip()
                        if field_tag
                        else None
                    )
                elif field in {"Director", "Stars"}:
                    item_string = (
                        field_tag.find_next("a").text.strip() if field_tag else None
                    )
                elif field == "Title":
                    field_tag = soup.find(class_="hero__primary-text")
                    item_string = field_tag.text.strip() if field_tag else None
                else:
                    item_string = (
                        field_tag.find_next().text.strip() if field_tag else "n/a"
                    )
                
                movie_data.append(item_string)
            imdb_info.append(movie_data)

        return imdb_info
    
    @staticmethod
    def sort_dict_top_n(movie_dict, n):
        sorted_dict = dict(sorted(movie_dict.items(), key=lambda x: x[1], reverse=True))
        return dict(list(sorted_dict.items())[:n])
        
    def top_directors(self, n):
        """
        The method returns a dict with top-n directors where the keys are directors and 
        the values are numbers of movies created by them. Sort it by numbers descendingly.
        """
        if self._correct_file_read:
            list_of_directors = [item[1] for item in self.imdb_info]
            directors_dict = Counter(list_of_directors)
            directors = directors_dict.most_common(n)
            return dict(directors)
        return None
    
    @staticmethod
    def clean_budget(budget_str):
        clean = ""
        for symbol in budget_str:
            if symbol >= "0" and symbol <= "9":
                clean += symbol
        return clean.lstrip("0")
        
    def most_expensive(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their budgets. Sort it by budgets descendingly.
        """
        if self._correct_file_read:
            movie_dict = {
                movie[-1]: int(self.clean_budget(movie[2]))
                for movie in self.imdb_info
                if self.clean_budget(movie[2]) != ""
            }
            budgets = self.sort_dict_top_n(movie_dict, n)
            return budgets
        return None
        
    def most_profitable(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the difference between cumulative worldwide gross and budget.
        Sort it by the difference descendingly.
        """
        if self._correct_file_read:
            movie_dict = {
                movie[-1]: (
                    int(self.clean_budget(movie[3])) - int(self.clean_budget(movie[2]))
                )
                for movie in self.imdb_info
                if self.clean_budget(movie[2]) != "" and self.clean_budget(movie[3]) != ""
            }
            profits = self.sort_dict_top_n(movie_dict, n)
            return profits
        return None
    
    @staticmethod
    def clean_time(time_str):
        time_arr = time_str.split()
        hour_to_min = int(time_arr[0]) * 60
        total_min = hour_to_min + int(time_arr[2])
        return total_min
        
    def longest(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are their runtime. If there are more than one version – choose any.
        Sort it by runtime descendingly.
        """
        if self._correct_file_read:
            movie_dict = {
                movie[-1]: f"{self.clean_time(movie[4])} min" for movie in self.imdb_info
            }
            runtimes = self.sort_dict_top_n(movie_dict, n)
            return runtimes
        return None

        
    def top_cost_per_minute(self, n):
        """
        The method returns a dict with top-n movies where the keys are movie titles and
        the values are the budgets divided by their runtime. The budgets can be in different currencies – do not pay attention to it. 
        The values should be rounded to 2 decimals. Sort it by the division descendingly.
        """
        if self._correct_file_read:
            movie_dict = {
                movie[-1]: round(
                    (int(self.clean_budget(movie[2])) / int(self.clean_time(movie[4]))), 2
                )
                for movie in self.imdb_info
                if self.clean_budget(movie[2]) != ""
            }
            costs = self.sort_dict_top_n(movie_dict, n)
            return costs
        return None

class Test:

    @pytest.fixture()
    def links(self):
        return Links('dataset/links.csv')
    
    @pytest.fixture()
    def movies(self):
        return Movies('dataset/movies.csv')
    
    @pytest.fixture()
    def tags(self):
        return Tags('dataset/tags.csv')
    
    @pytest.fixture()
    def ratings(self):
        return Ratings('dataset/ratings.csv')
    
    @pytest.fixture()
    def links_fail(self):
        return Links('Hello, i\'m Data Scientist!')
    
    @pytest.fixture()
    def movies_fail(self):
        return Movies('Hello, i\'m Data Scientist!')
    
    @pytest.fixture()
    def tags_fail(self):
        return Tags('Hello, i\'m Data Scientist!')
    
    @pytest.fixture()
    def ratings_fail(self):
        return Ratings('Hello, i\'m Data Scientist!')
    
    def test_dist_by_release(self, movies):
        result = movies.dist_by_release()
        assert isinstance(result, OrderedDict)
        assert list(result.items()) == sorted(result.items(), reverse=True, key=lambda x: x[1])
        for key, value in result.items():
            assert isinstance(key, int)
            assert isinstance(value, int)

    def test_dist_by_release_fail(self, movies_fail):
        result = movies_fail.dist_by_release()
        assert result is None

    def test_dist_by_genres(self, movies):
        result = movies.dist_by_genres()
        assert isinstance(result, OrderedDict)
        assert list(result.items()) == sorted(result.items(), reverse=True, key=lambda x: x[1])
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_dist_by_genres_fail(self, movies_fail):
        result = movies_fail.dist_by_genres()
        assert result is None

    def test_most_genres(self, movies):
        result = movies.most_genres(500)
        assert isinstance(result, OrderedDict)
        assert list(result.items()) == sorted(result.items(), reverse=True, key=lambda x: x[1])
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_most_genres_fail(self, movies_fail):
        result = movies_fail.most_genres(500)
        assert result is None

    def test_dist_by_year(self, ratings):
        result = ratings.movies.dist_by_year()
        assert isinstance(result, list)
        assert result == sorted(result, key=lambda x: x[0], reverse=False)
        for key, value in result:
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_dist_by_year_fail(self, ratings_fail):
        result = ratings_fail.movies.dist_by_year()
        assert result is None

    def test_dist_by_rating(self, ratings):
        result = ratings.movies.dist_by_rating()
        assert isinstance(result, list)
        assert result == sorted(result, key=lambda x: x[0], reverse=False)
        for key, value in result:
            assert isinstance(key, float)
            assert isinstance(value, int)

    def test_dist_by_rating_fail(self, ratings_fail):
        result = ratings_fail.movies.dist_by_rating()
        assert result is None
    
    def test_top_by_num_of_ratings(self, ratings):
        result = ratings.movies.top_by_num_of_ratings(500)
        assert isinstance(result, OrderedDict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_top_by_num_of_ratings_fail(self, ratings_fail):
        result = ratings_fail.movies.top_by_num_of_ratings(500)
        assert result is None
    
    def test_top_by_ratings(self, ratings):
        result = ratings.movies.top_by_ratings(500)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, float)

    def test_top_by_ratings_fail(self, ratings_fail):
        result = ratings_fail.movies.top_by_ratings(500)
        assert result is None

    def test_top_controversial(self, ratings):
        result = ratings.movies.top_controversial(500)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, float)

    def test_top_controversial_fail(self, ratings_fail):
        result = ratings_fail.movies.top_controversial(500)
        assert result is None

    def test_get_count_user_rating_distribution(self, ratings):
        result = ratings.users.get_count_user_rating_distribution()
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_get_count_user_rating_distribution_fail(self, ratings_fail):
        result = ratings_fail.users.get_count_user_rating_distribution()
        assert result is None

    def test_user_top_by_ratings(self, ratings):
        result = ratings.users.user_top_by_ratings()
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, float)

    def test_user_top_by_ratings_fail(self, ratings_fail):
        result = ratings_fail.users.user_top_by_ratings()
        assert result is None

    def test_top_user_controversial(self, ratings):
        result = ratings.users.top_user_controversial(500)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, float)

    def test_top_user_controversial_fail(self, ratings_fail):
        result = ratings_fail.users.top_user_controversial(500)
        assert result is None

    def test_most_words(self, tags):
        result = tags.most_words(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_longest_tags(self, tags):
        result = tags.longest(100)
        assert isinstance(result, list)
        assert result == sorted(result, key=lambda x: len(x), reverse=True)
        for tag in result:
            assert isinstance(tag, tuple)
            assert isinstance(tag[0], str)
            assert isinstance(tag[1], int)

    def test_most_words_and_longest(self, tags):
        result = tags.most_words_and_longest(100)
        assert isinstance(result, list)
        for tag in result:
            assert isinstance(tag, str)
    
    def test_most_popular(self, tags):
        result = tags.most_popular(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)
    
    def test_tags_with(self, tags):
        result = tags.tags_with('the')
        assert isinstance(result, list)
        assert result == sorted(result)
        for tag in result:
            assert isinstance(tag, str)

    def test_get_imdb(self, links):
        result = links.get_imdb({1: '0114709'}, ["Director", "Budget", "Gross worldwide", "Runtime", "Stars", "Title"])
        assert isinstance(result, list)
        for movie in result:
            assert isinstance(movie, list)
            assert len(movie) == 7
            assert isinstance(movie[0], str)
            assert isinstance(movie[1], str)
            assert isinstance(movie[2], str)
            assert isinstance(movie[3], str)
            assert isinstance(movie[4], str)
            assert isinstance(movie[5], str)
            assert isinstance(movie[6], str)
    
    def test_longest_links(self, links):
        result = links.longest(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, str)

    def test_top_directors(self, links):
        result = links.top_directors(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_most_expensive(self, links):
        result = links.most_expensive(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_most_profitable(self, links):
        result = links.most_profitable(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, int)

    def test_longest(self, links):
        result = links.longest(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, str)

    def test_cost_per_minute(self, links):
        result = links.top_cost_per_minute(100)
        assert isinstance(result, dict)
        assert list(result.items()) == sorted(result.items(), key=lambda x: x[1], reverse=True)
        for key, value in result.items():
            assert isinstance(key, str)
            assert isinstance(value, float)
