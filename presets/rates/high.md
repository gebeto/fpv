---
description: My favorite high rates
---

# High rates

![HIgh Rates](./high.png)

## Diff

Download link: [high.txt](./high.txt)

{% capture diff %}
{% include_relative high.txt %}
{% endcapture %}

```sh
{{ diff | strip }}
```