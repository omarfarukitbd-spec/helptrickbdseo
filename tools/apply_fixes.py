import os, re, shutil

THEMES = [
    r'Updated Theme/helptrickbd-theme',
    r'Helptrickbd Wp/helptrickbd-theme'
]

VERSION = '1.5.3'

def apply_fixes():
    for base in THEMES:
        print(f'=== Applying fixes to {base} (v{VERSION}) ===')

        # 0. Bump Version in style.css and functions.php
        style_path = os.path.join(base, 'style.css')
        if os.path.exists(style_path):
            with open(style_path, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r'Version:\s*[\d\.]+', f'Version: {VERSION}', c)
            with open(style_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'  [OK] Bumped style.css to v{VERSION}')

        func_path = os.path.join(base, 'functions.php')
        if os.path.exists(func_path):
            with open(func_path, 'r', encoding='utf-8') as f:
                c = f.read()
            c = re.sub(r"define\('HT_THEME_VERSION',\s*'[^']+'\);", f"define('HT_THEME_VERSION', '{VERSION}');", c)
            with open(func_path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f'  [OK] Bumped functions.php to v{VERSION}')

        # 1. Fix htbd_reading_time in inc/template-tags.php (Fix Array bug)
        tt_path = os.path.join(base, 'inc', 'template-tags.php')
        if os.path.exists(tt_path):
            with open(tt_path, 'r', encoding='utf-8') as f:
                tt_content = f.read()
            
            pattern = r"function htbd_reading_time\(\$post_id = 0\) \{[\s\S]*?return '৩ মিনিট পড়া';\s*\}"
            replacement = """function htbd_reading_time($post_id = 0) {
        if (function_exists('ht_get_reading_time')) {
            $data = ht_get_reading_time($post_id);
            if (is_array($data) && isset($data['minutes'])) {
                return function_exists('ht_bn_number') ? ht_bn_number($data['minutes']) . ' মিনিট পড়া' : $data['minutes'] . ' min read';
            }
            if (is_string($data)) {
                return $data;
            }
        }
        return '৩ মিনিট পড়া';
    }"""
            tt_content, n = re.subn(pattern, replacement, tt_content)
            if n > 0:
                print(f'  [OK] Fixed htbd_reading_time in {tt_path}')
            else:
                print(f'  [WARN] htbd_reading_time regex match failed in {tt_path}')
            
            with open(tt_path, 'w', encoding='utf-8') as f:
                f.write(tt_content)

        # 2. Fix nu-cgpa-calculator.js (Fix btnResetYear ReferenceError)
        js_path = os.path.join(base, 'assets', 'js', 'nu-cgpa-calculator.js')
        if os.path.exists(js_path):
            with open(js_path, 'r', encoding='utf-8') as f:
                js_content = f.read()
            
            old_js_block = """  const btnToolbarReset = document.getElementById('ht-btn-toolbar-reset');
  if (btnToolbarReset && btnResetYear) {
    btnToolbarReset.addEventListener('click', () => {
      if (confirm('আপনি কি নিশ্চিত যে সকল হিসাব মুছে রিসেট করতে চান?')) {
        btnResetYear.click();
      }
    });
  }"""
            new_js_block = """  const btnToolbarReset = document.getElementById('ht-btn-toolbar-reset');
  const btnResetYear = document.getElementById('btn-reset-year');
  if (btnToolbarReset && btnResetYear) {
    btnToolbarReset.addEventListener('click', () => {
      if (confirm('আপনি কি নিশ্চিত যে সকল হিসাব মুছে রিসেট করতে চান?')) {
        btnResetYear.click();
      }
    });
  }"""
            if old_js_block in js_content:
                js_content = js_content.replace(old_js_block, new_js_block)
                print(f'  [OK] Fixed btnResetYear in {js_path}')
            else:
                js_content = js_content.replace("if (btnToolbarReset && btnResetYear)", "const btnResetYear = document.getElementById('btn-reset-year');\n  if (btnToolbarReset && btnResetYear)")
                print(f'  [OK] Replaced btnResetYear pattern in {js_path}')
            
            with open(js_path, 'w', encoding='utf-8') as f:
                f.write(js_content)

        # 3. Guard page-nu-cgpa-calculator.php with fail-safe try-catch
        cgpa_path = os.path.join(base, 'page-nu-cgpa-calculator.php')
        if os.path.exists(cgpa_path):
            with open(cgpa_path, 'r', encoding='utf-8') as f:
                cgpa_content = f.read()
            
            old_crumb = """        <!-- Breadcrumbs Navigation -->
        <?php
        if (function_exists('ht_breadcrumbs')) {
            ht_breadcrumbs();
        } elseif (function_exists('htbd_breadcrumbs')) {
            htbd_breadcrumbs();
        }
        ?>"""
            new_crumb = """        <!-- Breadcrumbs Navigation -->
        <?php
        try {
            if (function_exists('ht_breadcrumbs')) {
                ht_breadcrumbs();
            } elseif (function_exists('htbd_breadcrumbs')) {
                htbd_breadcrumbs();
            }
        } catch (\\Throwable $e) {
            // Fail-safe breadcrumbs
        }
        ?>"""
            if old_crumb in cgpa_content:
                cgpa_content = cgpa_content.replace(old_crumb, new_crumb)
                print(f'  [OK] Guarded breadcrumbs with try-catch in {cgpa_path}')

            old_post_loop = """        <!-- Optional WordPress Post Content Notice -->
        <?php
        if (have_posts()) :
            while (have_posts()) :
                the_post();
                $content = trim(get_the_content());
                if (!empty($content)) :
        ?>
            <div class="ht-cgpa-admin-banner">
                <?php the_content(); ?>
            </div>
        <?php
                endif;
            endwhile;
        endif;
        ?>"""
            new_post_loop = """        <!-- Optional WordPress Post Content Notice -->
        <?php
        try {
            if (have_posts()) :
                while (have_posts()) :
                    the_post();
                    $content = trim(get_the_content());
                    if (!empty($content)) :
            ?>
                <div class="ht-cgpa-admin-banner">
                    <?php the_content(); ?>
                </div>
            <?php
                    endif;
                endwhile;
            endif;
        } catch (\\Throwable $e) {
            // Fail-safe post loop
        }
        ?>"""
            if old_post_loop in cgpa_content:
                cgpa_content = cgpa_content.replace(old_post_loop, new_post_loop)
                print(f'  [OK] Guarded post loop with try-catch in {cgpa_path}')

            with open(cgpa_path, 'w', encoding='utf-8') as f:
                f.write(cgpa_content)

        # 4. Remove topbar from header.php
        hp_path = os.path.join(base, 'header.php')
        if os.path.exists(hp_path):
            with open(hp_path, 'r', encoding='utf-8') as f:
                hp_c = f.read()
            old_tb = """    // 1. Topbar / Dateline (Optional or sitewide)
    if (get_theme_mod('ht_topbar_enable', true)) {
        get_template_part('template-parts/header/topbar');
    }"""
            if old_tb in hp_c:
                hp_c = hp_c.replace(old_tb, '')
                with open(hp_path, 'w', encoding='utf-8') as f:
                    f.write(hp_c)
                print(f'  [OK] Removed topbar from {hp_path}')

        # 5. Trim front-page.php (Keep strictly 4 edu sections)
        fp_path = os.path.join(base, 'front-page.php')
        if os.path.exists(fp_path):
            new_fp = """<?php
/**
 * Master Homepage Controller (Slim Modular Architecture)
 * HelpTrickBD Pro - Newspaper & Educational Portal Hybrid
 * Strictly follows the final version of helptrickbd-edu layout:
 * 1. Breaking Notice Marquee Ticker
 * 2. Magazine Lead Hero Story & Spotlight Cards
 * 3. 3-Column Specialized Subject Cards Grid (Strict SSC & Dakhil)
 * 4. Main 2-Column Home Layout Grid:
 *    - Left: Subject-Based Filterable Posts (2 columns)
 *    - Right: Academic Sidebar (Trending 1-6, Stay Connected, Categories Grid)
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

get_header();
?>

<div class="ht-container">
  <?php
  // 1. Breaking Notice Marquee Ticker
  get_template_part('template-parts/home/section-ticker');

  // 2. Magazine Lead Hero Story & Spotlight Cards
  get_template_part('template-parts/home/section-lead-hero');

  // 3. 3-Column Specialized Subject Cards Grid (Strict SSC & Dakhil)
  get_template_part('template-parts/home/section-subject-grid');
  ?>

  <!-- 4. Subject-Based Filterable Posts & Academic Sidebar -->
  <div class="n-home-layout-grid">
    <div class="n-home-layout-main">
      <?php get_template_part('template-parts/home/section-filter-rows'); ?>
    </div>
    <aside class="n-home-layout-sidebar">
      <?php get_template_part('template-parts/home/sidebar-popular-cats'); ?>
    </aside>
  </div>
</div>

<?php
get_footer();
"""
            with open(fp_path, 'w', encoding='utf-8') as f:
                f.write(new_fp)
            print(f'  [OK] Cleaned front-page.php in {base}')

        # 6. Set exact .ht-container padding in main.css
        main_css_path = os.path.join(base, 'assets', 'css', 'main.css')
        if os.path.exists(main_css_path):
            with open(main_css_path, 'r', encoding='utf-8') as f:
                css = f.read()
            css = re.sub(
                r'\.ht-container\s*\{[^}]*max-width:[^}]*\}',
                '''.ht-container {
  width: 100%;
  max-width: var(--ht-max-width, 1240px);
  margin-left: auto;
  margin-right: auto;
  padding: 0 10px;
}
@media (min-width: 600px) {
  .ht-container {
    padding: 0 16px;
  }
}
@media (min-width: 768px) {
  .ht-container {
    padding: 0 24px;
  }
}''',
                css
            )
            with open(main_css_path, 'w', encoding='utf-8') as f:
                f.write(css)
            print(f'  [OK] Updated .ht-container padding in {main_css_path}')

        # 7. Add full bleed .n-ticker in home-sections.css
        home_css_path = os.path.join(base, 'assets', 'css', 'home-sections.css')
        if os.path.exists(home_css_path):
            with open(home_css_path, 'r', encoding='utf-8') as f:
                h_css = f.read()
            if 'margin: 0 -10px 12px;' not in h_css:
                ticker_fix = """@media (max-width: 600px) {
  .n-ticker {
    margin: 0 -10px 12px;
    width: calc(100% + 20px);
    border-radius: 0;
  }
}"""
                h_css += "\n" + ticker_fix + "\n"
                print(f'  [OK] Added .n-ticker full bleed to {home_css_path}')
            with open(home_css_path, 'w', encoding='utf-8') as f:
                f.write(h_css)

apply_fixes()
print(f'All fixes for HelpTrickBD Pro v{VERSION} successfully applied!')
