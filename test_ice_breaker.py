import os
from typing import Tuple
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from chains.custom_chains import (
    get_summary_chain,
    get_interests_chain,
    get_ice_breaker_chain,
)

from third_parties.linkedin import scrape_linkedin_profile
from agents.linkedin_lookup_agent import linkedin_lookup
from dotenv import load_dotenv
from output_parsers import Summary, IceBreaker, TopicOfInterest
from langchain_core.output_parsers import PydanticOutputParser
import openai
from langsmith import wrappers, traceable

# Auto-trace LLM calls in-context
client = wrappers.wrap_openai(openai.Client())


@traceable
def ice_break_with(name: str) -> Tuple[Summary, str]:
    linkedin_username = linkedin_lookup(name=name)
    linkedin_data = scrape_linkedin_profile(
        linkedin_profile_url=linkedin_username, mock=True
    )

    summary_chain = get_summary_chain()
    summary_and_facts: Summary = summary_chain.invoke(
        input={"information": linkedin_data},
    )

    interests_chain = get_interests_chain()
    interests: TopicOfInterest = interests_chain.invoke(
        input={"information": linkedin_data}
    )

    ice_breaker_chain = get_ice_breaker_chain()
    ice_breakers: IceBreaker = ice_breaker_chain.invoke(
        input={"information": linkedin_data}
    )

    return (
        summary_and_facts,
        interests,
        ice_breakers,
        linkedin_data.get("photoUrl"),
    )


if __name__ == "__main__":
    ice_break_with(name="Jose Angel Gonzalez Barba")
