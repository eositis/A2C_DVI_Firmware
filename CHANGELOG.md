# Changelog

All notable changes to this project will be documented in this file.

## [1.8.4-eo] - Unreleased

### Changed
- **A2C RM_CLAMP color mode**: RM_CLAMP now uses the improved IIgs LORES palette (`tmds_lores_improved`) instead of the original 9-bit clamped LUT. Colors in CLAMP mode now match the slot-based A2DVI "Improved (IIGS/IIE)" color style.
  - Added `clamp_to_improved_index[512]` mapping table (9-bit dot pattern → improved palette index).
  - RM_CLAMP lookup path remaps through `tmds_lores_improved` for R/G/B output.
  - Regeneration tool: `tools/clamp_to_improved_lut.py`.

### Added
- `tools/clamp_to_improved_lut.py` — script to regenerate the CLAMP → improved IIgs index mapping from the 9-bit LUT and improved palette.
