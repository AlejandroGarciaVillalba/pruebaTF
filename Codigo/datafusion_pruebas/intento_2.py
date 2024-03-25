import requests
import json

# Definir la URL a la que se enviará la solicitud PUT
url = "https://datafusion-staging-parrvill-realstagingparrvill-dot-eusw1.datafusion.googleusercontent.com/api/v3/namespaces/default/apps/ingestastaging"

# Definir el payload o cuerpo de la solicitud en formato JSON
payload = """{
    "name": "ingestastaging",
    "description": "Data Pipeline Application",
    "artifact": {
        "name": "cdap-data-pipeline",
        "version": "6.9.2",
        "scope": "SYSTEM"
    },
    "config": {
        "resources": {
            "memoryMB": 2048,
            "virtualCores": 1
        },
        "driverResources": {
            "memoryMB": 2048,
            "virtualCores": 1
        },
        "connections": [
            {
                "from": "PostgreSQL",
                "to": "GCS"
            }
        ],
        "comments": [],
        "postActions": [],
        "properties": {},
        "processTimingEnabled": true,
        "stageLoggingEnabled": false,
        "stages": [
            {
                "name": "PostgreSQL",
                "plugin": {
                    "name": "Postgres",
                    "type": "batchsource",
                    "label": "PostgreSQL",
                    "artifact": {
                        "name": "postgresql-plugin",
                        "version": "1.10.2",
                        "scope": "SYSTEM"
                    },
                    "properties": {
                        "useConnection": "true",
                        "referenceName": "rna",
                        "importQuery": "SELECT * FROM \"rnacen\".\"rna\"",
                        "numSplits": "1",
                        "fetchSize": "1000",
                        "connectionTimeout": "100",
                        "schema": "{\"type\":\"record\",\"name\":\"etlSchemaBody\",\"fields\":[{\"name\":\"id\",\"type\":[\"long\",\"null\"]},{\"name\":\"upi\",\"type\":[\"string\",\"null\"]},{\"name\":\"timestamp\",\"type\":[{\"type\":\"long\",\"logicalType\":\"timestamp-micros\"},\"null\"]},{\"name\":\"userstamp\",\"type\":[\"string\",\"null\"]},{\"name\":\"crc64\",\"type\":[\"string\",\"null\"]},{\"name\":\"len\",\"type\":[\"int\",\"null\"]},{\"name\":\"seq_short\",\"type\":[\"string\",\"null\"]},{\"name\":\"seq_long\",\"type\":[\"string\",\"null\"]},{\"name\":\"md5\",\"type\":[\"string\",\"null\"]}]}",
                        "connection": "${conn(conexionpostgres)}"
                    }
                },
                "outputSchema": [
                    {
                        "name": "etlSchemaBody",
                        "schema": "{\"type\":\"record\",\"name\":\"etlSchemaBody\",\"fields\":[{\"name\":\"id\",\"type\":[\"long\",\"null\"]},{\"name\":\"upi\",\"type\":[\"string\",\"null\"]},{\"name\":\"timestamp\",\"type\":[{\"type\":\"long\",\"logicalType\":\"timestamp-micros\"},\"null\"]},{\"name\":\"userstamp\",\"type\":[\"string\",\"null\"]},{\"name\":\"crc64\",\"type\":[\"string\",\"null\"]},{\"name\":\"len\",\"type\":[\"int\",\"null\"]},{\"name\":\"seq_short\",\"type\":[\"string\",\"null\"]},{\"name\":\"seq_long\",\"type\":[\"string\",\"null\"]},{\"name\":\"md5\",\"type\":[\"string\",\"null\"]}]}"
                    }
                ],
                "id": "PostgreSQL",
                "type": "batchsource",
                "label": "PostgreSQL",
                "icon": "fa-plug",
                "$$hashKey": "object:302",
                "isPluginAvailable": true,
                "_uiPosition": {
                    "left": "390px",
                    "top": "177.6666717529297px"
                }
            },
            {
                "name": "GCS",
                "plugin": {
                    "name": "GCS",
                    "type": "batchsink",
                    "label": "GCS",
                    "artifact": {
                        "name": "google-cloud",
                        "version": "0.22.2",
                        "scope": "SYSTEM"
                    },
                    "properties": {
                        "useConnection": "true",
                        "referenceName": "depositardatosingesta",
                        "path": "gs://staging_parvilla/",
                        "suffix": "yyyy-MM-dd-HH-mm",
                        "format": "csv",
                        "location": "eu",
                        "contentType": "text/csv",
                        "schema": "{\"name\":\"etlSchemaBody\",\"type\":\"record\",\"fields\":[{\"name\":\"id\",\"type\":[\"long\",\"null\"]},{\"name\":\"upi\",\"type\":[\"string\",\"null\"]},{\"name\":\"timestamp\",\"type\":[{\"type\":\"long\",\"logicalType\":\"timestamp-micros\"},\"null\"]},{\"name\":\"userstamp\",\"type\":[\"string\",\"null\"]},{\"name\":\"crc64\",\"type\":[\"string\",\"null\"]},{\"name\":\"len\",\"type\":[\"int\",\"null\"]},{\"name\":\"seq_short\",\"type\":[\"string\",\"null\"]},{\"name\":\"seq_long\",\"type\":[\"string\",\"null\"]},{\"name\":\"md5\",\"type\":[\"string\",\"null\"]}]}",
                        "connection": "${conn(Cloud Storage Default)}",
                        "writeHeader": "true"
                    }
                },
                "outputSchema": [
                    {
                        "name": "etlSchemaBody",
                        "schema": "{\"name\":\"etlSchemaBody\",\"type\":\"record\",\"fields\":[{\"name\":\"id\",\"type\":[\"long\",\"null\"]},{\"name\":\"upi\",\"type\":[\"string\",\"null\"]},{\"name\":\"timestamp\",\"type\":[{\"type\":\"long\",\"logicalType\":\"timestamp-micros\"},\"null\"]},{\"name\":\"userstamp\",\"type\":[\"string\",\"null\"]},{\"name\":\"crc64\",\"type\":[\"string\",\"null\"]},{\"name\":\"len\",\"type\":[\"int\",\"null\"]},{\"name\":\"seq_short\",\"type\":[\"string\",\"null\"]},{\"name\":\"seq_long\",\"type\":[\"string\",\"null\"]},{\"name\":\"md5\",\"type\":[\"string\",\"null\"]}]}"
                    }
                ],
                "inputSchema": [
                    {
                        "name": "PostgreSQL",
                        "schema": "{\"type\":\"record\",\"name\":\"etlSchemaBody\",\"fields\":[{\"name\":\"id\",\"type\":[\"long\",\"null\"]},{\"name\":\"upi\",\"type\":[\"string\",\"null\"]},{\"name\":\"timestamp\",\"type\":[{\"type\":\"long\",\"logicalType\":\"timestamp-micros\"},\"null\"]},{\"name\":\"userstamp\",\"type\":[\"string\",\"null\"]},{\"name\":\"crc64\",\"type\":[\"string\",\"null\"]},{\"name\":\"len\",\"type\":[\"int\",\"null\"]},{\"name\":\"seq_short\",\"type\":[\"string\",\"null\"]},{\"name\":\"seq_long\",\"type\":[\"string\",\"null\"]},{\"name\":\"md5\",\"type\":[\"string\",\"null\"]}]}"
                    }
                ],
                "id": "GCS",
                "type": "batchsink",
                "label": "GCS",
                "icon": "fa-plug",
                "$$hashKey": "object:303",
                "isPluginAvailable": true,
                "_uiPosition": {
                    "left": "690px",
                    "top": "177.6666717529297px"
                }
            }
        ],
        "schedule": "0 1 */1 * *",
        "engine": "spark",
        "numOfRecordsPreview": 100,
        "rangeRecordsPreview": {
            "min": 1,
            "max": "5000"
        },
        "description": "Data Pipeline Application",
        "maxConcurrentRuns": 1,
        "pushdownEnabled": false,
        "transformationPushdown": {}
    },
    "version": "9d821e77-e50d-11ee-985f-ea8bbb0ee3cc"
}
"""
# Convertir el payload a formato JSON
json_payload = json.dumps(payload)

# Definir los encabezados de la solicitud
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer ya29.a0Ad52N3-gwK_vDsSUJbUVNrOAYpg95AiInLcbanDaZIzKtlJhHwVkVRkt7vX3bhOCzdCmREFZlQNTiXZ1mwKbx-P9ZK3TUnp7T5anFSat1ZmyEy5b0ZBF6CgJLrU6eJPjXocImGlGhDplmb7u6Lp_s4lX9Xo7JXy2dzmOLP-xgrnQqF6MWIInUegQ4y1Rj4JTNRfmdW4yKp4p9UWm73LKLAVsNUWNw7-FTwsMxal-Vl7cz07qAKYRnkqYzlmwG31Z2drGlX-Q91zuHtI49BDulhTWHRxjAaJLhz_BwLRt5LzXyN8eyMzP2Qi5a3Sc4zmCa2PU5lE9AE9drVj9zN-efLqUWxQfqVpSqDvVFItp2Y-d8oG6y1ikN69HnHetNRs23HfkrLrCrbmUFEQo30ONh0ua7dvC0gs6aCgYKASoSARESFQHGX2MintpSIu-7yJ3gzhDnI7CI1w0423"
}

# Realizar la solicitud PUT
response = requests.put(url, data=json_payload, headers=headers)

# Verificar el estado de la respuesta
if response.status_code == 200:
    print("La solicitud PUT fue exitosa.")
else:
    print(f"Error al realizar la solicitud PUT: {response.status_code} - {response.text}")
