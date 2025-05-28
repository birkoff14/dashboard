from django import template

register = template.Library()

@register.filter
def format_memory(value):
    """Convierte memoria de bytes a MB o GB automáticamente."""
    try:
        value = float(value)
        if value >= 1024**3:
            return f"{value / (1024**3):.2f} GB"
        elif value >= 1024**2:
            return f"{value / (1024**2):.2f} MB"
        elif value >= 1024:
            return f"{value / 1024:.2f} KB"
        return f"{value:.2f} B"
    except (ValueError, TypeError):
        return "N/A"
