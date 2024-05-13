import argparse

layer_parser = argparse.ArgumentParser()
layer_parser.add_argument('--hg_model')
layer_parser.add_argument('--hg_token')


def pop_kwargs_from_layers():

    args, left_over_args = layer_parser.parse_known_args()

    return args, left_over_args


def concat_download_dir_to_left_over_args(left_over_args, download_dir):

    left_over_args = [*left_over_args, "--download-dir", download_dir]

    return left_over_args
