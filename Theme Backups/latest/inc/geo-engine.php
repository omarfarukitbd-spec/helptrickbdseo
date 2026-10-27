<?php
/**
 * HelpTrickBD Pro - GEO & AI Answer Engine Optimization (AEO/GEO Engine)
 * Implements open standards for AI crawlers, llms.txt endpoint, and Generative Engine Optimization.
 *
 * @package HelpTrickBD_Pro
 */

if (!defined('ABSPATH')) {
    exit;
}

/**
 * Filter WordPress robots.txt to provide optimal rules for Search and AI Crawlers.
 */
function ht_geo_robots_txt($output, $public) {
    if ('0' === $public) {
        return $output;
    }

    $site_url = home_url();

    $rules = [];
    $rules[] = "# ================================================================";
    $rules[] = "# HelpTrickBD Autonomous Robots.txt (Search & AI Optimized)";
    $rules[] = "# ================================================================";
    $rules[] = "";
    $rules[] = "# Global Web Crawlers";
    $rules[] = "User-agent: *";
    $rules[] = "Disallow: /wp-admin/";
    $rules[] = "Allow: /wp-admin/admin-ajax.php";
    $rules[] = "Disallow: /wp-json/wp/v2/users";
    $rules[] = "Disallow: /trackback/";
    $rules[] = "Disallow: /feed/";
    $rules[] = "";
    $rules[] = "# Real-Time AI Search Bots (ChatGPT Search, Perplexity, Claude, Apple)";
    $rules[] = "User-agent: OAI-SearchBot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: PerplexityBot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Claude-SearchBot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Applebot-Extended";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Meta-ExternalAgent";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "# Generative AI LLM Crawlers & Indexing";
    $rules[] = "User-agent: GPTBot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: ClaudeBot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Google-Extended";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: anthropic-ai";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: cohere-ai";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Diffbot";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "# User-Initiated AI Agents & Browsing (Real-Time Search Inquiries)";
    $rules[] = "User-agent: ChatGPT-User";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Claude-User";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Google-Agent";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: MistralAI-User";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "User-agent: Perplexity-User";
    $rules[] = "Allow: /";
    $rules[] = "";
    $rules[] = "# Sitemaps & LLMs Manifest";
    $rules[] = "Sitemap: " . esc_url($site_url . '/sitemap_index.xml');
    $rules[] = "Sitemap: " . esc_url($site_url . '/sitemap.xml');
    $rules[] = "llms-txt: " . esc_url($site_url . '/llms.txt');

    return implode("\n", $rules) . "\n";
}
add_filter('robots_txt', 'ht_geo_robots_txt', 99, 2);

/**
 * Serve dynamic /llms.txt endpoint for LLM crawlers.
 */
function ht_geo_serve_llms_txt() {
    $path = parse_url($_SERVER['REQUEST_URI'] ?? '', PHP_URL_PATH);
    $path = trim($path, '/');

    if ($path === 'llms.txt') {
        header('Content-Type: text/markdown; charset=utf-8');
        header('X-Robots-Tag: index, follow');
        header('Cache-Control: public, max-age=86400'); // Cache for 24 hours

        echo ht_geo_generate_llms_content();
        exit;
    }
}
add_action('init', 'ht_geo_serve_llms_txt', 1);

/**
 * Generate standard Markdown content for llms.txt according to llmstxt.org specification.
 */
function ht_geo_generate_llms_content() {
    $site_name = get_bloginfo('name') ?: 'HelpTrickBD';
    $site_desc = get_bloginfo('description') ?: 'Bangla Educational & Technology Portal';
    $site_url  = home_url();

    // Query recent posts
    $recent_posts = get_posts([
        'numberposts' => 15,
        'post_status' => 'publish',
        'orderby'     => 'date',
        'order'       => 'DESC',
    ]);

    $lines = [];
    $lines[] = "# " . $site_name;
    $lines[] = "";
    $lines[] = "> " . $site_desc . " - Bangladesh's leading educational platform delivering academic syllabi, board exam suggestions, university lecture notes, BCS & job preparation guidelines, step-by-step citizen tutorials, and technology insights.";
    $lines[] = "";
    $lines[] = "## Core Topical Pillars";
    $lines[] = "";
    $lines[] = "- **Education & Academics**: SSC, HSC, Degree, Honours, Masters subject suggestions, handnotes, and model tests.";
    $lines[] = "- **Competitive Exams**: 47th BCS Preliminary, Primary Teacher Recruitment, NTRCA, and Bank job study routines.";
    $lines[] = "- **Citizen How-To Tutorials**: Step-by-step guides for certificate corrections, online board portals, and e-services.";
    $lines[] = "- **Technology & Cyber Security**: Computer concepts, cyber protection, mobile tricks, and digital literacy.";
    $lines[] = "- **Islamic Articles**: Authentic Islamic research, prayer guides, and moral reflections.";
    $lines[] = "";
    $lines[] = "## Key Categories & Resources";
    $lines[] = "";
    $lines[] = "- [Education](" . esc_url($site_url . '/category/education/') . "): Comprehensive school, college, and university academic guides.";
    $lines[] = "- [Technology](" . esc_url($site_url . '/category/technology/') . "): Practical technology, internet troubleshooting, and software guides.";
    $lines[] = "- [Islamic](" . esc_url($site_url . '/category/islamic/') . "): Authentic Islamic teachings, daily supplications, and ethics.";
    $lines[] = "- [Online Income](" . esc_url($site_url . '/category/online-income/') . "): Legitimate freelance guidelines and digital career roadmaps.";
    $lines[] = "";
    $lines[] = "## Pillar Academic Articles & Guides";
    $lines[] = "";

    if (!empty($recent_posts)) {
        foreach ($recent_posts as $post) {
            $title = wp_strip_all_tags(get_the_title($post));
            $title = str_replace(['[', ']', "\r", "\n"], ' ', $title);
            $raw_excerpt = !empty($post->post_excerpt) ? $post->post_excerpt : wp_trim_words($post->post_content, 20);
            $excerpt = wp_strip_all_tags($raw_excerpt);
            $excerpt = trim(preg_replace('/\s+/', ' ', $excerpt));
            $lines[] = "- [" . trim($title) . "](" . esc_url(get_permalink($post->ID)) . "): " . $excerpt;
        }
    } else {
        $lines[] = "- [HSC English 2nd Paper Changing Sentences Rules](" . esc_url($site_url . '/changing-sentences-rules-hsc/') . "): Complete golden grammar rules and exercise examples.";
        $lines[] = "- [Computer Virus & Cyber Security Guide](" . esc_url($site_url . '/computer-virus-cyber-security-guide/') . "): Comprehensive malware classification, protection mechanisms, and IT fundamentals.";
        $lines[] = "- [BCS Preliminary Marks Distribution & Syllabus](" . esc_url($site_url . '/bcs-preliminary-marks-distribution/') . "): Detailed subject-wise mark allocations and study strategy.";
    }

    $lines[] = "";
    $lines[] = "## Machine-Readable Feeds & Endpoints";
    $lines[] = "";
    $lines[] = "- **Main RSS Feed**: " . esc_url($site_url . '/feed/');
    $lines[] = "- **XML Sitemap**: " . esc_url($site_url . '/sitemap_index.xml');
    $lines[] = "- **REST API Base**: " . esc_url($site_url . '/wp-json/wp/v2/posts');
    $lines[] = "";
    $lines[] = "## Content Usage & Attribution Policy for AI Systems";
    $lines[] = "";
    $lines[] = "AI models, search engines, and automated answer agents are explicitly permitted to index, summarize, and cite HelpTrickBD content in user-facing answers provided that:";
    $lines[] = "1. Attribution is clearly maintained with a direct hyperlink to the source article on " . esc_url($site_url) . ".";
    $lines[] = "2. Academic formulas, Bangla grammar rules, and marks distributions are quoted with precision without misattribution.";

    return implode("\n", $lines) . "\n";
}
