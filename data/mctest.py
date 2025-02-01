from datasets import load_dataset
from typing import List
import numpy as np
from collections import defaultdict

from data.qa_document import QADocument

"""
The MCtest dataset is a multiple-choice question answering dataset. 
Each document contains text and at least one question with multiple choice answers.
"""

def load(split: str = "train", n_samples: int = None) -> List[QADocument]:
    """
    Load the MCtest dataset and return a list of QADocument objects.
    Args:
        split (str): The dataset split to load. Options are "train", "validation", "test". 
                     Defaults to "train".
        n_samples (int, optional): The number of samples to load. If None, load all samples. 
                                   Defaults to None.
    Returns:
        List[QADocument]: A list of QADocument objects containing the text, questions, and answers.
    """
    # load the dataset; retaining a particular split if specified
    dataset = load_dataset("sagnikrayc/mctest", "mc500")
    if split is None:
        splits = ["train", "validation", "test"]
    else:
        splits = [split]
    
    # unpack the dataset, reshaping the row-by-row into documents
    doc_texts = {}
    doc_questions, doc_answers = defaultdict(list), defaultdict(list)
    for s in splits:
        for d in dataset[s]:
            doc_id = d["idx"]["story"]
            if doc_id not in doc_texts:
                doc_texts[doc_id] = d["story"]
            doc_questions[doc_id].append(d["question"])
            doc_answers[doc_id].append(d["answer_options"][d["answer"]])
    documents = []
    for doc_id, text in doc_texts.items():
        documents.append(QADocument(text, doc_questions[doc_id], doc_answers[doc_id], doc_id))
    if n_samples is not None:
        documents = np.random.choice(documents, n_samples, replace=False).tolist()
    return documents
