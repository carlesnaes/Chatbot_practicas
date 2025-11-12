import bleach

# --- Configuración base ---
ALLOWED_TAGS = ["a", "b", "i", "br"]
ALLOWED_ATTRS = {"a": ["href"]}
ALLOWED_PROTOCOLS = ["http", "https"]

def sanitize_html(text: str) -> str:
    """
    Limpia HTML de entrada para prevenir XSS o inyecciones.
    Permite solo etiquetas y atributos seguros.
    """
    if not text:
        return ""
    
    clean = bleach.clean(
        text,
        tags=ALLOWED_TAGS,
        attributes=ALLOWED_ATTRS,
        protocols=ALLOWED_PROTOCOLS,
        strip=True
    )

    # Protección extra: eliminar javascript: o data: si se colaron tras decodificación
    if "javascript:" in clean.lower():
        clean = clean.replace("javascript:", "")
    if "data:" in clean.lower():
        clean = clean.replace("data:", "")

    return clean.strip()
