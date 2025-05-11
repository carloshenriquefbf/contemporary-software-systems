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

def get_google_results():
    websites_to_exclude = [
        'youtube.com', 'github.com', 'paperswithcode.com'
    ]

    for pop in population:
        query = f"{intervention_query} \"{pop}\" after:2021"
        for website in websites_to_exclude:
            query += " " + exclude_website(website)

        print("query:", query)
        search_results = google_search(query, API_KEY, CSE_ID, num_results=10)
        if not search_results:
            print("No results found for this query.")
            continue
        pop_df = pd.DataFrame(search_results)

        pop_df.to_csv(f"./google_results/google_results_{pop}.csv", index=False)
        print(f"Results for {pop} saved to google_results_{pop}.csv")
        print("==================")

def get_github_results():
    for pop in population:
        query = f"{intervention_query} \"{pop}\" after:2021"

        query += " " + include_website("github.com")

        print("query:", query)
        search_results = google_search(query, API_KEY, CSE_ID, num_results=10)
        if not search_results:
            print("No results found for this query.")
            continue
        pop_df = pd.DataFrame(search_results)

        pop_df.to_csv(f"./github_results/github_results_{pop}.csv", index=False)
        print(f"Results for {pop} saved to github_results_{pop}.csv")
        print("==================")

def get_pwc_results():
    for pop in population:
        query = f"{intervention_query} \"{pop}\" after:2021"

        query += " " + include_website("paperswithcode.com")

        print("query:", query)
        search_results = google_search(query, API_KEY, CSE_ID, num_results=10)
        if not search_results:
            print("No results found for this query.")
            continue
        pop_df = pd.DataFrame(search_results)

        pop_df.to_csv(f"./pwc_results/pwc_results_{pop}.csv", index=False)
        print(f"Results for {pop} saved to pwc_results_{pop}.csv")
        print("==================")

def merge_dataframes_in_directory(directory):
    all_dataframes = []
    for filename in os.listdir(directory):
        if filename.endswith('.csv'):
            filepath = os.path.join(directory, filename)
            df = pd.read_csv(filepath)
            all_dataframes.append(df)
    merged_df = pd.concat(all_dataframes, ignore_index=True)
    return merged_df

if __name__ == "__main__":
    os.makedirs('./google_results', exist_ok=True)
    os.makedirs('./github_results', exist_ok=True)
    os.makedirs('./pwc_results', exist_ok=True)
    os.makedirs('./final_results', exist_ok=True)

    get_google_results()
    get_github_results()
    get_pwc_results()

    google_df = merge_dataframes_in_directory('./google_results')
    github_df = merge_dataframes_in_directory('./github_results')
    pwc_df = merge_dataframes_in_directory('./pwc_results')

    google_df.to_csv('./final_results/merged_google_results.csv', index=False)
    github_df.to_csv('./final_results/merged_github_results.csv', index=False)
    pwc_df.to_csv('./final_results/merged_pwc_results.csv', index=False)
