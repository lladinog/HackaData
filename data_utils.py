import pandas as pd
import json

def extract_or_normalize_contract_type(value):
    """
    Normaliza un valor que puede ser JSON, nulo o una cadena simple a un tipo de contrato.
    Retorna 'No Definido' si no se puede extraer un tipo válido.
    """
    if pd.isna(value) or not isinstance(value, str) or not str(value).strip():
        return 'No Definido'

    cleaned_value = str(value).strip()

    # Si la cadena NO parece un JSON, la retorna directamente (asume que ya está aplanada)
    if not cleaned_value.startswith('{') and not cleaned_value.startswith('['):
        return cleaned_value

    # Intentar parsear JSON
    try:
        data = json.loads(cleaned_value)
        if isinstance(data, dict):
            # Prioridad: 'description' -> 'name' -> 'code'
            for key in ['description', 'name', 'code']:
                if key in data and data[key] is not None:
                    return str(data[key]).strip()
        return 'No Definido' # JSON válido pero sin las claves esperadas
    except json.JSONDecodeError:
        return cleaned_value # No es JSON válido, usar el valor crudo
    except Exception:
        return 'No Definido' # Cualquier otro error
