import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
CSE_ID = os.getenv('CSE_ID')

def exclude_website(website):
    return f"-site:{website}"

def include_website(website):
    return f"site:{website}"

def google_search(query, api_key, cse_id, num_results):
    results = []
    for start in range(1, num_results + 1, 10):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': api_key,
            'cx': cse_id,
            'q': query,
            'start': start
        }
        response = requests.get(url, params=params)
        data = response.json()

        if 'items' not in data:
            print("No items found.")
            break

        for item in data['items']:
            results.append({
                'title': item.get('title'),
                'link': item.get('link'),
                'snippet': item.get('snippet'),
                'displayLink': item.get('displayLink')
            })

    return results

population = [
    'test',
    'quality',
    'validation',
    'verification',
    'technical debt',
    'defect detection',
    'software inspection',
    'model checking',
    'debugging',
    'code review'
]

intervention_query = """
    Generative AI OR Generative Artificial Intelligence OR Generative Model OR Large Language Model
    OR Language Model OR Small Language Model OR LLM OR RAG OR Retrieval Augmented Generation
    OR Natural Language Processing OR NLP OR AI Agent OR AI Multi-Agent
    """

websites_to_exclude = [
    'youtube.com', 'github.com', 'paperswithcode.com'
]

websites_to_include = [
    # 'github.com'
    # 'paperswithcode.com',
]

df = pd.DataFrame()

for pop in population:
    query = f"{intervention_query} \"{pop}\" after:2021"
    for website in websites_to_exclude:
        query += " " + exclude_website(website)

    for website in websites_to_include:
        query += " " + include_website(website)

    print("query:", query)
    search_results = google_search(query, API_KEY, CSE_ID, num_results=10)

    pop_df = pd.DataFrame(search_results)

    pop_df.to_csv(f"./individual_results/google_results_{pop}.csv", index=False)
    print(f"Results for {pop} saved to google_results_{pop}.csv")
    print("==================")
    df = pd.concat([df, pop_df], ignore_index=True)

df.to_csv("google_results.csv", index=False)
print("Results saved to google_results.csv")

