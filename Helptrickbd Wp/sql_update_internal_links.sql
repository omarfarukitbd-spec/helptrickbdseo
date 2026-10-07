-- ==============================================================================
-- HelpTrickBD - 1-Click Database Search & Replace SQL Script
-- Run in phpMyAdmin or Adminer or MySQL CLI
-- Permanently converts all legacy Blogger URLs in wp_posts table to modern WP permalinks
-- ==============================================================================

START TRANSACTION;

-- Alias: ssc-english-2nd-paper-suggestion-2027 -> ssc-english-2nd-paper-final-suggestion
UPDATE wp_posts SET post_content = REPLACE(post_content, '/ssc-english-2nd-paper-suggestion-2027.html', '/ssc-english-2nd-paper-final-suggestion/') WHERE post_content LIKE '%/ssc-english-2nd-paper-suggestion-2027.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/ssc-english-2nd-paper-suggestion-2027.html', 'https://www.helptrickbd.com/ssc-english-2nd-paper-final-suggestion/') WHERE post_content LIKE '%/p/ssc-english-2nd-paper-suggestion-2027.html%';

-- Alias: bcs-preliminary-marks-distribution-booklist -> bcs-preliminary-marks-distribution_01436475916
UPDATE wp_posts SET post_content = REPLACE(post_content, '/bcs-preliminary-marks-distribution-booklist.html', '/bcs-preliminary-marks-distribution_01436475916/') WHERE post_content LIKE '%/bcs-preliminary-marks-distribution-booklist.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/bcs-preliminary-marks-distribution-booklist.html', 'https://www.helptrickbd.com/bcs-preliminary-marks-distribution_01436475916/') WHERE post_content LIKE '%/p/bcs-preliminary-marks-distribution-booklist.html%';

-- Alias: remittance-importance -> what-is-remittance-importance-economy-obstacles
UPDATE wp_posts SET post_content = REPLACE(post_content, '/remittance-importance.html', '/what-is-remittance-importance-economy-obstacles/') WHERE post_content LIKE '%/remittance-importance.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/remittance-importance.html', 'https://www.helptrickbd.com/what-is-remittance-importance-economy-obstacles/') WHERE post_content LIKE '%/p/remittance-importance.html%';

-- Alias: basic-economy-problems-bd -> bangladesh-basic-economy-features-problems-solutions
UPDATE wp_posts SET post_content = REPLACE(post_content, '/basic-economy-problems-bd.html', '/bangladesh-basic-economy-features-problems-solutions/') WHERE post_content LIKE '%/basic-economy-problems-bd.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/basic-economy-problems-bd.html', 'https://www.helptrickbd.com/bangladesh-basic-economy-features-problems-solutions/') WHERE post_content LIKE '%/p/basic-economy-problems-bd.html%';

-- Alias: budget-importance -> what-is-budget-importance-role-economy
UPDATE wp_posts SET post_content = REPLACE(post_content, '/budget-importance.html', '/what-is-budget-importance-role-economy/') WHERE post_content LIKE '%/budget-importance.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/budget-importance.html', 'https://www.helptrickbd.com/what-is-budget-importance-role-economy/') WHERE post_content LIKE '%/p/budget-importance.html%';

-- Alias: nu-cgpa-calculator -> nu-cgpa-calculator
UPDATE wp_posts SET post_content = REPLACE(post_content, '/nu-cgpa-calculator.html', '/nu-cgpa-calculator/') WHERE post_content LIKE '%/nu-cgpa-calculator.html%';
UPDATE wp_posts SET post_content = REPLACE(post_content, 'https://www.helptrickbd.com/p/nu-cgpa-calculator.html', 'https://www.helptrickbd.com/nu-cgpa-calculator/') WHERE post_content LIKE '%/p/nu-cgpa-calculator.html%';

-- Generic regex replace for standard /YYYY/MM/slug.html and /p/slug.html
-- Note: If your MySQL supports REGEXP_REPLACE (MySQL 8.0+ or MariaDB 10.0+):
UPDATE wp_posts SET post_content = REGEXP_REPLACE(post_content, 'https?://(www\.)?helptrickbd\.com/(p/|[0-9]{4}/[0-9]{2}/)([a-zA-Z0-9_-]+)\.html', 'https://www.helptrickbd.com/\\3/') WHERE post_content REGEXP 'helptrickbd\.com/(p/|[0-9]{4}/[0-9]{2}/)[a-zA-Z0-9_-]+\.html';

COMMIT;
