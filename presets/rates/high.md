---
description: My favorite high rates
---

# High rates

![HIgh Rates](https://i.imgur.com/OXMw9JQ.png)

## Diff

Download link: [high.txt](./high.txt)

{% capture diff %}
{% include_relative high.txt %}
{% endcapture %}

```sh
{{ diff | strip }}
```