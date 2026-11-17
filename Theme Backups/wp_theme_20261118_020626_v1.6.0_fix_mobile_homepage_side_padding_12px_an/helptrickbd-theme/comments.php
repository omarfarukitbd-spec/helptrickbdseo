<?php
/**
 * The Template for displaying Comments in HelpTrickBD Pro
 * 100% WordPress Core compliant, accessible WCAG 2.1 AA, Material 3 vector styling.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

if (post_password_required()) {
    return;
}
?>

<div id="comments" class="ht-comments-area">

    <?php if (have_comments()) : ?>
        <h3 class="ht-comments-title">
            <?php ht_m3_icon('forum', 22); ?>
            <span>
                <?php
                $ht_comment_count = get_comments_number();
                if ('1' === $ht_comment_count) {
                    printf(
                        /* translators: 1: title. */
                        esc_html__('One thought on &ldquo;%1$s&rdquo;', 'helptrickbd'),
                        '<span>' . wp_kses_post(get_the_title()) . '</span>'
                    );
                } else {
                    printf(
                        /* translators: 1: comment count number, 2: title. */
                        esc_html(_nx('%1$s thought on &ldquo;%2$s&rdquo;', '%1$s thoughts on &ldquo;%2$s&rdquo;', $ht_comment_count, 'comments title', 'helptrickbd')),
                        number_format_i18n($ht_comment_count),
                        '<span>' . wp_kses_post(get_the_title()) . '</span>'
                    );
                }
                ?>
            </span>
        </h3>

        <?php the_comments_navigation(); ?>

        <ol class="ht-comment-list">
            <?php
            wp_list_comments([
                'style'       => 'ol',
                'short_ping'  => true,
                'avatar_size' => 48,
            ]);
            ?>
        </ol>

        <?php
        the_comments_navigation();

        // If comments are closed and there are comments, let's leave a little note.
        if (!comments_open()) :
        ?>
            <p class="ht-no-comments"><?php esc_html_e('Comments are closed.', 'helptrickbd'); ?></p>
        <?php
        endif;

    endif; // have_comments()

    // Comment submission form
    comment_form([
        'title_reply'          => esc_html__('Leave a Comment or Question', 'helptrickbd'),
        'title_reply_to'       => esc_html__('Reply to %s', 'helptrickbd'),
        'cancel_reply_link'    => esc_html__('Cancel Reply', 'helptrickbd'),
        'label_submit'         => esc_html__('Post Comment', 'helptrickbd'),
        'comment_notes_before' => '<p class="ht-comment-notes"><span id="email-notes">' . esc_html__('Your email address will not be published.', 'helptrickbd') . '</span></p>',
    ]);
    ?>

</div><!-- #comments -->
