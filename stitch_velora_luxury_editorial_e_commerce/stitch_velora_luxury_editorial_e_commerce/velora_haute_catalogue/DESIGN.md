---
name: Velora Haute Catalogue
colors:
  surface: '#fff7ff'
  surface-dim: '#e3d5ef'
  surface-bright: '#fff7ff'
  surface-container-lowest: '#ffffff'
  surface-container-low: '#faf0ff'
  surface-container: '#f6e9ff'
  surface-container-high: '#f1e3fe'
  surface-container-highest: '#ebddf8'
  on-surface: '#20182b'
  on-surface-variant: '#4a4453'
  inverse-surface: '#352d41'
  inverse-on-surface: '#f8edff'
  outline: '#7b7484'
  outline-variant: '#cbc3d5'
  surface-tint: '#6d44c2'
  primary: '#3c008d'
  on-primary: '#ffffff'
  primary-container: '#5426a8'
  on-primary-container: '#c1a5ff'
  inverse-primary: '#d1bcff'
  secondary: '#6c509a'
  on-secondary: '#ffffff'
  secondary-container: '#ccadff'
  on-secondary-container: '#583c85'
  tertiary: '#3a0090'
  on-tertiary: '#ffffff'
  tertiary-container: '#5222b1'
  on-tertiary-container: '#bfa6ff'
  error: '#ba1a1a'
  on-error: '#ffffff'
  error-container: '#ffdad6'
  on-error-container: '#93000a'
  primary-fixed: '#eaddff'
  primary-fixed-dim: '#d1bcff'
  on-primary-fixed: '#24005b'
  on-primary-fixed-variant: '#5527a9'
  secondary-fixed: '#ecdcff'
  secondary-fixed-dim: '#d5baff'
  on-secondary-fixed: '#260453'
  on-secondary-fixed-variant: '#533881'
  tertiary-fixed: '#e9ddff'
  tertiary-fixed-dim: '#d0bcff'
  on-tertiary-fixed: '#23005c'
  on-tertiary-fixed-variant: '#5323b2'
  background: '#fff7ff'
  on-background: '#20182b'
  surface-variant: '#ebddf8'
typography:
  display-xl:
    fontFamily: Anton
    fontSize: 5.5rem
    fontWeight: '400'
    lineHeight: 5.25rem
    letterSpacing: 0.04em
  display-xl-mobile:
    fontFamily: Anton
    fontSize: 3rem
    fontWeight: '400'
    lineHeight: 3rem
    letterSpacing: 0.03em
  headline-lg:
    fontFamily: Anton
    fontSize: 3.5rem
    fontWeight: '400'
    lineHeight: 3.5rem
    letterSpacing: 0.03em
  headline-lg-mobile:
    fontFamily: Anton
    fontSize: 2.25rem
    fontWeight: '400'
    lineHeight: 2.25rem
    letterSpacing: 0.02em
  headline-md:
    fontFamily: Anton
    fontSize: 2rem
    fontWeight: '400'
    lineHeight: 2.25rem
    letterSpacing: 0.02em
  body-lg:
    fontFamily: Inter
    fontSize: 1.125rem
    fontWeight: '400'
    lineHeight: 1.75rem
    letterSpacing: -0.01em
  body-md:
    fontFamily: Inter
    fontSize: 0.9375rem
    fontWeight: '400'
    lineHeight: 1.5rem
    letterSpacing: 0em
  body-sm:
    fontFamily: Inter
    fontSize: 0.8125rem
    fontWeight: '400'
    lineHeight: 1.25rem
    letterSpacing: 0.01em
  label-code:
    fontFamily: JetBrains Mono
    fontSize: 0.75rem
    fontWeight: '500'
    lineHeight: 1rem
    letterSpacing: 0.08em
  label-price:
    fontFamily: JetBrains Mono
    fontSize: 1.125rem
    fontWeight: '600'
    lineHeight: 1.25rem
    letterSpacing: 0.02em
  label-badge:
    fontFamily: JetBrains Mono
    fontSize: 0.6875rem
    fontWeight: '500'
    lineHeight: 0.875rem
    letterSpacing: 0.12em
spacing:
  gutter: 1.5rem
  gutter-mobile: 1rem
  margin: 4rem
  margin-mobile: 1.25rem
  space-xs: 0.25rem
  space-sm: 0.5rem
  space-md: 1rem
  space-lg: 2rem
  space-xl: 3.5rem
---

## Brand & Style

This design system embodies the tension between high-fashion couture publishing and high-precision personal sourcing. Engineered for private clients, collectors, and luxury connoisseurs, the aesthetic discards generic e-commerce conventions in favor of a cinematic, editorial digital catalogue. 

The visual style blends **High-Contrast Editorial Minimalism** with structural **Architectural Precision**:
- Sharp, uncompromising zero-radius corners establish an uncompromising haute-couture presence.
- Expansive, gallery-scale negative space allows archival imagery and bespoke garments to breathe.
- Hairline architectural gridlines replace drop shadows and pill containers, elevating each layout into a museum-grade archival ledger.
- Monospaced serial tags, inventory IDs, and provenance stamps juxtapose against towering, condensed editorial headlines to evoke the bespoke exclusivity of an elite Parisian showroom vault.

## Colors

The palette draws directly from royal chromatic tradition, reimagined with contemporary digital vibrancy:

- **Primary Royal Purple (`#5426A8`)**: Used for primary brand moments, interactive accents, focal button fills, and signature typography.
- **Deep Midnight Purple (`#32145E`)**: Anchors hairline structural borders (`rgba(50, 20, 94, 0.16)`), structural header backgrounds, and deep typographic contrasts.
- **Electric Violet Accent (`#7950D9`)**: A surgical accent utilized sparingly for live availability pings, focused interactive states, and verified acquisition markers.
- **Dark Ink (`#20182B`)**: The foundation for body typography, metadata labels, and high-contrast structural dividing rules.
- **Canvas Neutrals (`#FAF9FC` Off-White, `#FFFFFF` Gallery White)**: Serve as clean, expansive gallery backdrops, punctuated by `#F0E9FF` (Soft Lavender) for hovered rows and highlight containers.
- **Muted Text (`#777080`)**: Reserved for collection serial numbers, curation dates, and subtle specifications.

## Typography

The typography structure establishes a rigorous editorial hierarchy:

- **Editorial Display (`Anton`)**: Renders all main titles, campaign themes, and drop names in condensed, commanding uppercase letterforms reminiscent of haute-couture print mastheads.
- **Editorial Body (`Inter`)**: Neutral, unobtrusive, and highly legible. It carries narrative descriptions, provenance summaries, and curator essays without competing with the imagery.
- **Provenance & Sourcing Spec (`JetBrains Mono`)**: Treats every product price, SKU, vault code, lot reference, and dimension as an authenticated specimen mark. All prices, technical materials, and live inventory statistics must appear in this monospaced voice.

## Layout & Spacing

The layout is grounded in a strict 12-column architectural grid inspired by broadsheet editorial publications:

- **Desktop (1440px+)**: 12 columns with generous `4rem` outer canvas margins and `1.5rem` gutters. Product spreads are framed inside structured hairline borders rather than floating bubbles.
- **Tablet (768px - 1024px)**: 6 columns with `2.5rem` margins and `1.25rem` gutters.
- **Mobile (< 768px)**: 4 columns with `1.25rem` margins and `1rem` gutters. Catalogue listings stack seamlessly with full-bleed imagery framed by continuous 1px bottom divider rules.

Whitespace is deliberate, airy, and rhythmic. Vertical section margins use `space-xl` and larger increments to maintain the expansive stillness typical of luxury physical catalogues.

## Elevation & Depth

This design system explicitly rejects drop shadows, skeuomorphic blur stacks, and multi-tier floating elevations. Depth is articulated purely through:

1. **Hairline Structural Borders**: Every boundary is marked with a 1px solid rule using `rgba(50, 20, 94, 0.16)`. In dark contextual panels, this transitions to `rgba(240, 233, 255, 0.12)`.
2. **Surface Inversion**: Modals, drawer overlays, and concierge panels slide in as crisp, opaque planes (`#FAF9FC` or `#20182B`) flanked by a 1px boundary line.
3. **Tinted Plateaus**: Hover states and selected items transition smoothly to `#F0E9FF` at 40–70% opacity, providing visual feedback through tonal presence rather than vertical lift.

## Shapes

The shape vocabulary is strictly geometric and razor-sharp (`0px` corner radius throughout):

- Buttons, image frames, badges, inputs, filter dropdowns, and cards maintain completely square corners.
- Images never use soft rounded corners; they sit edge-to-edge within their hairline grid cell boundaries.
- Badges and tags are rendered as rectangular, stamped architectural tags.

## Components

### Buttons
- **Primary Sourcing CTA**: Flat `#5426A8` background with `#FFFFFF` uppercase Anton or Inter Medium text, 0px radius, 14px vertical and 28px horizontal padding. On hover, background shifts to `#32145E`.
- **Secondary / Catalogue Action**: Transparent background with 1px hairline border `rgba(50, 20, 94, 0.25)` and Dark Ink `#20182B` label text. On hover, transitions to solid `#F0E9FF`.
- **Text Link CTA**: Monospace uppercase text with an arrow glyph (`REQUEST ACQUISITION ->`), featuring a persistent 1px underline offset by 4px.

### Product Catalogue Cards
- **Structure**: Zero shadow, zero curved radius. Wrapped entirely in a hairline border `rgba(50, 20, 94, 0.16)`.
- **Image Area**: High-aspect ratio (3:4 or 4:5), sitting directly atop the card boundary with no internal container padding.
- **Metadata Pane**: Separated by an internal 1px horizontal hairline. Displays the Brand/Provenance in `label-badge` uppercase, the Piece Title in `body-md` regular, and the Valuation/Price in `label-price` monospace.

### Badges & Status Markers
- **Archival Tags**: Small rectangular containers with 1px border `rgba(50, 20, 94, 0.2)`, `#FFFFFF` background, and uppercase `JetBrains Mono` text (`LOT NO. 042`, `BESPOKE ORDER`).
- **Availability Pip**: A crisp 6px square (not circle) in Electric Violet `#7950D9`.

### Input Fields & Selectors
- **Sourcing Inquiries & Forms**: Clean 1px bottom border or crisp 4-sided hairline boxes in `#20182B` at 20% opacity. Zero corner radius. Floating labels in `Inter` transitioning into `JetBrains Mono` during active focus states.
- **Focus State**: Hairline border darkens to `#5426A8` with zero glow/shadow.

### Checkboxes & Filters
- **Controls**: Square 14px x 14px bounding box with 1px solid `#32145E` border. When checked, filled with solid Royal Purple `#5426A8` displaying an austere white square indicator or minimal check mark.

### Private Concierge Drawer
- **Drawer Panel**: Full-height sidebar with a crisp left hairline border. Features an editorial header, client advisor metadata, and a direct inquiry stream set against an off-white `#FAF9FC` surface.