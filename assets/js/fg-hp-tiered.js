/**
 * Fantasy Grounds 5E — Tiered health bar colors
 * Campaign option: Combat → Health bar colors → Tiered
 *
 * FG tracks WOUNDS (damage taken), not “current HP remaining.”
 *   wounds = 0     → full health → dark green
 *   wounds high    → near death → red
 *
 * Same tier edges as remaining-HP mode, inverted:
 *   wounds / max ≤ 25%  dark green   (fg-hp-full)   ≈ remaining ≥ 75%
 *   wounds / max ≤ 50%  light green  (fg-hp-high)   ≈ remaining ≥ 50%
 *   wounds / max ≤ 75%  yellow       (fg-hp-mid)    ≈ remaining ≥ 25%
 *   wounds / max < 100% orange       (fg-hp-low)    ≈ remaining > 0%
 *   wounds ≥ max        red          (fg-hp-critical)
 *
 * Sol 123 max examples: 0–30 green · 31–61 light · 62–92 yellow · 93–122 orange · 123 red
 * Portia 143 max:       0–35 green · 36–71 light · 72–107 yellow · 108–142 orange · 143 red
 */
(function (global) {
  "use strict";

  var CLASSES = [
    "fg-hp-full",
    "fg-hp-high",
    "fg-hp-mid",
    "fg-hp-low",
    "fg-hp-critical"
  ];

  /**
   * @param {HTMLElement} input
   * @param {number} wounds  damage taken (FG wounds field)
   * @param {number} maxHp
   */
  function paint(input, wounds, maxHp) {
    if (!input || !maxHp || maxHp <= 0) return;
    var w = wounds;
    if (isNaN(w) || w < 0) w = 0;
    if (w > maxHp) w = maxHp;

    var wounded = w / maxHp;
    var next = "fg-hp-full";
    if (w >= maxHp) next = "fg-hp-critical";
    else if (wounded >= 0.75) next = "fg-hp-low";
    else if (wounded >= 0.5) next = "fg-hp-mid";
    else if (wounded >= 0.25) next = "fg-hp-high";
    else next = "fg-hp-full";

    for (var i = 0; i < CLASSES.length; i++) {
      input.classList.toggle(CLASSES[i], CLASSES[i] === next);
    }
    input.classList.remove("is-zero");
  }

  /** Tier class name for a wounds value (e.g. Portia weapon outlines) */
  function tierClass(wounds, maxHp) {
    var w = wounds;
    if (isNaN(w) || w < 0) w = 0;
    if (w > maxHp) w = maxHp;
    var wounded = w / maxHp;
    if (w >= maxHp) return "fg-hp-critical";
    if (wounded >= 0.75) return "fg-hp-low";
    if (wounded >= 0.5) return "fg-hp-mid";
    if (wounded >= 0.25) return "fg-hp-high";
    return "fg-hp-full";
  }

  function bind(root, input) {
    if (!root || !input) return;
    var maxHp = parseInt(root.getAttribute("data-hp-max"), 10);
    if (isNaN(maxHp) || maxHp <= 0) {
      maxHp = parseInt(input.max, 10) || 1;
    }

    function apply() {
      var n = parseInt(input.value, 10);
      if (isNaN(n)) n = 0;
      paint(input, n, maxHp);
    }

    input.addEventListener("input", apply);
    input.addEventListener("change", apply);
    apply();
  }

  function bindAll() {
    document.querySelectorAll("[data-ccs-hp][data-fg-hp-tiered]").forEach(function (root) {
      bind(root, root.querySelector(".ccs-hp-current"));
    });
  }

  global.FgHpTiered = {
    paint: paint,
    tierClass: tierClass,
    bind: bind,
    bindAll: bindAll
  };
})(typeof window !== "undefined" ? window : this);
