import os
import requests
from dotenv import load_dotenv

load_dotenv()

def scrape_linkedin_profile(linkedin_profile_url: str, mock: True = False) -> str:
    if mock:
        linkedin_profile_url="https://gist.githubusercontent.com/HalteroXHunter/322aacc094a00b68e989aed94acfbb62/raw/1353bbd4b1996ec4fc176461f8d4baeb88909be3/jose-angel-scraping.json"
        response = requests.get(linkedin_profile_url, timeout=10)

    else:
        api_endpoint = "https://api.scrapin.io/enrichment/profile"
        params = {
            "apikey": os.environ["SCRAPIN_API_KEY"],
            "linkedInUrl": linkedin_profile_url,
            }
        response = requests.get(api_endpoint, params=params, timeout=10)
    
    data = response.json().get("person")
    data = {
        k: v
        for k, v in data.items()
        if v not in ([],"","",None)
        and k not in ["certifications"]
    }

    return data

if __name__ == "__main__":
    print(
        scrape_linkedin_profile(
            linkedin_profile_url="https://www.linkedin.com/in/jos%C3%A9-%C3%A1ngel-gonz%C3%A1lez-barba/"
        )
    )