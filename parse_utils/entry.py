import os
import subprocess

from parse_utils.parse_args import pop_kwargs_from_layers, construct_lora_adapter_arg_str_for_vllm
from parse_utils.download_model import download_model_by_id


_HG_DOWNLOAD_DIR_KEY = 'hg_download_dir'
HG_DOWNLOAD_DIR = os.environ[_HG_DOWNLOAD_DIR_KEY]


def parse_and_download():

    layer_args, lora_adapters_settings, other_args = pop_kwargs_from_layers()

    for lora_adapter_name, lora_adapter_model_id in lora_adapters_settings.items():
        print(f'downloading lora model {lora_adapter_name} to "{HG_DOWNLOAD_DIR}"')
        download_model_by_id(model_id=lora_adapter_model_id,
                             download_dir=HG_DOWNLOAD_DIR,
                             token=layer_args.hg_token)
        print(f'completed downloading lora model {lora_adapter_name} to "{HG_DOWNLOAD_DIR}"')

    if lora_adapters_settings:
        lora_adapter_args_str = construct_lora_adapter_arg_str_for_vllm(download_dir=HG_DOWNLOAD_DIR,
                                                                        lora_adapters_settings=lora_adapters_settings)

        other_args.extend(['--enable-lora', '--lora-modules', lora_adapter_args_str])

    return other_args


def run_app():
    other_args = parse_and_download()
    completed_process = subprocess.run(['python3', '-m', 'vllm.entrypoints.openai.api_server', *other_args],
                                       capture_output=True, text=True)


if __name__ == "__main__":
    run_app()
