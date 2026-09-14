/**
 * Google Lighthouse Performance & SEO Audit Runner for HelpTrickBD
 * Powered by Google Lighthouse (33,000+ GitHub Stars)
 * 
 * Usage:
 *   node tools/lighthouse/audit_performance.js
 *   node tools/lighthouse/audit_performance.js --url https://www.helptrickbd.com/2026/01/sample-post.html
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const targetUrl = process.argv[2] || 'https://www.helptrickbd.com/';
const outputHtml = path.join(__dirname, 'lighthouse_report.html');
const outputJson = path.join(__dirname, 'lighthouse_report.json');

const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
if (fs.existsSync(chromePath)) {
    process.env.CHROME_PATH = chromePath;
}

console.log('='.repeat(60));
console.log('  HelpTrickBD - Google Lighthouse Audit Runner');
console.log(`  Target URL: ${targetUrl}`);
console.log(`  Using Chrome: ${process.env.CHROME_PATH || 'Default'}`);
console.log('='.repeat(60));
console.log('\n[*] Running Google Lighthouse audit (this may take 30-45 seconds)...\n');

try {
    const cmd = `npx -y lighthouse "${targetUrl}" --output html --output json --output-path "${path.join(__dirname, 'lighthouse_report')}" --chrome-flags="--headless --no-sandbox" --quiet`;
    execSync(cmd, { stdio: 'inherit' });

    console.log('\n[SUCCESS] Lighthouse Audit Finished!');
    console.log(`  HTML Report: ${outputHtml}`);
    console.log(`  JSON Report: ${outputJson}`);
    console.log('\nYou can open lighthouse_report.html in any browser to inspect your scores.');
} catch (error) {
    console.error('\n[ERROR] Lighthouse audit failed to run:', error.message);
}
