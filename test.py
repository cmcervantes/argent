import torch
from transformers import pipeline
from dotenv import load_dotenv
from os import getenv
from yaml import safe_load


from data import booksum

def __init_pipeline(model_cfg: dict) -> pipeline:
    """
    Initializes the text generation pipeline using the specified model configuration.

    Args:
        model_cfg (dict): A dictionary containing the model configuration. 
                          It should include the model name and pipeline arguments.

    Returns:
        pipeline: An instance of the text generation pipeline.
    """
    torch_device = "cuda" if torch.cuda.is_available() else "cpu"
    if torch_device == "cpu" and torch.mps.is_available():
        torch_device = "mps"
    pipe = pipeline(
        "text-generation",
        model=model_cfg["name"],
        model_kwargs=model_cfg["pipeline_args"],
        device=torch_device
    )
    return pipe


def __init__():
    # load the environment and configuration variables
    # TODO: reference these files by parsed argument (probably with these as defaults)
    load_dotenv("config/.env")
    cfg = safe_load(open("config/argent_base_cfg.yml", 'r'))

    # load the dataset
    dataset = booksum.load(n_samples=10)
    for i, (text, summary) in enumerate(dataset):
        print(f"Sample {i}:")
        print(f"Text: {text[:20]}")
        print(f"Summary: {summary[:20]}")
        print("\n")
    quit()

    # instantiate the model
    llm_pipe = __init_pipeline(cfg["model"])

    # call the model   
    messages = [
        {"role": "user", "content": "Who are you? Please, answer in pirate-speak."},
    ]
    outputs = pipe(messages, max_new_tokens=256)
    assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
    print(assistant_response)




if __name__ == "__main__":
    __init__()
