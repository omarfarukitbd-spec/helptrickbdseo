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

    <?php
    $is_bn = function_exists('ht_is_bangla_locale') ? ht_is_bangla_locale() : true;
    if (have_comments()) : 
    ?>
        <h3 class="ht-comments-title">
            <?php ht_m3_icon('forum', 22); ?>
            <span>
                <?php
                $ht_comment_count = get_comments_number();
                $formatted_num = function_exists('ht_number') ? ht_number($ht_comment_count) : number_format_i18n($ht_comment_count);
                if ('1' === strval($ht_comment_count)) {
                    if ($is_bn) {
                        printf(
                            /* translators: 1: title. */
                            esc_html__('&ldquo;%1$s&rdquo;-এর ওপর একটি মন্তব্য', 'helptrickbd'),
                            '<span>' . wp_kses_post(get_the_title()) . '</span>'
                        );
                    } else {
                        printf(
                            /* translators: 1: title. */
                            esc_html__('One thought on &ldquo;%1$s&rdquo;', 'helptrickbd'),
                            '<span>' . wp_kses_post(get_the_title()) . '</span>'
                        );
                    }
                } else {
                    if ($is_bn) {
                        printf(
                            /* translators: 1: comment count number, 2: title. */
                            esc_html__('&ldquo;%2$s&rdquo;-এর ওপর %1$s টি মন্তব্য', 'helptrickbd'),
                            esc_html($formatted_num),
                            '<span>' . wp_kses_post(get_the_title()) . '</span>'
                        );
                    } else {
                        printf(
                            /* translators: 1: comment count number, 2: title. */
                            esc_html(_nx('%1$s thought on &ldquo;%2$s&rdquo;', '%1$s thoughts on &ldquo;%2$s&rdquo;', $ht_comment_count, 'comments title', 'helptrickbd')),
                            esc_html($formatted_num),
                            '<span>' . wp_kses_post(get_the_title()) . '</span>'
                        );
                    }
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
            <p class="ht-no-comments"><?php echo $is_bn ? esc_html__('মন্তব্য করার সুবিধা বন্ধ রয়েছে।', 'helptrickbd') : esc_html__('Comments are closed.', 'helptrickbd'); ?></p>
        <?php
        endif;

    endif; // have_comments()

    // Comment submission form
    $reply_title = $is_bn ? esc_html__('মতামত বা প্রশ্ন লিখুন', 'helptrickbd') : esc_html__('Leave a Comment or Question', 'helptrickbd');
    $reply_to    = $is_bn ? esc_html__('%s-কে উত্তর দিন', 'helptrickbd') : esc_html__('Reply to %s', 'helptrickbd');
    $cancel_link = $is_bn ? esc_html__('উত্তর বাতিল করুন', 'helptrickbd') : esc_html__('Cancel Reply', 'helptrickbd');
    $submit_btn  = $is_bn ? esc_html__('মন্তব্য প্রকাশ করুন', 'helptrickbd') : esc_html__('Post Comment', 'helptrickbd');
    $email_notes = $is_bn ? esc_html__('আপনার ইমেইল ঠিকানা প্রকাশ করা হবে না।', 'helptrickbd') : esc_html__('Your email address will not be published.', 'helptrickbd');

    comment_form([
        'title_reply'          => $reply_title,
        'title_reply_to'       => $reply_to,
        'cancel_reply_link'    => $cancel_link,
        'label_submit'         => $submit_btn,
        'comment_notes_before' => '<p class="ht-comment-notes"><span id="email-notes">' . $email_notes . '</span></p>',
    ]);
    ?>

</div><!-- #comments -->
