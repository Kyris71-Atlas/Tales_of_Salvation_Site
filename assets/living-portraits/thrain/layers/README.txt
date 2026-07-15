Phase 1: composite.jpg is the approved master still (full stage).

Phase 2+: drop production cut layers here with names matching config.json:
  background.png, body.png, cape.png, beard.png, hair.png,
  eyes.png, eyebrows.png, mouth.png, hand.png, hammer.png,
  rug.png, props.png

Then set each layer's "src" and "ready": true in ../config.json
and set composite ready false (or leave as fallback).
