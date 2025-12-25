from openai import AzureOpenAI, DefaultHttpxClient

client = AzureOpenAI(
    api_key="abcdefg",
    api_version="2024-02-01",
    azure_endpoint = "https://cour-external-playground.openai.azure.com/",
    http_client=DefaultHttpxClient(verify=False)
    )

# +

# ### If you want to use your own OpenAI key, uncomment these cells below and comment out the other get_llm_response function cells:

# from openai import OpenAI

# ### Add your key as a string
# openai_api_key = "Add your key in here"

# # Set up the OpenAI client
# client = OpenAI(api_key=openai_api_key)

# def get_llm_response(prompt):
#     """This function takes as input a prompt, which must be a string enclosed in quotation marks,
#     and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
#     a string.
#     """
#     try:
#         if not isinstance(prompt, str):
#             raise ValueError("Input must be a string enclosed in quotes.")
#         completion = client.chat.completions.create(
#             model="gpt-3.5-turbo-0125",
#             messages=[
#                 {
#                     "role": "system",
#                     "content": "You are a helpful but terse AI assistant who gets straight to the point.",
#                 },
#                 {"role": "user", "content": prompt},
#             ],
#             temperature=0.0,
#         )
#         response = completion.choices[0].message.content
#         return response
#     except TypeError as e:
#         print("Error:", str(e))

# -

def get_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then saves the response of the model as
    a string.
    """
    try:
        if not isinstance(prompt, str):
            raise ValueError("Input must be a string enclosed in quotes.")
        completion = client.chat.completions.create(
            model="gpt-35-turbo",
            messages = [
                {
                    "role": "system",
                    "content": "You are a helpful but terse AI assistant who gets straight to the point.",
                },
                {"role": "user", "content": prompt},
            ],
            temperature=0.0,
        )
        response = completion.choices[0].message.content
        return response
    except TypeError as e:
        print("Error:", str(e))

def print_llm_response(prompt):
    """This function takes as input a prompt, which must be a string enclosed in quotation marks,
    and passes it to OpenAI's GPT3.5 model. The function then prints the response of the model.
    """
    llm_response = get_llm_response(prompt)
    print(llm_response)
