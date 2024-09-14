from contextvars import ContextVar

ctx_minio_client = ContextVar('minio_client')
ctx_http_client = ContextVar('http_client')
