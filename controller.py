import sys
from flask import abort, jsonify  # Import jsonify for JSON responses
import pymysql
from dbutils.pooled_db import PooledDB
from config import OPENAPI_STUB_DIR, DB_HOST, DB_USER, DB_PASSWD, DB_NAME

sys.path.append(OPENAPI_STUB_DIR)
from swagger_server import models  # Import correct models

pool = PooledDB(creator=pymysql,
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWD,
                database=DB_NAME,
                maxconnections=1,
                blocking=True)

def get_clothdryingintegrated():
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, sensor, source, value
            FROM clothesdryingintegrated
        """)
        result = [dict(zip([column[0] for column in cs.description], row)) for row in cs.fetchall()]
        return jsonify(result)  # Return JSON response

def get_clothdryingintegrated_by_id(id):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, sensor, source, value
            FROM clothesdryingintegrated
            WHERE id=%s
        """, [id])
        result = cs.fetchone()
    if result:
        return jsonify(result)  # Return JSON response
    else:
        abort(404)  # Return 404 Not Found


def get_clothdryingintegrated_by_sensor(sensor):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, sensor, source, value
            FROM clothesdryingintegrated
            WHERE sensor=%s
        """, [sensor])
        result = [dict(zip([column[0] for column in cs.description], row)) for row in cs.fetchall()]
        return jsonify(result)  # Return JSON response

def get_clothdryingintegrated_by_source(source):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, sensor, source, value
            FROM clothesdryingintegrated
            WHERE source=%s
        """, [source])
        result = [dict(zip([column[0] for column in cs.description], row)) for row in cs.fetchall()]
        return jsonify(result)  # Return JSON response

def get_clothdryingintegrated_by_sensor_and_source(sensor, source):
    with pool.connection() as conn, conn.cursor() as cs:
        cs.execute("""
            SELECT id, ts, lat, lon, sensor, source, value
            FROM clothesdryingintegrated
            WHERE sensor=%s AND source=%s
        """, [sensor, source])
        result = [dict(zip([column[0] for column in cs.description], row)) for row in cs.fetchall()]
        return jsonify(result)  # Return JSON response
