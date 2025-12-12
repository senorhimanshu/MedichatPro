# python - <<'PY'
import inspect
import pydantic
import euriai.langchain as e

print("pydantic version:", pydantic.__version__)
print("euriai version:", getattr(e, "__version__", "unknown"))
# Where is Field coming from inside euriai.langchain?
print("euriai.langchain.Field ->", e.__dict__.get("Field", None))
try:
    src = inspect.getsource(e)
    snippet = "\n".join(src.splitlines()[:120])  # first 120 lines
    print("\n--- top of euriai.langchain.py ---\n")
    print(snippet)
except Exception as ex:
    print("Couldn't load source for euriai.langchain:", ex)
# PY
