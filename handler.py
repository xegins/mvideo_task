import typing as tp

from urllib import parse


def parse_url(url: str) -> tp.Tuple[str, float]:
    parsed_url: parse.ParseResult = parse.urlparse(url)
    path = parsed_url.path.strip("/")
    query = parsed_url.query.split("=")
    limit = 0.0
    if len(query) == 2 and "limit" in query:
        try:
            limit = float(query[1])
        except ValueError:
            pass
    return path, limit


def get_recommends(recommends: "Recommendation",
                   sku: str,
                   accuracy: float) -> tp.List[str]:
    return recommends.get_recommendation_for_product(sku, accuracy)
