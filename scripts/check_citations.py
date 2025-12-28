import os
import re
from typing import Set, List


def extract_citations_from_tex_dir(tex_dir: str) -> Set[str]:
    citation_keys = set()

    cite_pattern = re.compile(r"\\cite[a-zA-Z*]*\s*\{([^}]+)\}")

    for root, _, files in os.walk(tex_dir):
        for file in files:
            if file.endswith(".tex"):
                path = os.path.join(root, file)
                with open(path, "r", encoding="utf-8", errors="ignore") as f:
                    content = f.read()

                matches = cite_pattern.findall(content)
                for m in matches:
                    keys = [k.strip() for k in m.split(",")]
                    citation_keys.update(keys)

    return citation_keys


def split_bibtex_entries(bib_content: str) -> List[str]:
    entry_pattern = re.compile(r"@\w+\s*\{[\s\S]*?\n\}", re.MULTILINE)
    return entry_pattern.findall(bib_content)


def get_bibtex_key(entry: str) -> str | None:
    m = re.match(r"@\w+\s*\{\s*([^,\s]+)", entry)
    return m.group(1) if m else None


def trim_bib_file(bib_file: str, used_keys: Set[str], output_file: str | None = None):
    """
    删除 bib 中未被 tex 使用的条目
    - output_file 为 None 时：不写文件，只打印结果
    """
    with open(bib_file, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    entries = split_bibtex_entries(content)

    kept_entries = []
    removed_keys = []

    for entry in entries:
        key = get_bibtex_key(entry)
        if key is None:
            continue
        if key in used_keys:
            kept_entries.append(entry)
        else:
            removed_keys.append(key)

    if output_file is not None:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write("\n\n".join(kept_entries))
            f.write("\n")
        print(f"✅ 已生成精简后的 bib 文件: {output_file}")
    else:
        print("ℹ️ output_file=None，仅进行分析，不写出文件")

    print("\n====== BIB 中未被 TEX 使用的条目 ======")
    for k in sorted(removed_keys):
        print(k)


if __name__ == "__main__":
    tex_dir = "contents"
    bib_file = "refs.bib"

    tex_keys = extract_citations_from_tex_dir(tex_dir)
    trim_bib_file(bib_file=bib_file, used_keys=tex_keys)
