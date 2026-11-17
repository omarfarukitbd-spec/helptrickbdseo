<?php
/**
 * Academic Comments & Discussion Component
 *
 * @package HelpTrickBD_EduPortal
 */

if (!defined('ABSPATH')) {
    exit;
}

if (post_password_required()) {
    return;
}
?>

<div id="comments" class="ht-comments-area" style="margin-top:40px;padding-top:30px;border-top:2px solid var(--ht-border);">
  <?php if (have_comments()) : ?>
    <h3 class="ht-comments-title" style="font-size:1.3rem;font-weight:800;color:var(--ht-text-primary);margin-bottom:20px;">
      <?php
      $comment_count = get_comments_number();
      printf(
          esc_html(_nx('1 Comment & Question', '%s Comments & Questions', $comment_count, 'comments title', 'helptrickbd-edu')),
          esc_html(number_format_i18n($comment_count))
      );
      ?>
    </h3>

    <ol class="ht-comment-list" style="list-style:none;padding:0;margin:0 0 30px;">
      <?php
      wp_list_comments(array(
          'style'       => 'ol',
          'short_ping'  => true,
          'avatar_size' => 48,
      ));
      ?>
    </ol>

    <?php the_comments_navigation(); ?>

    <?php if (!comments_open()) : ?>
      <p class="ht-no-comments" style="font-size:0.9rem;color:var(--ht-text-muted);font-style:italic;">
        <?php esc_html_e('Comments are closed for this article.', 'helptrickbd-edu'); ?>
      </p>
    <?php endif; ?>

  <?php endif; ?>

  <?php
  comment_form(array(
      'title_reply'          => esc_html__('Leave a Comment or Question', 'helptrickbd-edu'),
      'title_reply_to'       => esc_html__('Reply to %s', 'helptrickbd-edu'),
      'cancel_reply_link'    => esc_html__('Cancel Reply', 'helptrickbd-edu'),
      'label_submit'         => esc_html__('Post Comment', 'helptrickbd-edu'),
      'comment_notes_before' => '<p class="comment-notes" style="font-size:0.85rem;color:var(--ht-text-muted);margin-bottom:12px;">' . esc_html__('Your email address will not be published. Required fields are marked *', 'helptrickbd-edu') . '</p>',
      'comment_field'        => '<div class="comment-form-comment" style="margin-bottom:16px;"><label for="comment" style="display:block;font-weight:700;margin-bottom:6px;font-size:0.9rem;">' . esc_html__('Your Comment or Question *', 'helptrickbd-edu') . '</label><textarea id="comment" name="comment" cols="45" rows="5" required style="width:100%;padding:10px 14px;border:1px solid var(--ht-border);border-radius:var(--ht-radius-sm);font-family:var(--ht-font-sans);background:var(--ht-surface);color:var(--ht-text-primary);"></textarea></div>',
  ));
  ?>
</div>
