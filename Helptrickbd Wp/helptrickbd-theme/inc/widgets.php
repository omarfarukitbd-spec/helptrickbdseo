<?php
/**
 * Custom Widgets for HelpTrickBD Pro
 * Popular Posts and Modern Category Cards with Material 3 Icons & Zero Emojis.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * HelpTrickBD Popular Posts Widget
 */
class HT_Popular_Posts_Widget extends WP_Widget {

    public function __construct() {
        parent::__construct(
            'ht_popular_posts_widget',
            'HelpTrickBD: জনপ্রিয় পোস্ট (Popular Posts)',
            ['description' => 'র‍্যাংকড ১-৫ নম্বর ব্যাজ এবং থাম্বনেইল সহ সেরা জনপ্রিয় পোস্ট তালিকা']
        );
    }

    public function widget($args, $instance) {
        $title = !empty($instance['title']) ? $instance['title'] : 'জনপ্রিয় পোস্ট ও হ্যান্ডনোট';
        $number = !empty($instance['number']) ? absint($instance['number']) : 5;

        echo $args['before_widget'];

        echo '<div class="ht-widget-header">';
        ht_m3_icon('trending_up', 20, 'ht-widget-icon');
        echo '<h3 class="ht-widget-title">' . esc_html($title) . '</h3>';
        echo '</div>';

        $popular_query = new WP_Query([
            'posts_per_page'      => $number,
            'post_status'         => 'publish',
            'ignore_sticky_posts' => 1,
            'meta_key'            => 'ht_post_views_count',
            'orderby'             => 'meta_value_num date',
            'order'               => 'DESC',
        ]);

        if (!$popular_query->have_posts()) {
            $popular_query = new WP_Query([
                'posts_per_page'      => $number,
                'post_status'         => 'publish',
                'ignore_sticky_posts' => 1,
                'orderby'             => 'date',
                'order'               => 'DESC',
            ]);
        }

        if ($popular_query->have_posts()) :
        ?>
            <div class="ht-popular-list">
                <?php
                $rank = 0;
                while ($popular_query->have_posts()) :
                    $popular_query->the_post();
                    $rank++;
                ?>
                    <article class="ht-popular-item">
                        <a href="<?php the_permalink(); ?>" class="ht-popular-thumb-wrap" aria-label="<?php the_title_attribute(); ?>">
                            <div class="ht-popular-thumb-circle">
                                <?php ht_the_thumbnail(get_the_ID(), 'thumbnail', 'ht-popular-thumb-round'); ?>
                            </div>
                            <span class="ht-popular-badge ht-rank-<?php echo esc_attr($rank); ?>" title="র‍্যাঙ্ক #<?php echo esc_attr($rank); ?>"><?php echo esc_html(ht_bn_number($rank)); ?></span>
                        </a>
                        <div class="ht-popular-details">
                            <?php
                            $cats = get_the_category();
                            if (!empty($cats)) : ?>
                                <div class="ht-popular-cat-wrap">
                                    <span class="ht-popular-cat-chip"><?php echo esc_html($cats[0]->name); ?></span>
                                </div>
                            <?php endif; ?>
                            <h4 class="ht-popular-title">
                                <a href="<?php the_permalink(); ?>"><?php the_title(); ?></a>
                            </h4>
                            <div class="ht-popular-meta">
                                <span class="ht-popular-date">
                                    <?php ht_m3_icon('event', 13, 'ht-meta-icon'); ?>
                                    <?php ht_post_date(); ?>
                                </span>
                            </div>
                        </div>
                    </article>
                <?php
                endwhile;
                wp_reset_postdata();
                ?>
            </div>
        <?php
        endif;

        echo $args['after_widget'];
    }

    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : 'জনপ্রিয় পোস্ট ও হ্যান্ডনোট';
        $number = !empty($instance['number']) ? absint($instance['number']) : 5;
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>">শিরোনাম:</label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" name="<?php echo esc_attr($this->get_field_name('title')); ?>" type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('number')); ?>">পোস্ট সংখ্যা:</label>
            <input class="tiny-text" id="<?php echo esc_attr($this->get_field_id('number')); ?>" name="<?php echo esc_attr($this->get_field_name('number')); ?>" type="number" step="1" min="1" max="10" value="<?php echo esc_attr($number); ?>" size="3">
        </p>
        <?php
    }

    public function update($new_instance, $old_instance) {
        $instance = [];
        $instance['title'] = (!empty($new_instance['title'])) ? sanitize_text_field($new_instance['title']) : '';
        $instance['number'] = (!empty($new_instance['number'])) ? absint($new_instance['number']) : 5;
        return $instance;
    }
}

/**
 * HelpTrickBD Modern Categories Cards Widget
 */
class HT_Categories_Widget extends WP_Widget {

    public function __construct() {
        parent::__construct(
            'ht_categories_widget',
            'HelpTrickBD: আধুনিক বিষয়শ্রেণী (Category Cards)',
            ['description' => 'আইকন এবং পোস্ট কাউন্ট সহ আধুনিক কার্ড গ্রিড ক্যাটাগরি তালিকা']
        );
    }

    public function widget($args, $instance) {
        $title = !empty($instance['title']) ? $instance['title'] : 'সকল বিষয়শ্রেণী (ক্যাটাগরি)';
        $number = !empty($instance['number']) ? absint($instance['number']) : 10;

        echo $args['before_widget'];

        echo '<div class="ht-widget-header">';
        ht_m3_icon('folder', 20, 'ht-widget-icon');
        echo '<h3 class="ht-widget-title">' . esc_html($title) . '</h3>';
        echo '</div>';

        $categories = get_categories([
            'orderby'    => 'count',
            'order'      => 'DESC',
            'number'     => $number,
            'hide_empty' => true,
        ]);
        ?>
        <div class="ht-cat-cards-grid">
            <?php foreach ($categories as $category) : ?>
                <a href="<?php echo esc_url(get_category_link($category->term_id)); ?>" class="ht-cat-card-box">
                    <div class="ht-cat-card-left">
                        <span class="ht-cat-card-icon">
                            <?php ht_m3_icon('school', 18); ?>
                        </span>
                        <span class="ht-cat-card-name"><?php echo esc_html($category->name); ?></span>
                    </div>
                    <span class="ht-cat-card-badge">
                        <?php echo esc_html(ht_bn_number($category->count)); ?>টি
                    </span>
                </a>
            <?php endforeach; ?>
        </div>
        <?php

        echo $args['after_widget'];
    }

    public function form($instance) {
        $title = !empty($instance['title']) ? $instance['title'] : 'সকল বিষয়শ্রেণী (ক্যাটাগরি)';
        $number = !empty($instance['number']) ? absint($instance['number']) : 10;
        ?>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('title')); ?>">শিরোনাম:</label>
            <input class="widefat" id="<?php echo esc_attr($this->get_field_id('title')); ?>" name="<?php echo esc_attr($this->get_field_name('title')); ?>" type="text" value="<?php echo esc_attr($title); ?>">
        </p>
        <p>
            <label for="<?php echo esc_attr($this->get_field_id('number')); ?>">ক্যাটাগরি সংখ্যা:</label>
            <input class="tiny-text" id="<?php echo esc_attr($this->get_field_id('number')); ?>" name="<?php echo esc_attr($this->get_field_name('number')); ?>" type="number" step="1" min="1" max="20" value="<?php echo esc_attr($number); ?>" size="3">
        </p>
        <?php
    }

    public function update($new_instance, $old_instance) {
        $instance = [];
        $instance['title'] = (!empty($new_instance['title'])) ? sanitize_text_field($new_instance['title']) : '';
        $instance['number'] = (!empty($new_instance['number'])) ? absint($new_instance['number']) : 10;
        return $instance;
    }
}

/**
 * Register Custom HelpTrickBD Widgets
 */
function ht_register_custom_widgets() {
    register_widget('HT_Popular_Posts_Widget');
    register_widget('HT_Categories_Widget');
}
add_action('widgets_init', 'ht_register_custom_widgets');
