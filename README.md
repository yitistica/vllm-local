### Workaround Vllm Image on giving supporting local HF model

#### usage
docker run vllm-local:latest --host 127.0.0.1 --port 8888 --hg_model model_id --hg_token hugging_face_hub_token

#### from the docker hub
docker run yeetech191/vllm-local:latest --host 127.0.0.1 --port 8888 --hg_model model_id --hg_token hugging_face_hub_token