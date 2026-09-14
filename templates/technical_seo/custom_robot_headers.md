# ⚙️ Blogger Custom Robot Header Tags Configuration

Location: **Blogger Dashboard > Settings > Crawlers and indexing > Enable custom robot header tags**

Switch the toggle to **ON**, then configure each section as follows:

---

### 1. Home page tags
- Enable: **`all`**
- Enable: **`noodp`**
- *(Leave everything else OFF)*
- Click **Save**.

### 2. Archive and search page tags (Important: prevents thin duplicate indexing)
- Enable: **`noindex`**
- Enable: **`nofollow`**
- Enable: **`noodp`**
- *(Leave everything else OFF)*
- Click **Save**.

### 3. Post and page tags
- Enable: **`all`**
- Enable: **`noodp`**
- *(Leave everything else OFF)*
- Click **Save**.

---

### 💡 Why this setup is critical for AdSense and Indexing:
1. **Prevents Duplicate Content:** Search result pages (`/search?q=...`) and monthly archives are thin and duplicate posts. Setting them to `noindex` keeps Google Search Console focused only on high-value posts.
2. **Protects Crawl Budget:** Googlebot won't waste crawl quota crawling archive pagination.
3. **Improves Site Quality Score:** AdSense evaluates the percentage of high-value indexed URLs vs junk URLs.
