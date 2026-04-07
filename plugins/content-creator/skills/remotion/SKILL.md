---
name: remotion-video
description: Create and render short videos with code. Scaffolds a Remotion project, writes the composition, installs dependencies, and renders to MP4 automatically. Say "make a video", "create a video", "animate this", "remotion", "render a video", "video for LinkedIn", "video for social".
user-invocable: false
---

# Remotion Video Creator

Build and render short videos entirely from code. The user describes what they want — you scaffold, write, and render. No manual terminal commands needed.

## Before You Start

Read the relevant rule files from `rules/` for domain-specific patterns:

| Topic | File |
|-------|------|
| Compositions & structure | `rules/compositions.md` |
| Animation fundamentals | `rules/animations.md` |
| Timing & easing | `rules/timing.md` |
| Text animations | `rules/text-animations.md` |
| Transitions | `rules/transitions.md` |
| Sequencing | `rules/sequencing.md` |
| Images | `rules/images.md` |
| Video embedding | `rules/videos.md` |
| Audio & sound | `rules/audio.md` |
| Fonts | `rules/fonts.md` |
| Tailwind | `rules/tailwind.md` |
| Captions | `rules/display-captions.md` |
| Charts | `rules/charts.md` |
| 3D content | `rules/3d.md` |
| GIFs | `rules/gifs.md` |
| Lottie | `rules/lottie.md` |
| Parameters | `rules/parameters.md` |
| Maps | `rules/maps.md` |

Only read the ones relevant to the video you're building. Don't load all 30+ files.

## Workflow

### Step 1: Clarify the Video

Ask (or pull from context):
- **What's in the video?** — text, images, data, talking head, etc.
- **Platform?** — LinkedIn (1080x1080 or 1920x1080), Instagram Reels (1080x1920), YouTube (1920x1080), Twitter (1280x720)
- **Duration?** — default to 15-30 seconds for social
- **Style?** — minimal, bold, kinetic typography, data viz, etc.

If the user gives a one-liner like "make a video about X", pick sensible defaults and move.

### Step 2: Scaffold the Project

**IMPORTANT — Cowork permission workaround:** The mounted workspace (`/sessions/*/mnt/`) has restricted permissions that break Remotion's browser download (can't unlink temp files). Always scaffold and render in the session temp space, then copy output back.

```bash
# Build in temp space — NOT the mounted workspace
PROJECT_DIR="/tmp/video-project"
mkdir -p "$PROJECT_DIR" && cd "$PROJECT_DIR"
npm init -y
npm install --save-exact remotion @remotion/cli @remotion/bundler react react-dom
```

If Tailwind is needed:
```bash
cd "$PROJECT_DIR" && npm install -D tailwindcss@3 postcss autoprefixer
```

Create the minimum file structure:
```
/tmp/video-project/
  src/
    Root.tsx          # RemotionRoot with Composition(s)
    Video.tsx         # Main composition component
    components/       # Reusable pieces (text blocks, transitions)
  public/             # Static assets (images, fonts)
  remotion.config.ts  # Remotion config
  tsconfig.json
  package.json
```

### Step 3: Write the Composition

Build the video component following these rules (from the rule files):

- **All animation driven by `useCurrentFrame()` + `interpolate()`** — never CSS animations
- **Write timing in seconds**, multiply by `fps` from `useVideoConfig()`
- **Use `<Sequence>` for ordering** — `from` prop for delay, `durationInFrames` for length
- **Use `<AbsoluteFill>`** as the base layout container
- **Clamp interpolations** — always set `extrapolateRight: 'clamp'`
- **`staticFile()` for assets** in the `public/` folder

### Step 4: Ensure Browser

Remotion needs a browser to render. Install it in temp space where permissions allow:

```bash
cd "$PROJECT_DIR" && npx remotion browser ensure
```

If `ensure` fails, try setting a writable cache dir:
```bash
export REMOTION_BROWSER_CACHE_DIR="/tmp/remotion-browser"
mkdir -p "$REMOTION_BROWSER_CACHE_DIR"
npx remotion browser ensure
```

### Step 5: Render

```bash
cd "$PROJECT_DIR" && npx remotion render src/Root.tsx VideoComposition out/video.mp4 --concurrency 50%
```

Common render flags:
- `--codec h264` (default, best compatibility)
- `--image-format jpeg` (faster) or `png` (transparency)
- `--scale 1` (default)
- `--concurrency 50%` (safe default for limited environments)

### Step 6: Copy Output to Workspace

After successful render, copy the MP4 back to the mounted workspace so the user can access it:

```bash
# Find the workspace mount path
WORKSPACE=$(find /sessions -maxdepth 2 -name "mnt" -type d 2>/dev/null | head -1)
cp "$PROJECT_DIR/out/video.mp4" "$WORKSPACE/video.mp4"
echo "Video saved to workspace: video.mp4"
```

If the workspace path isn't found, check the current working directory:
```bash
cp "$PROJECT_DIR/out/video.mp4" ./video.mp4
```

### Step 7: Deliver

- Tell the user the video is in their workspace
- Offer to adjust duration, colors, text, or timing
- If they want a different format/size, re-render with updated dimensions in `$PROJECT_DIR`

## Key Rules (Always Follow)

1. **Never use CSS transitions or Tailwind animation classes** — they won't render
2. **Never use `setTimeout`, `setInterval`, or `requestAnimationFrame`** — use frame math
3. **Always use `React.FC` with typed props** for compositions
4. **Pin Tailwind to v3** if using it — v4 has incompatible config syntax
5. **Every `<Composition>` needs `id`, `component`, `width`, `height`, `fps`, `durationInFrames`**
6. **Use `@remotion/transitions` for scene transitions** — not manual opacity/position hacks

## Full Rules Reference

For deep dives on specific topics, read from `rules/`:

- [3d.md](rules/3d.md) - Three.js and React Three Fiber
- [animations.md](rules/animations.md) - Animation fundamentals
- [assets.md](rules/assets.md) - Importing images, videos, audio, fonts
- [audio.md](rules/audio.md) - Sound — importing, trimming, volume, speed, pitch
- [calculate-metadata.md](rules/calculate-metadata.md) - Dynamic composition metadata
- [can-decode.md](rules/can-decode.md) - Video decode checking with Mediabunny
- [charts.md](rules/charts.md) - Data visualization
- [compositions.md](rules/compositions.md) - Compositions, stills, folders, props
- [display-captions.md](rules/display-captions.md) - TikTok-style captions
- [extract-frames.md](rules/extract-frames.md) - Frame extraction from videos
- [fonts.md](rules/fonts.md) - Google Fonts and local fonts
- [get-audio-duration.md](rules/get-audio-duration.md) - Audio duration with Mediabunny
- [get-video-dimensions.md](rules/get-video-dimensions.md) - Video dimensions
- [get-video-duration.md](rules/get-video-duration.md) - Video duration
- [gifs.md](rules/gifs.md) - GIF playback synced to timeline
- [images.md](rules/images.md) - Img component
- [import-srt-captions.md](rules/import-srt-captions.md) - SRT subtitle import
- [lottie.md](rules/lottie.md) - Lottie animations
- [maps.md](rules/maps.md) - Mapbox maps
- [measuring-dom-nodes.md](rules/measuring-dom-nodes.md) - DOM measurement
- [measuring-text.md](rules/measuring-text.md) - Text measurement and fitting
- [parameters.md](rules/parameters.md) - Parametrizable videos with Zod
- [sequencing.md](rules/sequencing.md) - Delay, trim, duration limiting
- [tailwind.md](rules/tailwind.md) - TailwindCSS setup
- [text-animations.md](rules/text-animations.md) - Typography animations
- [timing.md](rules/timing.md) - Interpolation, easing, spring
- [transcribe-captions.md](rules/transcribe-captions.md) - Audio transcription
- [transitions.md](rules/transitions.md) - Scene transitions
- [transparent-videos.md](rules/transparent-videos.md) - Transparent video rendering
- [trimming.md](rules/trimming.md) - Trimming animations
- [videos.md](rules/videos.md) - Video embedding and manipulation
