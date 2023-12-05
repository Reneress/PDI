import requests

def search_bing(query):
    url = "https://www.bing.com/search"
    params = {'q': query}
    response = requests.get(url, params=params)
    return response.text

queries = ["Python", "Java", "C++", "JavaScript", "Ruby", "Swift", "Go", "Rust", "Kotlin", "TypeScript"]

for query in queries:
    result = search_bing(query)
    print(f"Resultados para {query}:\n{result}\n")
