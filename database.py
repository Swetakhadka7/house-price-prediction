import psycopg2
from datetime import datetime

DB_CONFIG = {
    'host': 'localhost',
    'database': 'house_predictions',
    'user': 'postgres',
    'password': 'admin',
    'port': '5432'
}

def get_connection():
    conn = psycopg2.connect(**DB_CONFIG)
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()
    create_sql = """
        CREATE TABLE IF NOT EXISTS predictions (
            id SERIAL PRIMARY KEY,
            overall_quality INTEGER,
            gr_liv_area INTEGER,
            garage_cars INTEGER,
            total_bsmt_sf INTEGER,
            full_bath INTEGER,
            year_built INTEGER,
            year_remod_add INTEGER,
            tot_rms_abv_grd INTEGER,
            fireplaces INTEGER,
            predicted_price FLOAT,
            prediction_date TIMESTAMP
        )
    """
    cursor.execute(create_sql)
    conn.commit()
    cursor.close()
    conn.close()
    print("Table created successfully")

def save_prediction(inputs, predicted_price):
    conn = get_connection()
    cursor = conn.cursor()
    insert_sql = """
        INSERT INTO predictions (
            overall_quality, gr_liv_area, garage_cars, total_bsmt_sf,
            full_bath, year_built, year_remod_add, tot_rms_abv_grd,
            fireplaces, predicted_price, prediction_date
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(insert_sql, (
        inputs['OverallQual'],
        inputs['GrLivArea'],
        inputs['GarageCars'],
        inputs['TotalBsmtSF'],
        inputs['FullBath'],
        inputs['YearBuilt'],
        inputs['YearRemodAdd'],
        inputs['TotRmsAbvGrd'],
        inputs['Fireplaces'],
        float(predicted_price),
        datetime.now()
    ))
    conn.commit()
    cursor.close()
    conn.close()
    print("Prediction saved successfully")

def get_all_predictions():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM predictions ORDER BY prediction_date DESC')
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

if __name__ == '__main__':
    create_table()