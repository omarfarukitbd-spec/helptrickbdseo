# 🔄 05_MULTI_PC_SYNC_PROTOCOL.md — Multi-Machine Git & State Synchronization
### Helptrickbd.com Home PC ↔ Office PC Seamless Pairing

> [!IMPORTANT]
> **MULTI-PC INTEGRITY PRINCIPLE**: The user works across two primary locations (Home PC and Office Laptop/PC). Inconsistent state, uncommitted changes, or forgotten pulls cause code divergence, broken files, and duplicated efforts. This protocol eliminates multi-device friction.

---

## 🔁 1. Pre-Task Protocol (কাজের শুরুর পূর্বশর্ত)
Before inspecting files, drafting code, or answering any implementation request, the agent MUST run:

```bash
git fetch origin
git status
```

1. **If Remote Has New Commits**:
   - Immediately pull updates using rebase to maintain a clean linear commit graph:
     ```bash
     git pull --rebase origin main
     ```
2. **If Local Working Tree Is Dirty**:
   - Inspect uncommitted changes. Stash or commit before pulling to prevent merge collisions.
3. **Verify Synchronized State**:
   - Ensure local `HEAD` matches `origin/main`.

---

## 📤 2. Post-Task Protocol (কাজের শেষের পূর্বশর্ত)
Immediately after completing a code modification, post expansion, asset generation, or milestone, the agent MUST execute:

```bash
git add -A
git commit -m "<type>(<scope>): <clear descriptive message>"
git push origin main
```

### Commit Types:
- `feat(content)`: Added new post or expanded thin article.
- `fix(permalinks)`: Corrected generic slug or broken URL.
- `fix(images)`: Compressed WebP asset or updated CDN path.
- `docs(rules)`: Updated agent guidelines or project documentation.
- `chore(sync)`: Synchronized session handover state.

---

## 🔒 3. Credentials & Local Secrets Protection (.gitignore Enforcement)
The following files contain private tokens and must **NEVER** be committed or pushed to Git:
1. `service_account.json` (Google Cloud Indexing API private key).
2. `tools/blogger_publisher/client_secrets.json` (Google OAuth Client ID & secret).
3. `tools/blogger_publisher/blogger_token.json` (Active authenticated Blogger OAuth session).

### Safe Handling Rule:
- Verify `.gitignore` contains all secret filenames.
- **Zero-Deletion Policy (টোকেন ফাইল ডিলিট সম্পূর্ণ নিষিদ্ধ)**: If a token expires or Blogger API reports an authentication error on a new machine, the agent **MUST NOT delete or recreate `blogger_token.json` autonomously**. The agent must run `python tools/check_all_credentials.py`, diagnose the issue, and inform the user with actionable instructions.
- If a new authentication is needed, instruct the user to run `python tools/blogger_publisher/authenticate.py`. **Never attempt to commit tokens to Git.**

---

## 📝 4. Handover & Context Continuity
1. **Documenting Major Milestones**:
   - Significant milestones (e.g., publishing a post batch, fixing dead links, updating theme XML) must be appended to `docs/CHAT_HISTORY.md` or logged in the commit message.
2. **Session Context Transfer**:
   - Ensure the next agent on the other PC can immediately identify:
     * Exactly which posts were touched.
     * What tools were run.
     * What remains on the immediate roadmap.
