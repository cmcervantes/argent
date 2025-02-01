import json
from os import getenv
from os.path import join as pth_join
from typing import List
import numpy as np

# from data.qa_document import QADocument
from data.qa_document import QADocument

"""
The BiPaR dataset is an extractive question answering dataset, where each document
is broken up into paragraphs, questions refer to those paragraphs, and there can be 
multiple valid answers for each question.
"""

def load(split: str = "train", n_samples: int = None) -> List[QADocument]:
    """
    Load the BiPaR dataset and return a list of QADocument objects.
    Args:
        split (str): The dataset split to load. Options are "train", "valid", "test". 
                     Defaults to "train".
        n_samples (int, optional): The number of samples to load. If None, load all samples. 
                                   Defaults to None.
    Returns:
        List[QADocument]: A list of QADocument objects containing the text, questions, and answers.
    """
    if split not in ["train", "valid", "test"]:
        raise ValueError("Invalid split specified; options are 'train', 'valid', 'test'.")
    
    # load the specified dataset split
    with open(pth_join(getenv("LOCAL_DATA_DIR"), "BiPaR", "Monolingual", "EN", f"Monolingual_EN_{split}.json"), 'r') as f:
        dataset = json.load(f)

    documents = []
    for d in dataset["data"]:
        title = d["title"]

        for i, p in enumerate(d["paragraphs"]):
            doc_text = p["context"]
            questions, answers = [], []
            for qa in p["qas"]:
                # the structure of this dataset is that each question 
                # has multiple potentially valid answers (e.g., "eighty dollars" v "eighty dollars a month")
                # For now, retain all as QA pairs
                # TODO: consider integrating single-question-multiple-answers into QADocument
                q = qa["question"]
                
                # while this dataset also contans "answer_start" -- 
                # the character index of the answer -- we're 
                # dropping this for the moment
                # TODO: integrate character indices into QADocument
                for a in qa["answers"]:
                    questions.append(q)
                    answers.append(a["text"])
            
            # while the dataset considers the documents as a whole,
            # we retain paragraphs in isolation
            # TODO: integrate higher order connections (e.g., paragraphs of a document) into QADocument
            documents.append(QADocument(
                text=doc_text, questions=questions,
                answers=answers, doc_id=f"{title}_{i}"))
   
    if n_samples is not None:
        documents = np.random.choice(documents, n_samples, replace=False).tolist()
    return documents
