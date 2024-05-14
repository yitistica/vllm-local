import argparse
import pathlib
layer_parser = argparse.ArgumentParser()
layer_parser.add_argument('--lora_adapters')
layer_parser.add_argument('--hg_token')


def parse_lora_adapters_arg(lora_adapters_arg: str):
    lora_adapters_settings = dict()

    if lora_adapters_arg:

        for lora_adapter_str in lora_adapters_arg.split(','):
            lora_adapter_name, lora_adapter_model_id = lora_adapter_str.split('=')
            lora_adapters_settings[lora_adapter_name.strip()] = lora_adapter_model_id.strip()

    return lora_adapters_settings


def pop_kwargs_from_layers():

    args, left_over_args = layer_parser.parse_known_args()

    lora_adapters_settings = parse_lora_adapters_arg(args.lora_adapters)

    return args, lora_adapters_settings, left_over_args


def construct_lora_adapter_arg_str_for_vllm(download_dir, lora_adapters_settings: dict):

    lora_adapter_args_vllm = []

    for lora_adapter_name, lora_adapter_model_id in lora_adapters_settings.items():

        path_to_adapter = pathlib.Path(download_dir).joinpath(lora_adapter_model_id)

        lora_adapter_args_vllm.append(f'{lora_adapter_name}={path_to_adapter}')

    lora_adapter_args_str = ' '.join(lora_adapter_args_vllm)

    return lora_adapter_args_str

