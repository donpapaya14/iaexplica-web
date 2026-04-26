"""
Planifica temas evitando duplicados y rotando categorías.
Lee artículos existentes en src/content/blog/ para evitar repetir.
"""

import os
import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["herramientas", "prompts", "automatizacion", "productividad", "tutoriales"]

ARTICLE_FORMULAS = {
    "herramientas": [
        "Herramienta de IA gratuita REAL con nombre, URL, para que sirve y tutorial paso a paso",
        "Comparativa de 3 herramientas IA para [tarea especifica] con nombres reales, pros y contras",
        "Herramienta IA que reemplaza un software de pago: nombre, como funciona, ejemplo de uso",
        "Las 5 mejores extensiones de Chrome con IA: nombres reales, que hacen, como instalarlas",
    ],
    "prompts": [
        "Prompt EXACTO para ChatGPT/Claude que resuelve un problema concreto del dia a dia con ejemplo de resultado",
        "Tecnica de prompting avanzada (chain of thought, few-shot, etc.) explicada con ejemplo real",
        "Coleccion de 5 prompts para [profesion/tarea] con instrucciones exactas y resultados esperados",
        "Prompt que convierte ChatGPT en [experto especifico] con instrucciones palabra por palabra",
    ],
    "automatizacion": [
        "Automatizacion con IA para ahorrar X horas semanales con herramienta REAL y pasos concretos",
        "Workflow automatizado con herramientas IA gratuitas: paso a paso con nombres y capturas",
        "Como automatizar [tarea repetitiva] con IA: guia completa con herramienta real",
    ],
    "productividad": [
        "Rutina de productividad con IA: herramientas REALES para cada hora del dia laboral",
        "Como usar IA para escribir emails/informes/documentos en la mitad de tiempo con ejemplo real",
        "Organizacion personal con IA: apps REALES que organizan tu dia automaticamente",
    ],
    "tutoriales": [
        "Tutorial completo de [herramienta IA popular] desde cero con capturas y ejemplos paso a paso",
        "Como crear [tipo de contenido] con IA: guia paso a paso con herramientas gratuitas REALES",
        "De cero a experto en [herramienta IA]: lo que necesitas saber en 10 minutos",
    ],
}


def get_existing_titles() -> set[str]:
    """Lee títulos de artículos existentes del frontmatter."""
    titles = set()
    if not BLOG_DIR.exists():
        return titles

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if match:
            titles.add(match.group(1).lower().strip())
    return titles


def get_category_counts() -> dict[str, int]:
    """Cuenta artículos por categoría."""
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?(\w+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1) in counts:
            counts[match.group(1)] += 1
    return counts


def pick_category() -> str:
    """Elige categoría con menos artículos (rotación equilibrada)."""
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    """Elige fórmula aleatoria para la categoría."""
    formulas = ARTICLE_FORMULAS.get(category, ARTICLE_FORMULAS["nutricion"])
    return random.choice(formulas)


def plan_topic() -> dict:
    """Devuelve categoría y fórmula para el próximo artículo."""
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()

    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],  # Para contexto al AI
        "existing_count": len(existing),
    }
