from flask import Flask, request
from summarize import generate_summary_route
from country import fetch_and_store_country

app = Flask(__name__)

@app.route('/fetch-country', methods=['GET'])
def fetch_country():
    return fetch_and_store_country()

@app.route('/generate-summary/<string:parameter>', methods=['GET'])
def summary(parameter):
    return generate_summary_route(parameter)

if __name__ == '__main__':
    app.run(debug=True)





# all complete code in one file

# # import os
# # from flask import Flask, jsonify
# # import psycopg2
# # import requests
# # from groq import Groq
# # from dotenv import load_dotenv

# # load_dotenv()

# # app = Flask(__name__)

# # DB_NAME = os.getenv("DB_NAME")
# # DB_USER = os.getenv("DB_USER")
# # DB_PASS = os.getenv("DB_PASS")
# # DB_HOST = os.getenv("DB_HOST")
# # DB_PORT = os.getenv("DB_PORT")

# # API_KEY = os.getenv("API_KEY")
# # GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# # client = Groq(api_key=GROQ_API_KEY)

# # def fetch_country_data(country_name):
# #     try:
# #         api_url = f"https://api.api-ninjas.com/v1/country?name={country_name}"
# #         headers = {'X-Api-Key': API_KEY}
# #         response = requests.get(api_url, headers=headers)

# #         if response.status_code == 200:
# #             data = response.json()
# #             if data:
# #                 country_data = {
# #                     'name': data[0]['name'],
# #                     'gdp': data[0].get('gdp', 0),
# #                     'population': data[0]['population'],
# #                     'literacy_rate': data[0].get('literacy', 0),
# #                     'tourists': data[0].get('tourists', 0),
# #                     'currency': data[0]['currency']['code'],
# #                     'surface_area': data[0].get('surface_area', 0),
# #                     'pop_growth': data[0].get('pop_growth', 0),
# #                     'pop_density': data[0].get('pop_density', 0),
# #                     'trade': data[0].get('trade', 0),
# #                     'imports': data[0].get('imports', 0),
# #                     'exports': data[0].get('exports', 0),
# #                     'sex_ratio': data[0].get('sex_ratio', 0),
# #                     'gdp_growth': data[0].get('gdp_growth', 0)
# #                 }
# #                 return country_data
# #             else:
# #                 print("No data found for the country.")
# #                 return None
# #         else:
# #             print(f"Error fetching data: {response.status_code}, {response.text}")
# #             return None
# #     except Exception as e:
# #         print(f"Exception occurred: {e}")
# #         return None

# # def store_country_data(country_data):
# #     try:
# #         connection = psycopg2.connect(
# #             dbname=DB_NAME,
# #             user=DB_USER,
# #             password=DB_PASS,
# #             host=DB_HOST,
# #             port=DB_PORT
# #         )
# #         cursor = connection.cursor()

# #         # Check if table exists, if not, create it
# #         create_table_query = """
# #             CREATE TABLE IF NOT EXISTS extended_country_details (
# #                 id SERIAL PRIMARY KEY,
# #                 name VARCHAR(255),
# #                 gdp FLOAT,
# #                 population FLOAT,
# #                 literacy_rate FLOAT,
# #                 currency VARCHAR(50),
# #                 surface_area FLOAT,
# #                 pop_growth FLOAT,
# #                 pop_density FLOAT,
# #                 trade FLOAT,
# #                 imports FLOAT,
# #                 exports FLOAT,
# #                 sex_ratio FLOAT,
# #                 gdp_growth FLOAT,
# #                 tourists FLOAT
# #             );
# #         """
# #         cursor.execute(create_table_query)

# #         insert_query = """
# #             INSERT INTO extended_country_details (
# #                 name, gdp, population, literacy_rate, currency, surface_area, pop_growth, 
# #                 pop_density, trade, imports, exports, sex_ratio, gdp_growth, tourists
# #             ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
# #         """
# #         cursor.execute(insert_query, (
# #             country_data['name'], country_data['gdp'], country_data['population'],
# #             country_data['literacy_rate'], country_data['currency'], country_data['surface_area'],
# #             country_data['pop_growth'], country_data['pop_density'], country_data['trade'],
# #             country_data['imports'], country_data['exports'], country_data['sex_ratio'],
# #             country_data['gdp_growth'], country_data['tourists']
# #         ))
# #         connection.commit()
# #         cursor.close()
# #         connection.close()
# #         print("Data stored successfully")
# #     except Exception as error:
# #         print("Error while storing data:", error)

# # def generate_summary(data):
# #     prompt = """You are an expert in giving summaries. Summarize the country data in a detailed paragraph, remove symbols: {data}."""
# #     try:
# #         completion = client.chat.completions.create(
# #             model="llama3-8b-8192",
# #             messages=[{"role": "user", "content": prompt}],
# #             temperature=1,
# #             max_tokens=1024,
# #             top_p=1,
# #             stream=False,
# #             stop=None,
# #         )
# #         summary = completion.choices[0].message.content
# #         return summary
# #     except Exception as e:
# #         print(f"Error during summarization: {e}")
# #         return "Unable to generate summary"

# # @app.route('/fetch-country/<string:country_name>', methods=['GET'])
# # def fetch_and_store_country(country_name):
# #     country_data = fetch_country_data(country_name)
# #     if country_data:
# #         store_country_data(country_data)
# #         return jsonify({'message': f"Data for {country_name} fetched and stored successfully.", 'data': country_data}), 200
# #     else:
# #         return jsonify({'error': 'Failed to fetch country data'}), 500

# # @app.route('/countries', methods=['GET'])
# # def get_countries_summary():
# #     try:
# #         connection = psycopg2.connect(
# #             dbname=DB_NAME,
# #             user=DB_USER,
# #             password=DB_PASS,
# #             host=DB_HOST,
# #             port=DB_PORT
# #         )
# #         cursor = connection.cursor()

# #         query = """
# #             SELECT name, gdp, population, literacy_rate, currency, surface_area, 
# #                    pop_growth, pop_density, trade, imports, exports, sex_ratio, 
# #                    gdp_growth, tourists 
# #             FROM extended_country_details;
# #         """
# #         cursor.execute(query)
# #         rows = cursor.fetchall()

# #         result = []
# #         for row in rows:
# #             country_data = {
# #                 'name': row[0],
# #                 'gdp': row[1],
# #                 'population': row[2],
# #                 'literacy_rate': row[3],
# #                 'currency': row[4],
# #                 'surface_area': row[5],
# #                 'pop_growth': row[6],
# #                 'pop_density': row[7],
# #                 'trade': row[8],
# #                 'imports': row[9],
# #                 'exports': row[10],
# #                 'sex_ratio': row[11],
# #                 'gdp_growth': row[12],
# #                 'tourists': row[13]
# #             }
# #             result.append(country_data)

# #         cursor.close()
# #         connection.close()
# #         return jsonify(result), 200

# #     except Exception as error:
# #         print("Error while fetching data:", error)
# #         return jsonify({'error': 'Unable to fetch data'}), 500

# # # API route to generate summary for all countries
# # @app.route('/generate-summary', methods=['GET'])
# # def generate_summary_route():
# #     try:
# #         connection = psycopg2.connect(
# #             dbname=DB_NAME,
# #             user=DB_USER,
# #             password=DB_PASS,
# #             host=DB_HOST,
# #             port=DB_PORT
# #         )
# #         cursor = connection.cursor()

# #         query = """
# #             SELECT name, gdp, population, literacy_rate, currency, surface_area, 
# #                    pop_growth, pop_density, trade, imports, exports, sex_ratio, 
# #                    gdp_growth, tourists 
# #             FROM extended_country_details;
# #         """
# #         cursor.execute(query)
# #         rows = cursor.fetchall()

# #         summary_data = []
# #         for row in rows:
# #             country_data = {
# #                 'name': row[0],
# #                 'gdp': row[1],
# #                 'population': row[2],
# #                 'literacy_rate': row[3],
# #                 'currency': row[4],
# #                 'surface_area': row[5]
# #             }
# #             summary_data.append(country_data)

# #         cursor.close()
# #         connection.close()

# #         if summary_data:
# #             summary = generate_summary(summary_data)
# #             return jsonify({'summary': summary}), 200
# #         else:
# #             return jsonify({'message': 'No data available for summarization.'}), 404

# #     except Exception as error:
# #         print("Error while generating summary:", error)
# #         return jsonify({'error': 'Unable to generate summary'}), 500

# # # Run the Flask app
# # if __name__ == '__main__':
# #     app.run(debug=True)
