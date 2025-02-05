import torch
from transformers import (
    AutoModelForCausalLM, AutoTokenizer, 
    pipeline, BitsAndBytesConfig
)
from langchain_huggingface import HuggingFacePipeline


def create_hf_pipeline(model_cfg: dict) -> HuggingFacePipeline:
    """
    Initializes the text generation pipeline using the specified model configuration.

    :param model_cfg: A dictionary containing the model configuration.
    :return: HuggingFacePipeline
    """
    # set up the device, defaulting to GPU / MPS where possible
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if torch_device == "cpu" and torch.mps.is_available():
        torch_device = "mps"
    
    # Though this isn't strictly necessary, create a separate model 
    # and tokenizer for the pipeline (in the future we may want to 
    # swap out these components)
    model = AutoModelForCausalLM.from_pretrained(
        model_cfg["name"],
        quantization_config=BitsAndBytesConfig(**model_cfg["quant_config"])
    )
    tokenizer = AutoTokenizer.from_pretrained(model_cfg["name"])
    pipe = pipeline("text-generation", model=model, tokenizer=tokenizer)
    
    return HuggingFacePipeline(pipeline=pipe)
    