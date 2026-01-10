import json
from dataclasses import dataclass
from pathlib import Path
from uuid import UUID


@dataclass(frozen=True)
class DatasetItem:
    query: str
    relevant_docs: list[UUID]
    reference_answers: list[str]

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            query=data["query"],
            relevant_docs=[UUID(doc_id) for doc_id in data["relevantDocs"]],
            reference_answers=data["referenceAnswers"],
        )


class TestDataset:
    def __init__(self, items: list[DatasetItem]):
        self.items = items

    @classmethod
    def load(cls, path: Path):
        with open(path) as file:
            items = [DatasetItem.from_dict(json.loads(line.strip())) for line in file]
        return cls(items)

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index: int) -> DatasetItem:
        return self.items[index]
