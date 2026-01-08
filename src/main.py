import os
from openai import AzureOpenAI
from dotenv import load_dotenv  # Added dotenv import
from prompts import PROMPT_LIBRARY

# Load variables from the .env file
load_dotenv()

# Load credentials from Environment Variables (now populated by dotenv)
AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

# Initialize the Azure OpenAI Client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2024-02-01",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)


def get_customer_support_response(template_id, customer_query, product, issue, tone):
    """
    Part 2: Parameterized Usage
    Demonstrates variable injection into prompt templates.
    """

    # 1. Fetch template from prompts.py
    base_template = PROMPT_LIBRARY.get(template_id)

    if not base_template:
        print(f"Error: Template '{template_id}' not found in prompt library.")
        return

    # 2. Inject dynamic variables into the prompt
    final_prompt = base_template.format(
        customer_query=customer_query,
        product_name=product,
        issue_type=issue,
        tone=tone
    )

    # Part 3: Azure OpenAI API Call
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are an automated enterprise response component."},
                {"role": "user", "content": final_prompt}
            ],
            temperature=0.3
        )

        # Output per assignment requirements
        print(f"\n--- PROMPT SENT TO MODEL ---")
        print(final_prompt)
        print("\n--- ENTERPRISE AI RESPONSE ---")
        print(response.choices[0].message.content.strip())
        print("-" * 50)

    except Exception as e:
        print(f"An error occurred while calling the API: {e}")


if __name__ == "__main__":
    # Test Case: Billing Issue (Enterprise Context)
    get_customer_support_response(
        template_id="general_support",
        customer_query="I have been billed twice for my January subscription!",
        product="Enterprise Cloud Suite",
        issue="Billing",
        tone="formal"
    )

    get_customer_support_response(
        template_id="technical_support",
        customer_query="The login page keeps spinning and won't let me in.",
        product="Enterprise Portal",
        issue="Technical/Access",
        tone="friendly"
    )