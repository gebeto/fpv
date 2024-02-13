---
description: This is my favourite indoor whoop
---

# Bibek (Mobula6)

This is my favourite indoor whoop

## ⚠️ Warning

1. Here is rotated FC for -90 degrees (`set align_board_yaw = -90`), in stock mobula, if you not rotated your FC, this value should be `set align_board_yaw = 90`
2. Check your motors order, this diff has my motors order, it can be different for you
3. This `diff` includes my `rates` and `osd`

## Diff all

Download link: [diff.txt](./Bibek.txt)

{% capture diff %}
{% include_relative Bibek.txt %}
{% endcapture %}

```sh
{{ diff | strip }}
```