"""
案例：基于传入的数值（每批次的歌词条数），创建 生成器，生成批次歌词
"""

import math
from pathlib import Path

base_dir = Path(__file__).parent


def dataset_loader(batch_size):
    """
    :param batch_size:每批次的歌词条数
    :return: 生成器，每个元素都是一批次的数据
    """

    with open(base_dir / "lyrics.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()

        # 计算批次总理
        total_batch = math.ceil(len(lines) / batch_size)

        # for idx in range(total_batch):
        #     yield lines[idx * batch_size : (idx + 1) * batch_size]
        yield from (
            lines[idx * batch_size : (idx + 1) * batch_size]
            for idx in range(total_batch)
        )


dl = dataset_loader(8)
for batch_data in dl:
    print(batch_data)
