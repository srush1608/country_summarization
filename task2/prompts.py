def get_population_prompt(country_data):
    prompt = """
    Provide a detailed analysis of the population for {name}. 
    The population is {population}. 
    The population density is {pop_density} people per square kilometer. 
    The sex ratio is {sex_ratio}. 
    Please give an overall view of the population situation in {name}.
    """.format(**country_data)
    return prompt

def get_tourists_prompt(country_data):
    prompt = """
    Generate a summary for the tourism sector in {name}.
    The country has welcomed {tourists} tourists. Analyze how tourism impacts the GDP, and how it contributes to the country's economy.
    Include any known challenges or growth trends in the tourism sector of {name}. Only provide the details of the data that are mentioned as parameters
    """.format(**country_data)
    return prompt

def get_import_export_prompt(country_data):
    prompt = """
    Summarize the import-export data for {name}.
    The country imports goods worth {imports} and exports goods worth {exports}. Discuss the trade balance and how it affects the economic stability of {name}.
    Include information on major trading partners if available.
    """.format(**country_data)
    return prompt
















# def get_population_prompt(data):
#     return """Provide detailed population-related data and analysis for {data['name']} including the population size and density."""

# def get_tourists_prompt(data):
#     return """Summarize the tourist data for {data['name']} including the number of tourists and its impact on the country."""

# def get_import_export_prompt(data):
#     return """Analyze the trade situation in {data['name']} by describing the imports, exports, and balance of trade."""
