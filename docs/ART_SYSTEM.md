# PREPFLOW ART SYSTEM

> Durable authority for PrepFlow artwork, visual ownership, production formats, and approved rendering rules. Current branch state, localhost state, exact commit hashes, and the next executable task belong in `docs/RESTART_PACKET.md`.

---

# 1. Visual Identity

PrepFlow uses **PrepFlow Illustrated Pixel**.

This is cinematic modern illustrated pixel art, not chunky retro pixel art.

Core principles:

- use crisp, intentional forms rather than random pixel noise;
- build assets from broad readable light and shadow masses before adding detail;
- use dark palette-related outlines rather than heavy pure black everywhere;
- reserve the strongest contrast for identity and interactive elements;
- use moderate contrast for supporting props;
- keep scenery quieter than controls and labels;
- use selective material texture rather than equal texture density everywhere;
- avoid dithering, scattered speckling, and hard stair-stepped edges;
- preserve approved artwork and supplied vector paths rather than recreating them unnecessarily.

Viewpoint is chosen per asset. Books may use a three-quarter view, people may face or turn naturally, tools should use the clearest readable angle, and environments must follow coherent scene perspective. There is no universal three-quarter-camera rule.

The current homepage palette combines warm amber and ivory highlights with cool blue-purple dusk shadows and deep navy-brown outlines.

---

# 2. Visual Ownership Boundaries

The homepage is composed from separate layers with separate owners.

## 2.1 Hospital background composite

Current runtime asset:

```text
web/images/home-hospital/prepflow-home-background-final.png
```

The composite owns permanent static scene artwork:

- hospital architecture;
- sky, sunset, landscaping, road, and environmental scenery;
- environmental lighting;
- the permanent architectural sign structures;
- permanent architectural lettering such as `REFERENCES`.

The current approved composite intentionally includes the left and right sign structures. This is a documented exception to the earlier plan that treated every sign as a separate runtime asset. The final composition was assembled from separately developed artwork and approved as one static scene plate.

The composite must not own:

- live button labels;
- hit areas;
- saved-session state;
- progress or block numbers;
- quiz instructions;
- chapter-selection state;
- accessibility labels;
- changing application data.

## 2.2 Architectural sign overlays

Live controls are positioned over the painted sign openings with HTML and CSS.

The left sign currently supports:

- `Start Here!` orientation copy;
- Build Your Quiz;
- Quiz in Progress;
- `Block X of Y`;
- Continue Quiz;
- Build a New Quiz.

The right sign supports the text-only Drug Library control.

The architectural perspective belongs to the artwork. Live control faces must remain visually front-facing, readable, and aligned to the painted openings. Visible command lettering and clickable areas must correspond closely; avoid oversized invisible hitboxes.

## 2.3 Book assets

The authoritative closed books for the current Quiz Builder interior
remain separate transparent clickable artwork:

```text
web/images/quiz-builder/books/fundamentals-closed.png
web/images/quiz-builder/books/pharm-closed.png
web/images/quiz-builder/books/medsurg-closed.png
```

The earlier files under `web/images/book-sprite-preview/` are historical and
must not replace the current Quiz Builder books.

The shared chapter-selection interior uses one transparent open-book asset:

```text
web/images/quiz-builder/books/quizbook-transparent.png
```

This neutral open book contains no subject-specific or changing information.
Subject title, chapters, counts, selection state, navigation, and accessibility
remain live browser-owned content. The same open-book asset is intentionally
reused for all three subjects.

Books own:

- permanent subject title;
- permanent cover color;
- permanent cover icon;
- permanent PrepFlow branding;
- cover, spine, pages, tabs, and material rendering.

Books do not own:

- question totals;
- chapter-selection counts;
- accessibility text;
- Pack paths;
- click behavior;
- disabled state;
- focus rings;
- changing status text.

The books now appear inside the dedicated quiz-builder screen rather than acting as the homepage's primary controls.

## 2.4 Nurse artwork

No nurse separation, nurse sprite production, nurse animation, or hospital-interior nurse scene has been implemented in the hospital-homepage milestone.

The previous city-and-nurses homepage is historical reference material. Nurse sprites may be reconsidered later, but they are not an approved current implementation requirement and must not be started merely because older dated documents proposed them.

If nurse assets are later approved, use separate transparent pose files initially. Do not create a sprite sheet unless repeated runtime animation or reuse justifies it.

## 2.5 HTML and JavaScript

HTML and JavaScript own:

- live control structure;
- button labels and accessibility labels;
- Pack paths;
- chapter-selection state;
- selected chapter counts;
- saved-session state;
- button enable/disable behavior;
- click behavior;
- quiz and progress data;
- temporary live homepage title and tagline.

Changing application information must remain live. Do not bake question totals, progress, saved-session state, or instructions into artwork.

## 2.6 CSS

CSS owns:

- placement and display size;
- the locked 16:9 scene composition;
- responsive layout;
- hover, pressed, disabled, and focus presentation;
- glow and drop-shadow treatment;
- command-label animation;
- live badge placement;
- alignment of controls to the painted sign openings.

CSS must not redraw principal final books or the hospital background with replacement illustrations.

Current relevant presentation files:

```text
web/hospital-home.css
web/quiz-builder-screen.css
web/approved-book-buttons.css
```

`web/hospital-home.css` is visually approved but currently contains a layered override stack accumulated during iteration. Consolidation is required as a protected cleanup milestone; do not casually delete or reconstruct the working cascade.

---

# 3. Permanent Artwork and Live Data

Permanent artwork may contain permanent identity and environmental lettering.

Changing application information remains live HTML, CSS, and JavaScript, including:

- question totals;
- selected chapter counts;
- progress;
- button instructions;
- saved-session state;
- accessibility labels;
- Pack paths;
- quiz scores.

The temporary homepage branding is live browser text:

```text
PrepFlow
Prepare. Practice. Progress.
```

It is a replaceable V1 treatment, not the permanent logo asset.

---

# 4. Production Formats

## 4.1 Transparent illustrated assets

Use transparent PNG masters during design and approval for books, characters, illustrated props, textured foreground objects, and reusable sign or emblem assets.

An optimized transparent WebP derivative may be used after approval when it preserves transparency, edge fidelity, color fidelity, and intended appearance.

## 4.2 SVG

Use SVG for clean interface symbols, simple scalable icons, approved cover emblems, logos, and diagrams that benefit from preserved paths.

Do not use SVG as the default final format for textured illustrated books, characters, or environment artwork.

## 4.3 Background plates

Use a static PNG or optimized WebP for a completed background plate when visual fidelity remains acceptable. Keep editable and review sources outside the runtime folder.

## 4.4 Dynamic interface elements

Use HTML and CSS for dynamic text, controls, status, and layout. Do not flatten changing application information into screenshots or background artwork.

---

# 5. Asset Folder Roles

Runtime browser assets belong under:

```text
web/images/
```

Only approved exports actually used by the browser belong there.

Source and review roles:

```text
art/source/
```

Editable masters, preserved vector paths, construction sources, and approved source artwork.

```text
art/review/
```

Comparisons, proof renders, enlarged inspections, and visual review images.

```text
web/images/
```

Approved runtime exports only.

Temporary ZIP files, timestamped backups, screenshots, superseded proofs, duplicate runtime copies, and transfer artifacts must not become permanent production assets.

The current untracked hospital artwork must be classified deliberately before release. Do not use `git add .`.

---

# 6. Approved Book System

## 6.1 Construction lock

The approved hardcover construction is the v21 geometry:

- visible front cover;
- visible back cover;
- full-depth continuous spine panel;
- visible page block;
- visible back-cover underside;
- all planes meet clearly;
- page block enters the spine and follows perspective;
- rear hinge remains hidden behind the page block;
- no floor shadow baked into the transparent asset.

This construction applies to all three subject books.

## 6.2 Tabs

Each book has three tabs. They are vertically separated, aligned with page perspective, and placed approximately 20%, 50%, and 80% through page-block depth.

## 6.3 Rendering master

Approved production rule:

- transparent 1024 × 1024 PNG master;
- smooth alpha;
- no hard alpha threshold;
- no tiny-palette final quantization;
- no dithering or scattered speckling;
- normal browser image smoothing.

## 6.4 Borders

Use one strong dark outer silhouette, one primary gold or cream cover border, and at most one quiet secondary inset border.

Do not use several alternating colored diagonal lines or braided multi-color outlines.

## 6.5 Page grain

Page-edge grain must follow page geometry. Use many fine restrained lines through the page-block thickness. Do not use a few crosswise bands running from cover to cover.

## 6.6 Subject locks

### Fundamentals

- title: `FUNDAMENTALS`;
- blue cover family;
- approved chart/clipboard emblem;
- shared vertical title-strip system.

### Pharm

- title: `PHARM`;
- green cover family;
- approved capsule artwork;
- shared vertical title-strip system.

### Med-Surg

- title: `MED-SURG`;
- purple cover family;
- approved stethoscope emblem;
- deeper silver-lavender icon panel;
- shared vertical title-strip system.

---

# 7. Homepage Composition

The approved local homepage uses:

- one locked 16:9 PrepFlow Teaching Hospital exterior composite;
- live HTML/CSS title and tagline;
- live left-sign launcher controls;
- live right-sign Drug Library control;
- a dedicated quiz-builder screen;
- separate transparent subject books inside the builder.

The hospital scene is the homepage environment. The books are no longer placed across the bottom of the main scene.

The permanent building sign reading `PREPFLOW TEACHING HOSPITAL` belongs to the scene. The larger live `PrepFlow` title in the upper-left sky is a temporary V1 browser layer.

Command attention treatment is limited to the live lettering. Borders, sign surfaces, and the background remain stationary. The current shared pulse uses opacity, scale, and text-shadow and has been visually verified in both new-quiz and saved-session states.

The complete transparent book is the clickable button inside the quiz builder. Zero-selection badges remain hidden; selected counts appear only when they communicate actual selected state.

---

# 7A. Quiz Builder Interior Composition

The current local Quiz Builder uses one contained 16:9 nursing-station scene:

```text
web/images/quiz-builder/prepflow-nursing-station-quiz-builder.png
```

The background, closed books, shelf plaques, and lower browser-owned controls
share one proportional scene-coordinate plane.

Approved closed-book resting geometry:

```text
width: 9.6%
bottom: 47.2%

Fundamentals left: 21.1%
Pharm left:        44.8%
Med-Surg left:     68.5%
```

Approved decorative plaque geometry:

```text
top: 58.0%

Fundamentals left: 24.9%
Pharm left:        47.6%
Med-Surg left:     70.5%
```

The visible book artwork animates independently of its fixed subject-card
hitbox. The approved sequence centers and enlarges the selected book, dims the
other books, holds briefly, pulses once, and then invokes the existing
chapter-opening behavior.

The plaques are live HTML/CSS scene decoration, not buttons.

For scene-bound objects sharing one painted surface, use measured rendered
geometry and one shared baseline. When a newer adjustment replaces an earlier
experimental CSS rule, remove or replace the superseded rule. Keep one
authoritative current rule unless another is intentionally required for a
distinct breakpoint, state, or interaction.

## 7.2 Drug Reference medication-room terminal

The approved Drug Reference desktop plate is:

```text
web/images/drug-reference/prepflow-medication-room-reference-station.png
```

Its locked native geometry is 1672 × 941. The live display opening runs from
`(442, 87)` to `(1261, 486)`, measuring 819 × 399 with an aspect ratio of
approximately 2.052632:1. Desktop and tablet-landscape HTML must remain inside
that opening; the plate owns the cabinet bezel and all surrounding equipment.
Implementation details and scene-relative percentages are recorded in
`docs/DRUG_REFERENCE_DESKTOP_TERMINAL.md`.

The mobile portrait Drug Reference intentionally remains a separate responsive
presentation and does not use the medication-room plate.

# 8. Asset Development Workflow

For one isolated asset:

1. inspect the current runtime asset and scene;
2. identify the exact decision being tested;
3. preserve locked geometry and approved source artwork;
4. create a rough proof only when needed;
5. state whether the proof is a study or usable runtime asset;
6. compare it at actual application size;
7. test it in the real local application;
8. obtain explicit visual approval;
9. export the approved runtime asset;
10. document the lock;
11. clean up safely;
12. commit and push only after verification.

Do not regenerate or flatten the complete scene when changing one isolated asset unless the approved production workflow specifically requires a new final composite.

Exploratory overrides may accumulate during visual iteration, but cleanup is part of the milestone. Before structural cleanup:

- create an external backup;
- preserve the approved rendered result;
- isolate cleanup from feature changes;
- test all states and hit areas in the real browser;
- run applicable automated tests;
- inspect the focused diff.

---

# 9. Local Visual Verification

Run the local server from the project root:

```bash
cd ~/projects/prepflow && python3 -m http.server 8004
```

Open:

```text
http://localhost:8004/web/
```

The server must run from the repository root because the sibling `packs/` directory must also be served.

Use `Ctrl+Shift+R` for a hard refresh.

Before changing CSS or artwork during a display problem:

1. verify the server is running;
2. verify its working directory;
3. open the target image directly by URL;
4. compare the direct asset with the homepage;
5. inspect the live DOM element;
6. inspect pseudo-elements and generated children;
7. inspect computed styles and animation state;
8. only then diagnose caching or service-worker behavior.

A clean diagnostic origin may use port 8005.

---

# 10. Decision Status Language

## Implemented and approved

Present in the real local application and explicitly approved.

## Approved but not implemented

A decided direction that still requires production work.

## Experimental

A temporary proof or local test that is not a permanent rule.

## Superseded

An earlier proof, workflow, or design that must not be restored.

Temporary experiments do not become permanent architecture merely because they exist in Git history or local backups.

---

# 11. Current Status

## Implemented and approved

- PrepFlow Teaching Hospital exterior homepage composite;
- locked 16:9 scene composition;
- architectural left and right signs in the final composite;
- live quiz and Drug Library controls aligned over the sign openings;
- dedicated quiz-builder screen;
- three approved transparent subject-book assets inside the builder;
- live saved-session and chapter-selection state;
- shared text-only command pulsing;
- temporary live PrepFlow title and tagline;
- 72 automated tests passing;
- real-browser functional and visual approval.

## Approved cleanup work not yet implemented

- consolidate `web/hospital-home.css` into one authoritative rule system while preserving the approved result;
- classify and relocate or remove duplicate untracked hospital source/review assets;
- review the layered-workflow brief before committing it as durable documentation;
- replace the temporary live title treatment when a permanent logo system is approved.

## Not currently implemented

- nurse sprite separation;
- nurse animation;
- redesign of the current chapter-selection layer;
- permanent reusable PrepFlow emblem.

## Superseded

- city-and-nurses homepage as the active implementation target;
- nurse separation as the automatic next milestone;
- books as the main homepage controls;
- CSS-drawn principal books;
- inline cover-emblem replacement artwork;
- Pharm-only prototype milestone;
- native 256 hard-edge book export;
- hard alpha threshold;
- tiny-palette quantization;
- braided multi-color outlines;
- crosswise cover-to-cover page bands;
- always-visible `OPEN BOOK` ovals;
- baked closed-book question totals.

---

# 12. Change Control

Update this document whenever a durable art, asset-ownership, rendering, format, folder, or cleanup rule changes.

Do not place temporary branch status, exact commit hashes, or the next executable task here. Those belong in `docs/RESTART_PACKET.md`.

When a newer approved decision replaces an older rule, update this document to reflect current truth and mark the old approach superseded where historical confusion is likely.
