/**
 * Living Portrait v1.0
 * ------------------------
 * A stage. The character waits. Modules (blink, talk, rug…) happen on the stage.
 * The scheduler does not know character names — only config + asset paths.
 *
 * Phase 1: show approved composite master.
 * Phase 2: modules with frame lists plug in; schedule cycles behaviors.
 */
(function () {
  "use strict";

  var BASE = "../assets/living-portraits/";

  function resolveBase(el) {
    var custom = el.getAttribute("data-base");
    if (custom) return custom.replace(/\/?$/, "/");
    // default relative to page under forge-of-fury/
    return BASE;
  }

  function defaultConfig(characterId, compositeUrl) {
    return {
      id: characterId,
      displayName: characterId.charAt(0).toUpperCase() + characterId.slice(1),
      stage: { sizePx: 220 },
      layers: [
        {
          id: "composite",
          z: 5,
          src: compositeUrl || "layers/composite.jpg",
          ready: true,
          phase1Base: true
        }
      ],
      modules: {},
      schedule: ["idle"],
      phase: 1
    };
  }

  function loadConfig(base, characterId, el) {
    // 1) Embedded config (config.js) — works on file:// and GitHub Pages
    if (
      window.LivingPortraitConfigs &&
      window.LivingPortraitConfigs[characterId]
    ) {
      return Promise.resolve(
        JSON.parse(JSON.stringify(window.LivingPortraitConfigs[characterId]))
      );
    }

    // 2) fetch config.json (http/https servers)
    var url = base + characterId + "/config.json";
    return fetch(url, { cache: "no-cache" })
      .then(function (r) {
        if (!r.ok) throw new Error("config http " + r.status);
        return r.json();
      })
      .catch(function () {
        // 3) last resort: still show composite only
        var composite =
          el.getAttribute("data-composite") ||
          base + characterId + "/layers/composite.jpg";
        var cfg = defaultConfig(characterId, null);
        cfg.layers[0].src = null;
        cfg.layers[0]._absolute = composite;
        return cfg;
      });
  }

  function layerUrl(base, characterId, src, layer) {
    if (layer && layer._absolute) return layer._absolute;
    if (!src) return null;
    if (
      /^https?:\/\//i.test(src) ||
      src.charAt(0) === "/" ||
      src.indexOf("..") === 0 ||
      src.indexOf("assets/") === 0
    )
      return src;
    return base + characterId + "/" + src.replace(/^\//, "");
  }

  function buildStage(el, config, base) {
    var size = el.getAttribute("data-size") || String(config.stage && config.stage.sizePx) || "220";
    el.setAttribute("data-size", size);
    el.classList.add("living-portrait");
    el.setAttribute("data-character", config.id);
    el.setAttribute("role", "img");
    el.setAttribute(
      "aria-label",
      (config.displayName || config.id) + " living portrait"
    );

    var stage = document.createElement("div");
    stage.className = "lp-stage";

    var layers = (config.layers || []).slice().sort(function (a, b) {
      return (a.z || 0) - (b.z || 0);
    });

    layers.forEach(function (layer) {
      var div = document.createElement("div");
      div.className = "lp-layer";
      div.setAttribute("data-layer", layer.id);
      div.style.zIndex = String(layer.z || 0);
      var url = layerUrl(base, config.id, layer.src, layer);
      if (url && layer.ready !== false) {
        div.style.backgroundImage = 'url("' + url + '")';
        div.classList.add("is-ready");
      }
      stage.appendChild(div);
    });

    // Module frame host (phase 2)
    var mod = document.createElement("div");
    mod.className = "lp-module-frame";
    mod.setAttribute("data-lp-module-frame", "1");
    stage.appendChild(mod);

    // Ambient host (phase 2)
    var amb = document.createElement("div");
    amb.className = "lp-ambient";
    amb.setAttribute("data-lp-ambient", "1");
    stage.appendChild(amb);

    el.innerHTML = "";
    el.appendChild(stage);

    return { stage: stage, moduleFrame: mod, ambient: amb };
  }

  /**
   * Behavior scheduler — character-agnostic.
   * Only runs modules that have ready frames. Otherwise holds still on composite.
   */
  function createScheduler(ui, config, base) {
    var timer = null;
    var schedule = config.schedule || ["idle"];
    var index = 0;
    var frameIndex = 0;
    var currentModule = null;

    function moduleDef(name) {
      return (config.modules && config.modules[name]) || null;
    }

    function clearTimer() {
      if (timer) {
        clearTimeout(timer);
        timer = null;
      }
    }

    function showCompositeOnly() {
      ui.moduleFrame.classList.remove("is-active");
      ui.moduleFrame.style.backgroundImage = "";
    }

    function playModule(name) {
      var mod = moduleDef(name);
      if (!mod || !mod.ready || !mod.frames || !mod.frames.length) {
        showCompositeOnly();
        return false;
      }
      currentModule = name;
      frameIndex = 0;
      stepFrame(mod);
      return true;
    }

    function stepFrame(mod) {
      clearTimer();
      var frames = mod.frames;
      if (!frames.length) {
        showCompositeOnly();
        return;
      }
      var frameSrc = frames[frameIndex % frames.length];
      var url = layerUrl(base, config.id, frameSrc);
      ui.moduleFrame.style.backgroundImage = 'url("' + url + '")';
      ui.moduleFrame.classList.add("is-active");
      frameIndex += 1;

      var duration = mod.frameDurationMs || 400;
      var doneCycle = frameIndex >= frames.length;

      if (doneCycle && !mod.loop) {
        timer = setTimeout(function () {
          showCompositeOnly();
          advanceSchedule();
        }, duration);
        return;
      }
      if (doneCycle && mod.loop) {
        frameIndex = 0;
        // Keep looping this module until schedule advances.
        // Single-module schedules (e.g. blink only) stay on stage forever.
        timer = setTimeout(function () {
          if (schedule.length <= 1) {
            stepFrame(mod);
            return;
          }
          if (!mod._loops) mod._loops = 0;
          mod._loops += 1;
          if (mod._loops >= 2) {
            mod._loops = 0;
            advanceSchedule();
          } else {
            stepFrame(mod);
          }
        }, duration);
        return;
      }
      timer = setTimeout(function () {
        stepFrame(mod);
      }, duration);
    }

    function advanceSchedule() {
      if (!schedule.length) {
        showCompositeOnly();
        return;
      }
      var attempts = 0;
      while (attempts < schedule.length) {
        var name = schedule[index % schedule.length];
        index += 1;
        attempts += 1;
        var mod = moduleDef(name);
        if (mod && mod.rare && Math.random() > 0.25) continue;
        if (playModule(name)) return;
      }
      showCompositeOnly();
      // retry later in case assets appear
      timer = setTimeout(advanceSchedule, 8000);
    }

    function start() {
      clearTimer();
      // Phase 1: no modules ready → stay on composite forever (stage waiting)
      var anyReady = Object.keys(config.modules || {}).some(function (k) {
        var m = config.modules[k];
        return m && m.ready && m.frames && m.frames.length;
      });
      if (!anyReady) {
        showCompositeOnly();
        return;
      }
      advanceSchedule();
    }

    function destroy() {
      clearTimer();
    }

    return { start: start, destroy: destroy, advanceSchedule: advanceSchedule };
  }

  function mount(el) {
    var characterId = el.getAttribute("data-character");
    if (!characterId) {
      console.warn("LivingPortrait: missing data-character");
      return;
    }
    var base = resolveBase(el);

    loadConfig(base, characterId, el).then(function (config) {
      var ui = buildStage(el, config, base);
      var scheduler = createScheduler(ui, config, base);
      el._livingPortrait = { config: config, scheduler: scheduler };
      scheduler.start();
    });
  }

  function init() {
    var nodes = document.querySelectorAll("[data-living-portrait]");
    nodes.forEach(mount);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  // Public hook for future pages
  window.LivingPortrait = { mount: mount, init: init };
})();
