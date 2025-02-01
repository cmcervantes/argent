from argparse import ArgumentParser
from dotenv import load_dotenv
from yaml import safe_load


__ENV_PATH = "config/.env"
__CONFIG_PATH = "config/argent_base_cfg.yml"



def __init__():
    # parse command line args
    argparser = ArgumentParser(
        description="Argent: A toolkit for automated narrative representation and understanding.")
    argparser.add_argument("--config", "-c", default=__CONFIG_PATH, help="Path to the argent yaml config file")
    args = argparser.parse_args()

    # load the environment and configuration variables
    load_dotenv(__ENV_PATH)
    cfg = safe_load(open(args.config, 'r'))



if __name__ == "__main__":
    __init__()
