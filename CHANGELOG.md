# Changelog

All notable changes to this project will be documented in this file.

## [1.8.5-eo] - Unreleased

### Changed
- Version bump to 1.8.5-eo.
- **RM_CLAMP color mapping**: `clamp_improved_lut.py` now uses sRGB-space nearest-neighbor matching instead of TMDS-space weighted L2. Phase-invariant mapping (i and i^0x100 share the same output) eliminates striations in solid color bars.

### Added
- `tools/generate_clamp_reference.py` — generates colorized reference image (`assets/clamp_reference_expected.png`) for RM_CLAMP comparison, using Apple II LORES palette sRGB values.

## [1.8.4-eo] - Unreleased

### Changed
- **A2C RM_CLAMP color mode** (fix): RM_CLAMP now uses a precomputed R/G/B LUT (`clamp_improved_red/green/blue[512]`) instead of the previous two-stage lookup. All lookups are in RAM (same cost as original 8to3 path); flash reads removed to fix frame timing.
  - Weighted L2 mapping from original CLAMP LUT to improved IIgs LORES palette.
  - Regeneration tool: `tools/clamp_improved_lut.py`.
