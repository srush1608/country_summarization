from database import get_db_connection

def generate_summary(parameter, country_name):
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        try:
            # Fetch relevant data for the summary
            select_query = """
                SELECT name, gdp, population, tourists, currency, surface_area, imports, exports, pop_density, sex_ratio, gdp_growth 
                FROM extended_country_details WHERE name = %s
            """
            cursor.execute(select_query, (country_name,))
            row = cursor.fetchone()

            if row:
                gdp_in_millions = row[1] / 1_000_000 if row[1] else 0
                population_in_millions = row[2] / 1_000_000 if row[2] else 0
                tourists_in_millions = row[3] / 1_000_000 if row[3] else 0
                imports_in_millions = row[6] / 1_000_000 if row[6] else 0
                exports_in_millions = row[7] / 1_000_000 if row[7] else 0
                
                if parameter == "population":
                    summary = f"The population of {row[0]} is approximately {population_in_millions:.2f} million with a density of {row[8]} people per sq km."
                elif parameter == "tourists":
                    summary = f"{row[0]} attracts around {tourists_in_millions:.2f} million tourists annually."
                elif parameter == "import_export":
                    summary = f"{row[0]} has imports valued at approximately {imports_in_millions:.2f} million USD and exports estimated at {exports_in_millions:.2f} million USD."
                else:
                    summary = "Invalid parameter for summary."

                # Including additional information in summary
                summary += f" The GDP of {row[0]} is approximately {gdp_in_millions:.2f} million USD and the currency is {row[4]}."

                return {'status': 'success', 'summary': summary}
            else:
                return {'status': 'error', 'message': 'Country not found in database'}

        except Exception as e:
            return {'status': 'error', 'message': str(e)}
        finally:
            cursor.close()
            connection.close()
    else:
        return {'status': 'error', 'message': 'Database connection failed'}
