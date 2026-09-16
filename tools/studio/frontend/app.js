// HelpTrickBD Autonomous Publishing Studio Frontend Logic

document.addEventListener("DOMContentLoaded", () => {
  let uploadedPdfText = "";
  let currentBlueprint = null;

  // DOM Elements
  const pdfDropzone = document.getElementById("pdfDropzone");
  const pdfFileInput = document.getElementById("pdfFileInput");
  const fileInfo = document.getElementById("fileInfo");
  const postTitle = document.getElementById("postTitle");
  const postCategory = document.getElementById("postCategory");
  const siloPartsCount = document.getElementById("siloPartsCount");
  const btnAnalyze = document.getElementById("btnAnalyze");

  const step1Card = document.getElementById("step1Card");
  const step2Card = document.getElementById("step2Card");
  const step3Card = document.getElementById("step3Card");

  const stepIndicator1 = document.getElementById("stepIndicator1");
  const stepIndicator2 = document.getElementById("stepIndicator2");
  const stepIndicator3 = document.getElementById("stepIndicator3");

  const pillarBox = document.getElementById("pillarBox");
  const siloGrid = document.getElementById("siloGrid");
  const btnBackToStep1 = document.getElementById("btnBackToStep1");
  const btnProceedToPreview = document.getElementById("btnProceedToPreview");

  const btnBackToStep2 = document.getElementById("btnBackToStep2");
  const searchDescText = document.getElementById("searchDescText");
  const btnCopySearchDesc = document.getElementById("btnCopySearchDesc");
  const articlePreviewBody = document.getElementById("articlePreviewBody");
  const toggleLivePublish = document.getElementById("toggleLivePublish");
  const toggleStatusLabel = document.getElementById("toggleStatusLabel");
  const btnApproveAndPublish = document.getElementById("btnApproveAndPublish");
  const resultBox = document.getElementById("resultBox");
  const liveResultContent = document.getElementById("liveResultContent");

  // Drag & Drop
  pdfDropzone.addEventListener("click", () => pdfFileInput.click());

  pdfDropzone.addEventListener("dragover", (e) => {
    e.preventDefault();
    pdfDropzone.classList.add("dragover");
  });

  pdfDropzone.addEventListener("dragleave", () => {
    pdfDropzone.classList.remove("dragover");
  });

  pdfDropzone.addEventListener("drop", (e) => {
    e.preventDefault();
    pdfDropzone.classList.remove("dragover");
    if (e.dataTransfer.files.length > 0) {
      handlePdfUpload(e.dataTransfer.files[0]);
    }
  });

  pdfFileInput.addEventListener("change", (e) => {
    if (e.target.files.length > 0) {
      handlePdfUpload(e.target.files[0]);
    }
  });

  function handlePdfUpload(file) {
    if (!file.name.endsWith(".pdf")) {
      alert("দয়া করে একটি সঠিক .pdf ফাইল নির্বাচন করুন!");
      return;
    }

    fileInfo.style.display = "block";
    fileInfo.textContent = `⏳ আপলোড ও স্ক্যান হচ্ছে: ${file.name} (${(file.size / 1024).toFixed(1)} KB)...`;

    fetch("/api/upload-pdf", {
      method: "POST",
      body: file
    })
    .then(r => r.json())
    .then(data => {
      if (data.success) {
        fileInfo.textContent = `✔ স্ক্যান সম্পন্ন: ${file.name} — ${data.pages} পৃষ্ঠা, ${data.word_count} শব্দ!`;
        uploadedPdfText = data.preview_snippet || "";
        if (!postTitle.value.trim()) {
          // Auto-suggest title based on filename
          let nameClean = file.name.replace(".pdf", "").replace(/[-_]/g, " ");
          postTitle.value = nameClean;
        }
      } else {
        fileInfo.textContent = `❌ ত্রুটি: ${data.error}`;
      }
    })
    .catch(err => {
      fileInfo.textContent = `❌ নেটওয়ার্ক ত্রুটি: ${err}`;
    });
  }

  // Step 1 -> Step 2: Analyze & Generate Blueprint
  btnAnalyze.addEventListener("click", () => {
    const title = postTitle.value.trim();
    if (!title) {
      alert("দয়া করে আর্টিকেলের একটি মূল শিরোনাম লিখুন!");
      postTitle.focus();
      return;
    }

    btnAnalyze.disabled = true;
    btnAnalyze.textContent = "⏳ সাইলো আর্কিটেকচার তৈরি হচ্ছে...";

    fetch("/api/generate-blueprint", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonBody({
        title: title,
        category: postCategory.value,
        text: uploadedPdfText
      })
    })
    .then(r => r.json())
    .then(data => {
      btnAnalyze.disabled = false;
      btnAnalyze.textContent = "⚡ স্মার্ট সাইলো প্ল্যান ও ব্লুপ্রিন্ট তৈরি করুন";

      if (data.success) {
        currentBlueprint = data.blueprint;
        renderSiloBlueprint(currentBlueprint);
        showStep(2);
      } else {
        alert("ত্রুটি: " + data.error);
      }
    })
    .catch(err => {
      btnAnalyze.disabled = false;
      btnAnalyze.textContent = "⚡ স্মার্ট সাইলো প্ল্যান ও ব্লুপ্রিন্ট তৈরি করুন";
      alert("নেটওয়ার্ক সমস্যা: " + err);
    });
  });

  function renderSiloBlueprint(bp) {
    // Render Pillar
    pillarBox.innerHTML = `
      <div style="display: flex; justify-content: space-between; align-items: flex-start;">
        <div>
          <span style="font-size: 12px; font-weight: 700; background: #0284c7; color: white; padding: 2px 8px; border-radius: 4px;">MAIN PILLAR HUB</span>
          <h3 style="font-size: 18px; margin: 6px 0 4px 0; color: #0c2340;">${bp.pillar.title}</h3>
          <p style="font-size: 13px; color: #475569; margin: 0;"><strong>পারমালিঙ্ক স্লাগ:</strong> <code>${bp.pillar.slug}</code> | <strong>লেবেল:</strong> ${bp.pillar.labels.join(", ")}</p>
        </div>
        <span style="font-size: 13px; font-weight: 600; color: #0284c7; background: #e0f2fe; padding: 4px 10px; border-radius: 6px;">১৬:৯ ব্যানার (${bp.pillar.bg_image})</span>
      </div>
    `;

    // Render Silos
    siloGrid.innerHTML = "";
    bp.silos.forEach((silo, idx) => {
      const card = document.createElement("div");
      card.className = "silo-card-item";
      card.innerHTML = `
        <span class="silo-part-badge">${silo.part_name}</span>
        <h4>${silo.bengali_title}</h4>
        <p><strong>টার্গেট সমাধান:</strong> ${silo.questions}</p>
        <div class="silo-meta">
          <span>স্লাগ: <code>${silo.slug}</code></span>
          <span>টেমপ্লেট: ${silo.bg_image}</span>
        </div>
      `;
      siloGrid.appendChild(card);
    });
  }

  // Navigation handlers
  btnBackToStep1.addEventListener("click", () => showStep(1));
  btnBackToStep2.addEventListener("click", () => showStep(2));

  // Step 2 -> Step 3: Preview
  btnProceedToPreview.addEventListener("click", () => {
    if (!currentBlueprint) return;

    // Load Pillar or Part 1 sample into preview
    const samplePost = currentBlueprint.silos[0] || currentBlueprint.pillar;
    searchDescText.textContent = samplePost.search_desc || "এসএসসি ও দাখিল পরীক্ষার পূর্ণাঙ্গ প্রস্তুতি ও মানবণ্টন নির্দেশিকা।";

    // Render rich preview snippet
    articlePreviewBody.innerHTML = `
      <div style="font-family: 'SolaimanLipi', sans-serif; line-height: 1.8;">
        <h1 style="color: #0c2340; font-size: 26px; border-left: 5px solid #0284c7; padding-left: 12px; margin-bottom: 16px;">${samplePost.bengali_title || samplePost.title}</h1>
        
        <div style="background: #f8fafd; border: 1px solid #dbeafe; border-left: 4px solid #0c2340; padding: 14px 18px; border-radius: 8px; margin-bottom: 20px;">
          <p style="margin: 0; font-size: 16px; color: #0f172a;"><strong>সারসংক্ষেপ (Quick Overview):</strong> জাতীয় শিক্ষাক্রমের নতুন সিলেবাস অনুসারে প্রস্তুতকৃত এই চূড়ান্ত নির্দেশিকায় মানবণ্টন, গুরুত্বপূর্ণ প্রশ্ন এবং এ-প্লাস পাওয়ার কৌশলসমূহ ক্রমানুসারে সাজানো হয়েছে।</p>
        </div>

        <p style="font-size: 17px; color: #334155;">পরীক্ষায় পূর্ণ নম্বর নিশ্চিত করার জন্য প্রতিটি অধ্যায়ের মৌলিক ধারণা ও প্রশ্নোত্তরের কাঠামো স্পষ্টভাবে উপস্থাপন করা হলো...</p>

        <div style="background: #f8fafc; border: 1px solid #e2e8f0; border-left: 4px solid #0284c7; border-radius: 8px; padding: 16px; margin: 24px 0;">
          <h4 style="margin: 0 0 8px 0; color: #0f172a; font-size: 16px;">📚 স্টাডি সাইলো সিরিজ নেভিগেশন (Silo Navigation Box)</h4>
          <p style="margin: 0; font-size: 14px; color: #64748b;">এই সিরিজের প্রতিটি সহযোগী পোস্ট ক্রমানুসারে পড়ে পূর্ণাঙ্গ প্রস্তুতি সম্পন্ন করুন।</p>
        </div>
      </div>
    `;

    showStep(3);
  });

  // Copy Search Description
  btnCopySearchDesc.addEventListener("click", () => {
    const text = searchDescText.textContent;
    navigator.clipboard.writeText(text).then(() => {
      btnCopySearchDesc.textContent = "✔ Copied!";
      setTimeout(() => {
        btnCopySearchDesc.textContent = "📋 Copy Description";
      }, 2000);
    });
  });

  // Toggle Live/Draft
  toggleLivePublish.addEventListener("change", (e) => {
    if (e.target.checked) {
      toggleStatusLabel.textContent = "সরাসরি লাইভ পাবলিশ (Live Published)";
      btnApproveAndPublish.className = "btn btn-success btn-large";
      btnApproveAndPublish.textContent = "🚀 Approve & Publish to Blogger (১-ক্লিক)";
    } else {
      toggleStatusLabel.textContent = "ড্রাফট হিসেবে সেভ (Save as Draft in Blogger)";
      btnApproveAndPublish.className = "btn btn-primary btn-large";
      btnApproveAndPublish.textContent = "💾 Approve & Save as Draft (১-ক্লিক)";
    }
  });

  // Publish / Save Button
  btnApproveAndPublish.addEventListener("click", () => {
    if (!currentBlueprint) return;

    const isLive = toggleLivePublish.checked;
    btnApproveAndPublish.disabled = true;
    btnApproveAndPublish.textContent = "⏳ ব্লগারে পোস্ট প্রসেস হচ্ছে...";

    const samplePost = currentBlueprint.silos[0] || currentBlueprint.pillar;

    fetch("/api/publish-live", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: jsonBody({
        title: samplePost.bengali_title || samplePost.title,
        content: articlePreviewBody.innerHTML,
        labels: samplePost.labels || ["Education"],
        is_draft: !isLive
      })
    })
    .then(r => r.json())
    .then(data => {
      btnApproveAndPublish.disabled = false;
      btnApproveAndPublish.textContent = isLive ? "🚀 Approve & Publish to Blogger (১-ক্লিক)" : "💾 Approve & Save as Draft (১-ক্লিক)";

      if (data.success) {
        resultBox.style.display = "block";
        liveResultContent.innerHTML = `
          <p><strong>পোস্ট আইডি:</strong> <code>${data.post_id}</code></p>
          <p><strong>স্ট্যাটাস:</strong> ${data.is_draft ? "ব্লগারে ড্রাফট হিসেবে সংরক্ষিত" : "ব্লগে পাবলিকলি লাইভ প্রকাশিত"}</p>
          ${data.url ? `<p class="result-link-item"><strong>লাইভ পোস্টের ইউআরএল:</strong> <a href="${data.url}" target="_blank">${data.url}</a></p>` : ""}
          <p style="color: #16a34a; font-size: 13px; margin-top: 6px;">✔ গুগল ইনডেক্সিং এপিআই এবং ৬টি ফিড হাবে পিং পাঠানো হয়েছে।</p>
        `;
        resultBox.scrollIntoView({ behavior: 'smooth' });
      } else {
        alert("পাবলিশিং ত্রুটি: " + data.error);
      }
    })
    .catch(err => {
      btnApproveAndPublish.disabled = false;
      btnApproveAndPublish.textContent = isLive ? "🚀 Approve & Publish to Blogger (১-ক্লিক)" : "💾 Approve & Save as Draft (১-ক্লিক)";
      alert("নেটওয়ার্ক ত্রুটি: " + err);
    });
  });

  function showStep(stepNum) {
    step1Card.style.display = stepNum === 1 ? "block" : "none";
    step2Card.style.display = stepNum === 2 ? "block" : "none";
    step3Card.style.display = stepNum === 3 ? "block" : "none";

    stepIndicator1.className = stepNum === 1 ? "step active" : "step";
    stepIndicator2.className = stepNum === 2 ? "step active" : "step";
    stepIndicator3.className = stepNum === 3 ? "step active" : "step";

    window.scrollTo({ top: 0, behavior: 'smooth' });
  }

  function jsonBody(obj) {
    return JSON.stringify(obj);
  }
});
