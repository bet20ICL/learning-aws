from pprint import pprint
import boto3
from boto3.dynamodb.conditions import Key, Attr

def title_by_year(year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression = Key('year').eq(year)
    )
    return response['Items']

def practice1():
    query_year = 1994
    print(f"Get movies from {query_year}")
    movies = title_by_year(query_year)
    for movie in movies:
        # print(f"\n{movie['year']} : {movie['title']}")
        print(movie['info']['actors'])
        print('\n')

def get_movie(title, year, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('Movies')
    response = table.query(
        KeyConditionExpression = Key('year').eq(year) & Key('title').eq(title)
    )
    return response['Items']

def p2():
    title = 'After Hours'
    year = 1985
    print(f'{title}, {year} info:')
    movie = get_movie(title, year)
    pprint(movie)

def movie_before(year, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('Movies')
    
    response = table.scan(FilterExpression=Key('year').gt(year))
    data = response['Items']
    display_movies(data)

    count = 0
    while 'LastEvaluatedKey' in response:
        response = table.scan(FilterExpression=Key('year').gt(year))
        display_movies(response['Items'])
        data.extend(response['Items'])
        print(f"Iteration {count}")
        count += 1
    return data

def print_movies(movies):
    for movie in movies:
        print(f"\n{movie['year']} : {movie['title']}") 

def p3():
    year = 2000
    print(f'All movies before {year}:')
    movies = movie_before(year, print_movies)

def scan_actor(actor, display_movies, dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
    
    table = dynamodb.Table('Movies')
    response = table.scan(
        ExpressionAttributeValues={":a" : actor},
        FilterExpression = ":a = info.actors[0]"
    )
    data = response['Items']
    display_movies(data)

    # while 'LastEvaluatedKey' in response:
    #     response = table.scan(
    #         FilterExpression = actor IN :act,
    #         ExpressionAttributeNames={":act": actors}
    #     )
    #     display_movies(response['Items'])
    #     data.extend(response['Items'])
        
    return data

def p4():
    actor = "Tom Hanks"
    print(f"All Movies starring {actor}")
    movies = scan_actor(actor, print_movies)



if __name__ == '__main__':
    practice1()
