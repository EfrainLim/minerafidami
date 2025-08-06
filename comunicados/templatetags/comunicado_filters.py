from django import template
import os

register = template.Library()

@register.filter
def filename(value):
    """Extrae solo el nombre del archivo de una ruta completa"""
    if value:
        return os.path.basename(str(value))
    return ""

@register.filter
def truncate_filename(value, length=30):
    """Trunca el nombre del archivo si es muy largo"""
    if value:
        filename = os.path.basename(str(value))
        if len(filename) > length:
            name, ext = os.path.splitext(filename)
            return name[:length-len(ext)-3] + "..." + ext
        return filename
    return "" 