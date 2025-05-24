<!-- Markdown templates, etc. -->
<!-- まだ使用してない -->
## {{ date }} – Insight List

{% for item in insights %}
- 🧠 {{ item.summary }}
  Tags: {{ item.tags }} (Source: {{ item.source }})
{% endfor %}
