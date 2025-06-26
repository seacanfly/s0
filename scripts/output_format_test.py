import io
import sys
from s0c0.main import solve

def test_output_format():
    sys.stdout = io.StringIO()
    solve()
    out = sys.stdout.getvalue().strip()
    assert out.startswith("Result: "), f"输出格式错误：{out}"

test_output_format()
print("✅ 输出格式检查通过")
