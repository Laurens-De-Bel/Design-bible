// Auto-sizes any <iframe class="calc-iframe"> to match its content's
// actual height, so there's neither a scrollbar nor leftover whitespace
// below it - used for the stlite calculator embeds, whose height changes
// as the user interacts with them (e.g. the "Stairs" fields appearing).
//
// Registered via document$ (a Material-for-MkDocs observable that fires
// on every page load, including instant-navigation swaps) rather than a
// plain inline <script> in the markdown content, because scripts
// inserted via the DOM-patching instant navigation uses don't
// auto-execute the way a real page load would.
document$.subscribe(function () {
  document.querySelectorAll("iframe.calc-iframe").forEach(function (iframe) {
    function target() {
      // Streamlit's own root container is position: fixed internally, so
      // it's taken out of normal document flow - document.body never
      // sees its content and reports scrollHeight 0 regardless of how
      // tall the app actually is. Measure Streamlit's own main content
      // container instead (falling back to body for any non-Streamlit
      // page that might reuse this class).
      var doc = iframe.contentDocument;
      return doc.querySelector('[data-testid="stMain"]') || doc.body;
    }

    function resize() {
      try {
        iframe.style.height = target().scrollHeight + "px";
      } catch (e) {
        // Cross-origin (shouldn't happen here) or not loaded yet.
      }
    }

    iframe.addEventListener("load", function () {
      resize();
      new ResizeObserver(resize).observe(target());
    });
  });
});
