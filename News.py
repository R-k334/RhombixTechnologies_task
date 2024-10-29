import requests

def news():
    api_key = 'cfbd0ceb0c45450588547e8f695eec0d'  # Using your NewsAPI key
    url = f'https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}'
    
    try:
        response = requests.get(url)
        news_data = response.json()
        
        if news_data['status'] == 'ok':
            headlines = [article['title'] for article in news_data['articles'][:5]]  # Limit to 5 articles
            return headlines
        else:
            return ["No news found at the moment."]
    
    except Exception as e:
        print("An error occurred while fetching the news:", e)
        return ["Unable to retrieve news at the moment."]
