/**
 * Fantasy Grounds 5E — Tiered health bar colors
 * Campaign option: Combat → Health bar colors → Tiered
 *
 * Remaining HP / Max:
 *   ≥ 75%  dark green   (fg-hp-full)
 *   < 75%  light green  (fg-hp-high)
 *   < 50%  yellow       (fg-hp-mid)
 *   < 25%  orange       (fg-hp-low)
 *   = 0    red          (fg-hp-critical)
 *
 * Opt-in: only pages that call FgHpTiered.bind(...) get this paint.
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

  function paint(input, current, maxHp) {
    if (!input || !maxHp || maxHp <= 0) return;
    var n = current;
    if (isNaN(n) || n < 0) n = 0;
    if (n > maxHp) n = maxHp;

    var ratio = n / maxHp;
    var next = "fg-hp-full";
    if (n <= 0) next = "fg-hp-critical";
    else if (ratio < 0.25) next = "fg-hp-low";
    else if (ratio < 0.5) next = "fg-hp-mid";
    else if (ratio < 0.75) next = "fg-hp-high";
    else next = "fg-hp-full";

    for (var i = 0; i < CLASSES.length; i++) {
      input.classList.toggle(CLASSES[i], CLASSES[i] === next);
    }
    input.classList.remove("is-zero");
  }

  /**
   * @param {HTMLElement} root  [data-ccs-hp] with data-hp-max
   * @param {HTMLInputElement} input  .ccs-hp-current
   */
  function bind(root, input) {
    if (!root || !input) return;
    var maxHp = parseInt(root.getAttribute("data-hp-max"), 10);
    if (isNaN(maxHp) || maxHp <= 0) {
      maxHp = parseInt(input.max, 10) || 1;
    }

    function apply() {
      var n = parseInt(input.value, 10);
      if (isNaN(n)) n = maxHp;
      paint(input, n, maxHp);
    }

    input.addEventListener("input", apply);
    input.addEventListener("change", apply);
    apply();
  }

  /** Bind every [data-ccs-hp][data-fg-hp-tiered] on the page */
  function bindAll() {
    document.querySelectorAll("[data-ccs-hp][data-fg-hp-tiered]").forEach(function (root) {
      bind(root, root.querySelector(".ccs-hp-current"));
    });
  }

  global.FgHpTiered = {
    paint: paint,
    bind: bind,
    bindAll: bindAll
  };
})(typeof window !== "undefined" ? window : this);
