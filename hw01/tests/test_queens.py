# 方式：将仓库根目录加入 Python 路径，确保能找到 hw01 包
import sys
from pathlib import Path
# 获取仓库根目录（oiiai）
ROOT_DIR = Path(__file__).parent.parent.parent
sys.path.append(str(ROOT_DIR))

# 此时即可正常导入
from hw01.src.queens_solver import solve_n_queens

def test_n4_queens():
    assert len(solve_n_queens(4)) == 2

def test_n8_queens():
    assert len(solve_n_queens(8)) == 92