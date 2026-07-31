# Drug Reference Desktop Terminal

## Scope

The desktop and tablet-landscape Drug Reference uses the complete approved
medication-room plate at:

```text
web/images/drug-reference/prepflow-medication-room-reference-station.png
```

The artwork owns the room, cabinet, drawers, scanner, badge reader, keyboard,
storage, permanent materials, and lighting. Browser-owned content is limited to
the blank display opening. The existing phone portrait implementation remains a
separate rule system under `html.mobile-portrait` and is not composed into the
room plate.

## Verified plate and opening geometry

The committed PNG IHDR reports a native size of **1672 × 941 pixels**. The
display opening was checked against the committed plate at these locked points:

| Point | Pixel coordinate |
| --- | ---: |
| Top-left | `(442, 87)` |
| Top-right | `(1261, 87)` |
| Bottom-right | `(1261, 486)` |
| Bottom-left | `(442, 486)` |

The opening is **819 × 399 pixels**, with an aspect ratio of
**2.0526315789473686:1**. Its scene-relative geometry is:

- left: `26.4354067%`;
- top: `9.2454835%`;
- width: `48.9832536%`;
- height: `42.4017003%`.

The CSS keeps the entire 1672:941 plate proportional, centers it in the
viewport, and places the header, compact browse toolbar, search/filter row, and
two-pane working area only within those percentages. Live content therefore
does not overlap the cabinet bezel, scanner, keyboard, drawers, or room.

## Runtime behavior

- The left pane is a dense, independently scrolling medication index. Rows
  include generic name, trade names, and routes. A selected row gains both a
  structural left marker and a checkmark in addition to its color treatment.
- The right pane independently scrolls an ivory clinical-reference card.
  Verified medication fields and safety color meanings remain unchanged.
- The first desktop visit rests on a live Drug Reference Index instead of
  automatically opening a medication.
- The index reports the current loaded medication count, explains all supported
  search dimensions, offers compact browse entry points, and shows a
  study-reference safety statement.
- The five most recently opened medication IDs may be stored in local storage.
  No patient, personal, search, or medication-content data is stored. When that
  list exists, the index offers Recently Viewed entries and Continue Last Card.
- An empty result set displays corrective search guidance in the index and
  results pane instead of leaving either pane blank.
- Search aliases, filtering dimensions, data loading, and all medication card
  content continue to use the existing registry and card sources.

## Review boundary

The desktop terminal requires local visual review at the intended Chromebook
desktop and tablet-landscape sizes before it can be called visually approved.
Automated checks establish geometry, loading, syntax, and application behavior;
they do not replace that review.
