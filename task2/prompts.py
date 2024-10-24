def get_population_prompt(country_data):
    population_in_millions = country_data['population'] / 1_000_000 if 'population' in country_data and country_data['population'] else 0
    pop_density = country_data.get('pop_density', 'N/A')
    sex_ratio = country_data.get('sex_ratio', 'N/A')
    
    prompt = """
    Provide a detailed analysis of the population for {name}. 
    The population is {population_in_millions} million. 
    The population density is {pop_density} people per square kilometer. 
    The sex ratio is {sex_ratio}. 
    Only include the parameters mentioned and do not predict any further details.
    """.format(
        name=country_data['name'],
        population_in_millions=population_in_millions,
        pop_density=pop_density,
        sex_ratio=sex_ratio
    )
    return prompt

def get_tourists_prompt(country_data):
    tourists_in_millions = country_data['tourists'] / 1_000_000 if 'tourists' in country_data and country_data['tourists'] else 0
    
    prompt = """
    Generate a summary for the tourism sector in {name}.
    The country has welcomed {tourists_in_millions} million tourists. 
    Only provide the details of the data that are mentioned as parameters and do not predict any additional information.
    """.format(
        name=country_data['name'],
        tourists_in_millions=tourists_in_millions
    )
    return prompt

def get_import_export_prompt(country_data):
    imports_in_millions = country_data['imports'] / 1_000_000 if 'imports' in country_data and country_data['imports'] else 0
    exports_in_millions = country_data['exports'] / 1_000_000 if 'exports' in country_data and country_data['exports'] else 0

    prompt = """
    Summarize the import-export data for {name}.
    The country imports goods worth {imports_in_millions} million and exports goods worth {exports_in_millions} million. 
    Only include the provided parameters and do not predict anything beyond the given data.
    """.format(
        name=country_data['name'],
        imports_in_millions=imports_in_millions,
        exports_in_millions=exports_in_millions
    )
    return prompt
