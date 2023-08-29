# Modules
import psycopg2
import sys

# Connecting To Server
connection = psycopg2.connect(
    database="postgres",
    user=f"{sys.argv[2]}",
    password=f"{sys.argv[3]}",
    host="127.0.0.1",
    port="5432",
)

# Autocommit Changes & Create Cursor For Command Execution
connection.autocommit = True
cursor = connection.cursor()

# DB Name Check
db_check = sys.argv[1]

# Check if DB Already Exists
cursor.execute("SELECT datname FROM pg_database WHERE datname = %s", (db_check,))
database_exists = cursor.fetchone()

if database_exists:
    # Drop The Database
    cursor.execute("DROP DATABASE IF EXISTS %s", (db_check,))
    print(f"Database {db_check} dropped.")

# Database Creation PSQL Command
sql_database_create = f"""CREATE DATABASE {sys.argv[1]}"""
cursor.execute(sql_database_create)

# Output Create Message
print(f"'{sys.argv[1]}' Database Created")

# Connecting To Server
connection = psycopg2.connect(
    database=db_check,
    user=f"{sys.argv[2]}",
    password=f"{sys.argv[3]}",
    host="127.0.0.1",
    port="5432",
)

# Autocommit Changes & Create Cursor For Command Execution
connection.autocommit = True
cursor = connection.cursor()

# Create Necessary Tables

# Asset
sql_asset_table = """CREATE TABLE asset(
      id INT,
      tfit_id INT,
      name CHAR,
      active BOOLEAN,
      max_allowable_temp INT,
      min_allowable_temp INT  
    )"""

cursor.execute(sql_asset_table)
print("Asset Table Created")

# Capacity
sql_capacity_table = """CREATE TABLE capacity(
      id BIGINT,
      asset_id INT,
      time TIMESTAMP WITH TIME ZONE,
      capacity DOUBLE PRECISION
    )"""

cursor.execute(sql_capacity_table)
print("Capacity Table Created")

# Fiber
sql_fiber_table = """CREATE TABLE fiber(
      id INT,
      name CHARACTER VARYING,
      asset_id INT,
      start DOUBLE PRECISION,
      "end" DOUBLE PRECISION,
      max_allowable_temp DOUBLE PRECISION,
      min_allowable_temp DOUBLE PRECISION  
    )"""

cursor.execute(sql_fiber_table)
print("Fiber Table Created")

# Load
sql_load_table = """CREATE TABLE load(
      id BIGINT,
      asset_id INT,
      time TIMESTAMP WITH TIME ZONE,
      load DOUBLE PRECISION 
    )"""

cursor.execute(sql_load_table)
print("Load Table Created")

# Location
sql_location_table = """CREATE TABLE location(
      id INT,
      name CHARACTER VARYING,
      coordinates NUMERIC,
      region CHARACTER VARYING
    )"""

cursor.execute(sql_location_table)
print("Location Table Created  ")

# Notifications
sql_notifications_table = """CREATE TABLE notifications(
      id INT,
      asset_id INT,
      fiber_id INT,
      time TIMESTAMP WITH TIME ZONE,
      message TEXT,
      alert_level CHARACTER VARYING,  
      action CHARACTER VARYING
    )"""

cursor.execute(sql_notifications_table)
print("Notifications Table Created  ")

# Status
sql_status_table = """CREATE TABLE status(
      id BIGINT,
      tfit_id INT,
      active BOOLEAN,
      message TEXT,
      time TIMESTAMP WITH TIME ZONE
    )"""

cursor.execute(sql_status_table)
print("Status Table Created  ")

# Temperature
sql_temperature_table = """CREATE TABLE temperature(
      id INT,
      time TIMESTAMP WITH TIME ZONE,
      fiber_id INT,
      max DOUBLE PRECISION,
      min DOUBLE PRECISION,
      avg DOUBLE PRECISION
      
    )"""

cursor.execute(sql_temperature_table)
print("Temperature Table Created  ")

# Tfit
sql_tfit_table = """CREATE TABLE tfit(
      id INT,
      name CHARACTER VARYING,
      location_id INT,
      sensor_data_table CHARACTER VARYING,
      sensor_settings_table CHARACTER VARYING,
      sensor_diagnostics_table CHARACTER VARYING
    )"""

cursor.execute(sql_tfit_table)
print("Tfit Table Created  ")

# 3D Model
sql_3d_table = """CREATE TABLE three_d_model(
      id INT,
      asset_id INT,
      fibers CHARACTER VARYING,
      accessories CHARACTER VARYING,
      scale DOUBLE PRECISION
    )"""

cursor.execute(sql_3d_table)
print("3DModel Table Created  ")

# 2D Model
sql_2d_table = """CREATE TABLE two_d_model(
      id INT,
      asset_id INT,
      svg_path CHARACTER VARYING,
      z_index INT,
      fiber_id INT
    )"""

cursor.execute(sql_2d_table)
print("2DModel Table Created  ")

# Relations Between Tables


# Sensor Table Inclusion (w/ Parameters)


# Close Connection To Server
connection.close()
