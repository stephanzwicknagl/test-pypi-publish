import pathlib
import os

DEFAULT_BACKEND_PROTOCOL = "http"
DEFAULT_BACKEND_HOST = "localhost"
DEFAULT_BACKEND_PORT = 5050
DEFAULT_FRONTEND_PORT = 8050
DEFAULT_BACKEND_URL = f"{DEFAULT_BACKEND_PROTOCOL}://{DEFAULT_BACKEND_HOST}:{DEFAULT_BACKEND_PORT}"
SHARED_PATH = pathlib.Path(__file__).parent.resolve()
GRAPH_PATH = SHARED_PATH / "viasp_graph_storage.json"
STATIC_PATH =  pathlib.Path(__file__).parent.parent.resolve() / "server/static/"
CLINGRAPH_PATH = os.path.join(STATIC_PATH, "clingraph")
PROGRAM_STORAGE_PATH = SHARED_PATH / "prg.lp"
STDIN_TMP_STORAGE_PATH = SHARED_PATH / "viasp_stdin_tmp.lp"
