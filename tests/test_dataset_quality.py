from agentic_soc_factory.pipeline.dataset import split_dataset
from agentic_soc_factory.pipeline.quality import leakage_overlap


def test_split_dataset_sizes():
    rows = [{"id": str(i), "messages": []} for i in range(100)]
    splits = split_dataset(rows, seed=1)
    assert len(splits["train"]) == 80
    assert len(splits["val"]) == 10
    assert len(splits["test"]) == 10


def test_leakage_overlap():
    train = [{"messages": [{"role": "user", "content": "A"}]}]
    test = [{"messages": [{"role": "user", "content": "A"}]}]
    assert leakage_overlap(train, test) == 1.0
