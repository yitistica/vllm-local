from huggingface_hub import login
from huggingface_hub import snapshot_download


def log_in_hf(token):
    login(token=token, )


def download_model_by_id(model_id, local_dir=None, token=None):

    if token:
        log_in_hf(token=token)  # will raise if invalid;

    snapshot_download(repo_id=model_id, local_dir=local_dir)

