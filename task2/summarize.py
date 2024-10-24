from flask import Flask, jsonify, request
from groq import Groq
from database import get_db_connection
from prompts import get_population_prompt, get_tourists_prompt, get_import_export_prompt
import os

app = Flask(__name__) 
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=GROQ_API_KEY)

def generate_summary(prompt):
    try:
        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            temperature=0,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "Unable to generate summary"

@app.route('/generate-summary/<string:parameter>', methods=['GET'])
def generate_summary_route(parameter):
    country_name = request.args.get('name')  
    if not country_name:
        return jsonify({'error': 'Country name is required'}), 400

    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        query = """
        SELECT name, population, tourists, imports, exports, pop_density, gdp_growth, sex_ratio, literacy_rate 
        FROM extended_country_details 
        WHERE name = %s;
        """
        cursor.execute(query, (country_name,))
        rows = cursor.fetchall()

        if rows:
            country_data = {
                'name': rows[0][0],
                'population': rows[0][1] if rows[0][1] is not None else None,
                'tourists': rows[0][2] if rows[0][2] is not None else None,
                'imports': rows[0][3] if rows[0][3] is not None else None,
                'exports': rows[0][4] if rows[0][4] is not None else None,
                'pop_density': rows[0][5] if rows[0][5] is not None else None,
                'gdp_growth': rows[0][6] if len(rows[0]) > 6 and rows[0][6] is not None else None,
                'sex_ratio': rows[0][7] if len(rows[0]) > 7 and rows[0][7] is not None else None,
                'literacy_rate': rows[0][8] if len(rows[0]) > 8 and rows[0][8] is not None else None
            }

            if parameter == 'population':
                prompt = get_population_prompt(country_data)
            elif parameter == 'tourists':
                prompt = get_tourists_prompt(country_data)
            elif parameter == 'import_export':
                prompt = get_import_export_prompt(country_data)
            else:
                return jsonify({'error': 'Invalid parameter'}), 400

            summary = generate_summary(prompt)
            return jsonify({'summary': summary}), 200
        else:
            return jsonify({'message': 'No data available for the specified country.'}), 404
    else:
        return jsonify({'error': 'Database connection error'}), 500

if __name__ == '__main__':
    app.run(debug=True)
