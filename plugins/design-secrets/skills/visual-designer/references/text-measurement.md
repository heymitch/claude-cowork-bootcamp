# Text Measurement for SVG Layout

SVG `<text>` doesn't wrap, constrain, or auto-layout. You must calculate widths before placing elements. This reference provides character-width approximations for common fonts so you can compute column widths, avoid overlaps, and build proper grids.

## Character Width Table (pixels per character at 1x scale)

Measured at common sizes. Multiply by character count, then add letter-spacing.

### Monospace Fonts (fixed-width — every character same width)

| Font | Size | Char Width | With letter-spacing 2px | With letter-spacing 3px |
|---|---|---|---|---|
| Space Mono | 11px | 7.3px | 9.3px | 10.3px |
| Space Mono | 12px | 8.0px | 10.0px | 11.0px |
| Space Mono | 14px | 9.3px | 11.3px | 12.3px |
| Space Mono 700 | 12px | 8.2px | 10.2px | 11.2px |
| JetBrains Mono | 12px | 7.8px | 9.8px | 10.8px |
| Courier New | 12px | 7.2px | 9.2px | 10.2px |

### Display Fonts (variable-width — use average, add 15% buffer)

| Font | Size | Avg Char Width | Buffer (×1.15) |
|---|---|---|---|
| Oswald 700 | 22px | 10.5px | 12.1px |
| Oswald 700 | 28px | 13.5px | 15.5px |
| Oswald 700 | 36px | 17.5px | 20.1px |
| Oswald 700 | 48px | 23px | 26.5px |
| Bebas Neue | 28px | 12px | 13.8px |
| Anton | 28px | 13px | 15px |

### Body Fonts (variable-width — use average, add 15% buffer)

| Font | Size | Avg Char Width | Buffer (×1.15) |
|---|---|---|---|
| Inter 400 | 14px | 7.2px | 8.3px |
| Inter 400 | 16px | 8.2px | 9.4px |
| Inter 400 | 18px | 9.2px | 10.6px |
| Inter 600 | 16px | 8.5px | 9.8px |
| Inter 600 | 18px | 9.5px | 10.9px |

## Formula

```
text_width = (char_count × char_width) + ((char_count - 1) × letter_spacing)
column_width = text_width + padding_left + padding_right
```

For mono fonts (fixed width), this is exact.
For variable-width fonts, add the 15% buffer because wide characters (M, W, @) blow out the average.

## Example: Computing a Label Column

Longest label: "BROWSER AUTOMATION" = 18 characters
Font: Space Mono 12px, letter-spacing 3px

```
text_width = (18 × 8.0) + (17 × 3) = 144 + 51 = 195px
with padding (20px each side) = 195 + 40 = 235px
```

So the label column needs to be AT LEAST 235px wide.

## Grid Layout Pattern for Comparison Infographics

```
|← label_col →|← gap →|← chat_col →|← gap →|← cowork_col →|
|   235px      | 20px  |   420px    | 20px  |   420px       |
```

Total: 235 + 20 + 420 + 20 + 420 = 1115px (fits in 1200px canvas with 40px margins)

### Computing Each Column

1. **Find the longest text in each column** (count characters)
2. **Compute its pixel width** using the table above
3. **Add padding** (20px each side minimum)
4. **That's the column width** — all elements in that column use the same x-start

### Placing Text in the Grid

```
label_x = margin (40px)
chat_x = margin + label_col + gap
cowork_x = margin + label_col + gap + chat_col + gap
```

Every row uses the same x positions. No manual per-row positioning.

## Self-Check

After computing the grid, verify:
- [ ] Total width (all columns + gaps + margins) ≤ canvas width
- [ ] Longest text in each column fits within column width
- [ ] No x positions overlap between columns
- [ ] Consistent padding in every row
