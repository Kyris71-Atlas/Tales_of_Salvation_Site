Animation modules (phase 2) — one behavior at a time.

Suggested folders:
  idle/
  storytelling/
  smile/
  thinking/
  hammer/
  rug/

Frame files e.g. idle/01.jpg … idle/08.jpg

Then in config.json:
  "modules": {
    "idle": {
      "ready": true,
      "frames": ["modules/idle/01.jpg", "modules/idle/02.jpg", ...],
      "frameDurationMs": 400,
      "loop": true
    }
  }

Scheduler will start cycling when any module is ready.
