<?php
/**
 * Master Header Template (Slim Modular Controller)
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}
?><!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
  <meta charset="<?php bloginfo('charset'); ?>">
  <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0">
  <link rel="profile" href="https://gmpg.org/xfn/11">
  <?php wp_head(); ?>
</head>

<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<div id="page" class="site-wrapper">
  <a class="skip-link screen-reader-text" href="#primary"><?php esc_html_e('সরাসরি কনটেন্টে যান', 'helptrickbd-edu'); ?></a>

  <?php
  // 1. Top Dateline & Font Resizer Bar
  get_template_part('template-parts/header/topbar');

  // 2. Grand Serif Newspaper Masthead
  get_template_part('template-parts/header/masthead');

  // 3. Sticky Newspaper Navigation & Category Track
  get_template_part('template-parts/header/navbar');
  ?>

  <main id="primary" class="site-main">
