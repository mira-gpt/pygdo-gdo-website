from gdo.base.Method import Method
from gdo.message.GDT_HTML import GDT_HTML


class overview(Method):
    """A public introduction to GDO."""

    def gdo_execute(self):
        return GDT_HTML().html('''
<main class="gdo-home">
  <section class="gdo-hero" aria-labelledby="gdo-title">
    <div><p class="gdo-eyebrow"><span class="gdo-indicator"></span> THE GDO PROJECT</p>
      <h1 id="gdo-title">Build things<br><em>that connect.</em></h1>
      <p class="gdo-lead">A modular foundation for websites, applications and bots. Build your own corner of the internet, one module at a time.</p>
      <div class="gdo-actions"><a class="gdo-button" href="https://github.com/gizmore/pygdo">Explore PyGDO ↗</a><a class="gdo-secondary" href="#how-it-works">See how it works ↓</a></div>
    </div>
    <div class="gdo-diagram" aria-label="GDO connecting modules, websites and bots">
      <div class="gdo-diagram-top"><span>GDO / SYSTEM OVERVIEW</span><span>● ● ●</span></div>
      <div class="gdo-orbit"><span class="gdo-node gdo-node-a">MODULES</span><span class="gdo-node gdo-node-b">WEBSITES</span><span class="gdo-node gdo-node-c">BOTS</span><strong class="gdo-center">GDO<span>ONE FOUNDATION</span></strong></div>
      <div class="gdo-diagram-top"><span>MADE TO CONNECT</span><span>01 / ∞</span></div>
    </div>
  </section>
  <section id="how-it-works" class="gdo-section">
    <div class="gdo-section-intro"><p class="gdo-eyebrow">01 / THE IDEA</p><h2>Start with the core.<br><em>Make it yours.</em></h2><p>GDO brings reusable building blocks together so a project can grow in its own direction.</p></div>
    <div class="gdo-steps"><article><span>01</span><h3>Choose a foundation</h3><p>PyGDO is the Python reference implementation of GDO.</p></article><article><span>02</span><h3>Add modules</h3><p>Bring in the capabilities your project needs and leave the rest behind.</p></article><article><span>03</span><h3>Make connections</h3><p>Build experiences for the web and chat around a common application.</p></article></div>
  </section>
  <section class="gdo-section gdo-license"><div><p class="gdo-eyebrow">02 / WHAT’S NEXT</p><h2>Room to grow.</h2></div><div><p>We plan to offer licenses for various modules in the future. Details and availability will be announced when they are ready.</p><a class="gdo-secondary" href="https://github.com/gizmore/pygdo/tree/main/DOCS">Read the documentation ↗</a></div></section>
  <footer class="gdo-footer"><strong>GDO<span>.</span></strong><span>Build, connect, create.</span><a href="https://github.com/gizmore/pygdo">GitHub ↗</a></footer>
</main>''')
