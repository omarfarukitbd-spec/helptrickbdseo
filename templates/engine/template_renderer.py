#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
templates/engine/template_renderer.py
--------------------------------------------------------------
HelpTrickBD Zero-Dependency Semantic Template Engine.

Provides high-speed rendering of Post Archetypes:
- Supports {{ variable }}
- Supports {% if condition %} ... {% endif %}
- Supports {% for item in items %} ... {% endfor %}
- Supports {% include 'partial.html' %}
- Replaces massive 1,300-line hardcoded python files with clean, reusable HTML templates!
"""

import os
import re

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
TEMPLATES_DIR = os.path.join(PROJECT_ROOT, "templates")

def render_template(template_name: str, context: dict) -> str:
    """Renders a template file located in templates/archetypes/ or templates/ with given context."""
    tpl_path = os.path.join(TEMPLATES_DIR, "archetypes", template_name)
    if not os.path.exists(tpl_path):
        tpl_path = os.path.join(TEMPLATES_DIR, template_name)
    
    if not os.path.exists(tpl_path):
        raise FileNotFoundError(f"Template not found: {template_name} (checked {tpl_path})")

    with open(tpl_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Handle {% include '...' %}
    def replace_include(match):
        inc_file = match.group(1).strip("'\"")
        inc_path = os.path.join(TEMPLATES_DIR, "partials", inc_file)
        if os.path.exists(inc_path):
            with open(inc_path, "r", encoding="utf-8") as inc_f:
                return inc_f.read()
        return ""

    content = re.sub(r"\{%\s*include\s+(['\"].*?['\"])\s*%\}", replace_include, content)

    # 2. Handle {% for item in list %} ... {% endfor %}
    def replace_for(match):
        item_var = match.group(1).strip()
        list_var = match.group(2).strip()
        body = match.group(3)

        items = context.get(list_var, [])
        if not isinstance(items, (list, tuple)):
            return ""

        output = []
        for it in items:
            sub_ctx = dict(context)
            if isinstance(it, dict):
                for k, v in it.items():
                    sub_ctx[f"{item_var}.{k}"] = str(v)
            else:
                sub_ctx[item_var] = str(it)

            # Render inner body with sub_ctx
            rendered_body = body
            for k, v in sub_ctx.items():
                rendered_body = rendered_body.replace(f"{{{{ {k} }}}}", str(v))
                rendered_body = rendered_body.replace(f"{{{{{k}}}}}", str(v))
            output.append(rendered_body)

        return "".join(output)

    for_pattern = re.compile(r"\{%\s*for\s+(\w+)\s+in\s+(\w+)\s*%\}(.*?)\{%\s*endfor\s*%\}", re.DOTALL)
    content = for_pattern.sub(replace_for, content)

    # 3. Handle {% if condition %} ... {% endif %}
    def replace_if(match):
        cond_var = match.group(1).strip()
        body = match.group(2)
        val = context.get(cond_var)
        if val:
            return body
        return ""

    if_pattern = re.compile(r"\{%\s*if\s+(\w+)\s*%\}(.*?)\{%\s*endif\s*%\}", re.DOTALL)
    content = if_pattern.sub(replace_if, content)

    # 4. Handle simple variables {{ var }}
    for k, v in context.items():
        if isinstance(v, (str, int, float)):
            content = content.replace(f"{{{{ {k} }}}}", str(v))
            content = content.replace(f"{{{{{k}}}}}", str(v))

    return content
