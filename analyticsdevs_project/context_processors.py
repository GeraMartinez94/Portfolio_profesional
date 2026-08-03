import os
import json

def ga_settings(request):
    """Context processor que expone las variables esenciales de Google Analytics a las plantillas.

    Proporciona:
    - GA_MEASUREMENT_ID: para usar en gtag.js
    - GA_PROPERTY_ID: id de propiedad (opcional)
    - GA_SERVICE_ACCOUNT_PATH: ruta al JSON de cuenta de servicio (opcional)
    - GA_SERVICE_ACCOUNT_JSON: carga JSON parseado si se definió como variable
    - GA_ENABLED: booleano que indica si alguna credencial está presente
    """
    ga_measurement_id = os.environ.get('GA_MEASUREMENT_ID')
    ga_property_id = os.environ.get('GA_PROPERTY_ID')
    ga_service_account_path = os.environ.get('GA_SERVICE_ACCOUNT_PATH')
    ga_service_account_json = os.environ.get('GA_SERVICE_ACCOUNT_JSON')

    ga_service_account = None
    if ga_service_account_json:
        try:
            ga_service_account = json.loads(ga_service_account_json)
        except Exception:
            ga_service_account = None

    ga_enabled = bool(ga_measurement_id or ga_service_account_path or ga_service_account)

    return {
        'GA_MEASUREMENT_ID': ga_measurement_id,
        'GA_PROPERTY_ID': ga_property_id,
        'GA_SERVICE_ACCOUNT_PATH': ga_service_account_path,
        'GA_SERVICE_ACCOUNT_JSON': ga_service_account,
        'GA_ENABLED': ga_enabled,
    }
