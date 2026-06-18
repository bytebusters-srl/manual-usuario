#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Utilidades para generar los bloques de capturas (\\captura) del manual.

Lee los archivos .txt de descripción "en bruto", limpia las referencias a las
imágenes y produce una leyenda mejorada para cada captura, garantizando que
TODAS las imágenes de cada carpeta queden incluidas en el documento.
"""
import os
import re

IMG_ROOT = "assets/img"
ABS_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def natural_key(s):
    return [int(t) if t.isdigit() else t.lower()
            for t in re.split(r'(\d+)', s)]


def list_images(folder):
    d = os.path.join(ABS_ROOT, IMG_ROOT, folder)
    files = [f for f in os.listdir(d)
             if f.lower().endswith((".png", ".jpg", ".jpeg"))]
    return sorted(files, key=natural_key)


def tex_escape(text):
    repl = {
        '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
        '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}',
        '^': r'\textasciicircum{}',
    }
    out = []
    for ch in text:
        out.append(repl.get(ch, ch))
    return ''.join(out)


def escape_plain(text):
    """Escapa los caracteres especiales de LaTeX en leyendas de texto plano
    (provenientes de los .txt). No se usa en las listas redactadas a mano, que
    contienen comandos como \\boton{} y \\campo{}."""
    for a, b in (('\\', r'\textbackslash{}'), ('&', r'\&'), ('%', r'\%'),
                 ('#', r'\#'), ('_', r'\_'), ('{', r'\{'), ('}', r'\}'),
                 ('~', r'\textasciitilde{}'), ('^', r'\textasciicircum{}')):
        text = text.replace(a, b)
    return text


def fix_quotes(text):
    """Convierte comillas rectas "..." en guillemets españoles «...».
    Evita además el conflicto de la comilla activa de babel-spanish."""
    text = re.sub(r'"([^"]*)"', r'«\1»', text)
    text = text.replace('"', '')  # comillas sueltas remanentes
    return text


def _norm(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = s.strip(' ,.;:')
    if not s:
        return s
    s = s[0].upper() + s[1:]
    return s + '.'


def parse_txt(txt_rel, prefix):
    """Devuelve dict token_lower -> leyenda limpia, a partir del .txt en bruto."""
    path = os.path.join(ABS_ROOT, IMG_ROOT, txt_rel)
    with open(path, encoding="utf-8", errors="ignore") as fh:
        raw = fh.read()
    tok = re.escape(prefix) + r'\d+(?:_\d+)?[a-z]?'
    tok_ext = tok + r'(?:\.(?:png|jpe?g))?'
    # Clausula de referencia a imagen (conector opcional + 'en la imagen' + token)
    ref_re = re.compile(
        r'(?i)\s*,?\s*'
        r'(?:(?:tal\s+)?como\s+(?:es\s+)?(?:se\s+\w+\s+)?'
        r'|proceso(?:\s+\w+){0,3}\s*'
        r'|seg[u\xfa]n\s+se\s+\w+\s+'
        r'|visible\s+'
        r'|que\s+se\s+\w+\s+(?:\w+\s+)?)?'
        r'(?:en\s+(?:la|el)\s+)?(?:im[a\xe1]gen(?:es)?\s+)?'
        + tok_ext +
        r'(?:\s*y\s*' + tok_ext + r')?\s*\.?'
    )
    tokfind = re.compile(r'(?i)' + tok)
    mapping = {}
    for line in raw.splitlines():
        line = line.strip()
        if not line:
            continue
        toks = [t.lower() for t in tokfind.findall(line)]
        if not toks:
            continue
        desc = ref_re.sub(' ', line)
        desc = re.sub(r'(?i)\b' + tok + r'\b', '', desc)  # restos sueltos
        # "La imagen X confirma..." -> al quitar "imagen X" queda "La confirma...":
        desc = re.sub(r'(?i)^\s*(?:la|el|esta|este)\s+'
                      r'(?=(?:confirma|ilustra|muestra|detalla|presenta|aparece|nos\b)\w*)',
                      '', desc)
        desc = re.sub(r'(?i)\ben\s+en\b', 'en', desc)        # typo "en en"
        desc = re.sub(r'(?i)\bdarle\s+click\b', 'hacer clic', desc)
        desc = re.sub(r'(?i)\bdarle\s+clic\b', 'hacer clic', desc)
        desc = _norm(desc)
        if not desc or len(desc) < 4:
            continue
        for t in toks:
            mapping.setdefault(t, desc)
    return mapping


def token_of(filename, prefix):
    base = os.path.splitext(filename)[0]
    return base.lower()


def block_from_txt(folder, prefix, txt_rel, idx_range=None,
                   fallback="Vista del apartado dentro de la plataforma."):
    """Genera \\captura para las imágenes de `folder` (subrango opcional 1-based)."""
    imgs = list_images(folder)
    if idx_range is not None:
        a, b = idx_range
        imgs = imgs[a - 1:b]
    mapping = parse_txt(txt_rel, prefix) if txt_rel else {}
    lines = []
    for f in imgs:
        key = token_of(f, prefix)
        cap = mapping.get(key, fallback)
        path = "%s/%s/%s" % (IMG_ROOT, folder, f)
        lines.append("\\captura{%s}{%s}" % (path, fix_quotes(escape_plain(cap))))
    return "\n".join(lines)


def block_from_list(folder, captions, order=None):
    """`captions`: lista alineada a las imágenes (orden natural o `order`)."""
    if order is not None:
        imgs = order
    else:
        imgs = list_images(folder)
    assert len(imgs) == len(captions), \
        "%s: %d imgs vs %d captions" % (folder, len(imgs), len(captions))
    lines = []
    for f, cap in zip(imgs, captions):
        path = "%s/%s/%s" % (IMG_ROOT, folder, f)
        lines.append("\\captura{%s}{%s}" % (path, fix_quotes(cap)))
    return "\n".join(lines)


def responsive_block(folder, items):
    """items: lista de (filename, caption). Empareja de a 2 con responsivePar."""
    lines = []
    i = 0
    while i < len(items):
        if i + 1 < len(items):
            f1, c1 = items[i]
            f2, c2 = items[i + 1]
            lines.append("\\responsivePar{%s/%s/%s}{%s}{%s/%s/%s}{%s}" % (
                IMG_ROOT, folder, f1, c1, IMG_ROOT, folder, f2, c2))
            i += 2
        else:
            f1, c1 = items[i]
            lines.append("\\responsiveUna{%s/%s/%s}{%s}" % (
                IMG_ROOT, folder, f1, c1))
            i += 1
    return "\n".join(lines)
