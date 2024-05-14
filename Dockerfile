FROM vllm/vllm-openai:latest

COPY ./serve.sh serve.sh
COPY parse_utils parse_utils

RUN mkdir downloaded_model
ENV hg_download_dir="downloaded_model/"

EXPOSE 8000

ENTRYPOINT ["bash", "serve.sh"]
