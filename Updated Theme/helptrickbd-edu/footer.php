<?php
/**
 * Master Footer Template (Slim Modular Controller)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?>
  </main><!-- #primary -->

  <footer class="ht-footer">
    <div class="ht-container">
      <?php
      // 1. Footer 4-Column Academic Widgets
      get_template_part('template-parts/footer/footer-widgets');

      // 2. Footer Copyright & Disclaimer Bar
      get_template_part('template-parts/footer/copyright-bar');
      ?>
    </div>
  </footer>

  <?php
  // 3. Fast Fullscreen Search Modal Overlay (Ctrl+K)
  get_template_part('template-parts/footer/search-modal');

  // 4. Mobile Off-Canvas Drawer Navigation
  get_template_part('template-parts/footer/mobile-drawer');

  // WordPress Core Footer Hook
  wp_footer();
  ?>
</div><!-- #page -->
</body>
</html>
