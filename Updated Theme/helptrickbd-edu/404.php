<?php
/**
 * Custom 404 Error Page Template
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<div class="ht-container">
  <nav class="ht-breadcrumb" aria-label="<?php esc_attr_e('Breadcrumbs', 'helptrickbd-edu'); ?>">
    <a href="<?php echo esc_url(home_url('/')); ?>"><?php esc_html_e('Home', 'helptrickbd-edu'); ?></a>
    <span aria-hidden="true"> › </span>
    <span aria-current="page"><?php esc_html_e('404 Not Found', 'helptrickbd-edu'); ?></span>
  </nav>

  <div class="ht-404-wrap" style="max-width: 680px; margin: 48px auto; text-align: center; padding: 32px 16px;">
    <div class="ht-404-badge" style="font-size: 5rem; font-family: var(--ht-font-serif); font-weight: 900; color: var(--ht-accent); line-height: 1;">
      404
    </div>
    
    <h1 style="font-family: var(--ht-font-serif); font-size: 1.8rem; margin: 16px 0 10px;">
      <?php esc_html_e('Page Not Found', 'helptrickbd-edu'); ?>
    </h1>
    
    <p style="color: var(--ht-text-muted); font-size: 1.0625rem; margin-bottom: 24px;">
      <?php esc_html_e('The page you are looking for might have been removed, had its name changed, or is temporarily unavailable. Try searching below or return to the homepage.', 'helptrickbd-edu'); ?>
    </p>

    <div style="margin-bottom: 32px;">
      <form role="search" method="get" action="<?php echo esc_url(home_url('/')); ?>" style="display: flex; gap: 8px; justify-content: center;">
        <input type="search" name="s" placeholder="<?php esc_attr_e('Search articles, notes...', 'helptrickbd-edu'); ?>" style="padding: 10px 16px; border: 1px solid var(--ht-border); border-radius: var(--ht-radius-md); font-family: inherit; font-size: 1rem; width: 100%; max-width: 380px;">
        <button type="submit" class="ht-btn ht-btn-primary"><?php esc_html_e('Search', 'helptrickbd-edu'); ?></button>
      </form>
    </div>

    <div style="border-top: 1px solid var(--ht-border); padding-top: 24px;">
      <a href="<?php echo esc_url(home_url('/')); ?>" class="ht-btn" style="border: 1px solid var(--ht-rule);">
        &larr; <?php esc_html_e('Back to Home', 'helptrickbd-edu'); ?>
      </a>
    </div>
  </div>
</div>

<?php
get_footer();
