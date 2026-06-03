const { chromium } = require('playwright');
const fs = require('fs');

(async () => {
  const urls = fs.readFileSync('urls.txt', 'utf-8')
    .split('\n')
    .map(url => url.trim())
    .filter(url => url.length > 0);

  const browser = await chromium.launch();
  const page = await browser.newPage();
  
  const sleep = (time) => new Promise((r) => setTimeout(r, time));//timeはミリ秒

  for (let i = 0; i < urls.length; i++) {
    await page.goto(urls[i], { waitUntil: 'load', timeout: 5000 });
    await page.setViewportSize({ width: 3840, height: 2160 });
    await sleep(1000);
    await page.screenshot({
      path: `screenshot-${String(i + 1).padStart(3, '0')}.png`,
      fullPage: true
    });
    console.log(`撮影完了: ${urls[i]}`);
  }

  await browser.close();
})();
