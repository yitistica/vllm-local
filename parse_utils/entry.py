import os

from parse_utils.parse_args import pop_kwargs_from_layers, concat_download_dir_to_left_over_args
from parse_utils.download_model import download_model_by_id


_HG_DOWNLOAD_DIR_KEY = 'hg_download_dir'
HG_DOWNLOAD_DIR = os.environ[_HG_DOWNLOAD_DIR_KEY]


def parse_and_download():

    layer_args, other_args = pop_kwargs_from_layers()

    print(f'downloading model {layer_args.hg_model} to "{HG_DOWNLOAD_DIR}"')
    download_model_by_id(model_id=layer_args.hg_model,
                         local_dir=HG_DOWNLOAD_DIR,
                         token=layer_args.hg_token)
    print(f'completed downloading model {layer_args.hg_model} to "{HG_DOWNLOAD_DIR}"')

    other_args = concat_download_dir_to_left_over_args(other_args,
                                                       download_dir=HG_DOWNLOAD_DIR)

    return other_args


if __name__ == "__main__":

    other_args = parse_and_download()
    left_over_args = ' '.join(other_args)
    print(left_over_args)
