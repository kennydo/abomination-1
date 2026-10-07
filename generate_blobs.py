#!/usr/bin/env python3
"""Write 7 GiB of incompressible 512 KiB files into ./blobs."""

import os
import sys

BLOB_DIR = "blobs"
FILE_SIZE = 512 * 1024  # 512 KiB
TOTAL_SIZE = 7 * 1024**3  # 7 GiB
FILE_COUNT = TOTAL_SIZE // FILE_SIZE  # 14336


def main() -> None:
    os.makedirs(BLOB_DIR, exist_ok=True)
    width = len(str(FILE_COUNT - 1))
    for i in range(FILE_COUNT):
        path = os.path.join(BLOB_DIR, f"blob_{i:0{width}d}.bin")
        with open(path, "wb") as f:
            # os.urandom pulls from the OS CSPRNG, so the data won't compress.
            f.write(os.urandom(FILE_SIZE))
        if (i + 1) % 1024 == 0 or i + 1 == FILE_COUNT:
            print(f"{i + 1}/{FILE_COUNT} files written", file=sys.stderr)


if __name__ == "__main__":
    main()
