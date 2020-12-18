import os

import typing as tp

from collections import defaultdict


class Recommendation:
    def __init__(self, recommendation_file_path: str = ""):
        self.recommendation: \
            tp.Dict[str, tp.List[tp.Optional[str, float]]] = defaultdict(list)
        self._recommendation_file_path: str = recommendation_file_path or "recommends.csv"
        self._load_recommendation_from_file()

    def _load_recommendation_from_file(self) -> None:
        if not os.path.exists(self._recommendation_file_path):
            raise FileNotFoundError(
                f"File '{self._recommendation_file_path}' - not found!"
            )
        with open(self._recommendation_file_path) as f:
            for row in f:
                product_code, recommended_product, recommended_level = row.split(",")
                self.recommendation[product_code].append(
                    (recommended_product, float(recommended_level))
                )

    def get_recommendation_for_product(self,
                                       sku: str,
                                       minimal_accuracy_level: float = 0.0) -> tp.List[str]:
        if sku not in self.recommendation:
            return []

        result = []
        for recommended_sku, accuracy in self.recommendation[sku]:
            if accuracy >= minimal_accuracy_level:
                result.append(recommended_sku)
        return result
