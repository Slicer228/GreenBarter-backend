from src.schemas.response_s import SchemaOffer


def offer_view(func):
    async def wrapper(*args):
        original = await func(*args)
        if original:
            return original
        else:
            return None
    return wrapper
