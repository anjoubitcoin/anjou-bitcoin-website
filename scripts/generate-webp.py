#!/usr/bin/env python3
"""Génère les dérivés WebP responsive des images d'articles.

Pour chaque image sous assets/images/articles/ (.jpg/.jpeg/.png), produit deux
variantes redimensionnées et compressées : « <base>-600.webp » (vignettes de la
grille) et « <base>-1200.webp » (image « hero » de l'article). Les gabarits
`_includes/postbox.html` et `_includes/post.html` les servent via <picture> avec
repli sur le fichier d'origine.

⚠️ À relancer après avoir ajouté une image d'article, sinon la balise <picture>
pointera vers un WebP inexistant (image cassée).

Prérequis : Pillow  (pip install Pillow)
Usage     : python scripts/generate-webp.py
"""
import os
from PIL import Image

ROOT = "assets/images/articles"
WIDTHS = (600, 1200)


def main() -> None:
    made = 0
    for dirpath, _, files in os.walk(ROOT):
        for f in files:
            ext = f.lower().rsplit(".", 1)[-1]
            if ext not in ("jpg", "jpeg", "png"):
                continue
            path = os.path.join(dirpath, f)
            base = path.rsplit(".", 1)[0]
            im = Image.open(path)
            im.load()
            if im.mode in ("RGBA", "LA", "P") and "transparency" in im.info:
                im = im.convert("RGBA")
            else:
                im = im.convert("RGB")
            w, h = im.size
            for width in WIDTHS:
                out = im if w <= width else im.resize(
                    (width, round(h * width / w)), Image.LANCZOS
                )
                out.save(f"{base}-{width}.webp", "WEBP", quality=80, method=6)
                made += 1
    print(f"{made} dérivés WebP générés sous {ROOT}/")


if __name__ == "__main__":
    main()
