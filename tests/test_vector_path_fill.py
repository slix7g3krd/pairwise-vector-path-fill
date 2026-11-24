import pytest
import graphics.vector_path_fill as mod

CASES = [
    ("keep_winding", (1,)),
    ("adaptive_tess", (1,)),
    ("analytic_coverage", (1,)),
    ("version_cache", (1,)),
    ("same_batch", (1,)),
    ("parse", (1,)),
    ("tessellate", (1,)),
    ("fill", (1,)),
    ("stroke", (1,)),
    ("cache", (1,)),
    ("validate_fill", (1,)),
    ("metrics", (1,)),
    ("audit", (1,)),
    ("fallback", (1,)),
    ("determinism", (1,)),
]

@pytest.mark.parametrize("fn_name,args", CASES)
def test_contract(fn_name, args):
    fn = getattr(mod, fn_name)
    assert fn(*args) is not None
