import os

import typing as tp

from collections import defaultdict


class Recommendation:
    def __init__(self, recommendation_file_path: str):
        self.recommendation: \
            tp.Dict[str, tp.List[tp.Optional[str, float]]] = defaultdict(list)
        self._recommendation_file_path: str = recommendation_file_path
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
        self._sort_recommendation_value_by_accuracy()

    def _sort_recommendation_value_by_accuracy(self) -> None:
        for key, values in self.recommendation.items():
            self.recommendation[key] = sorted(values, key=lambda elem: elem[1])

    @staticmethod
    def _search_lower_bound_index(values: tp.List[tp.Tuple[str, float]],
                                  accuracy: float) -> int:
        if values[0][1] >= accuracy:
            return 0

        left, mid, right = 0, len(values) // 2, len(values) - 1

        while values[mid][1] != accuracy and left < right:
            if accuracy > values[mid][1]:
                left = mid + 1
            else:
                right = mid - 1
            mid = (left + right) // 2
        while values[mid - 1][1] == accuracy:
            mid -= 1
        return mid

    def get_recommendation_for_product(self,
                                       sku: str,
                                       minimal_accuracy_level: float = 0.0) -> tp.List[str]:
        if sku not in self.recommendation:
            return []

        recommends_for_sku = self.recommendation[sku]
        index = self._search_lower_bound_index(recommends_for_sku, minimal_accuracy_level)
        return [recommended_product[0] for recommended_product in recommends_for_sku[index:]]
