from datasets import load_dataset
from typing import List, Tuple
import numpy as np


# Pending deprecation; it's likely we'll need to refactor
# to more appropriately represent the summarization content
def load(split: str = "train", n_samples: int = None) -> List[Tuple]:
    """
    Loads the Narrative QA dataset split and returns a list of text-summary pairs.

    Args:
        split (str): The dataset split to load (e.g., "train", "test", "validation"). Default is "train".
        n_samples (int, optional): The number of samples to load. If None, loads all samples. Default is None.

    Returns:
        List[Tuple]: A list of tuples where each tuple contains a chapter text and its corresponding summary.
    """
    # load the dataset split
    dataset = load_dataset("deepmind/narrativeqa", split=split)

    # since we're primarily using this dataset as a pairing of text and summary, 
    # we can ignore the other facets and return a list of those pairs
    # TODO: it is likely we'll need additional fields from this dataset; but for now we're
    #   only using the summary and the text
    sample_indices = range(len(dataset)) if n_samples is None else np.random.choice(range(len(dataset)), n_samples, replace=False).tolist()
    return [(dataset[i]["document"]["text"], dataset[i]["document"]["summary"]["text"]) for i in sample_indices]
