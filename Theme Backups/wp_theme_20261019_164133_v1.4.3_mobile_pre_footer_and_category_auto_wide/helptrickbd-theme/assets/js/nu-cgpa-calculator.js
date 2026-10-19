
(function() {
  // ---------------------------------------------------------------------------
  // BLOGGER HTML ENTITY SCRUBBER & DECODER
  // ---------------------------------------------------------------------------
  function _bn(str) {
    if (!str || typeof str !== 'string') return str;
    if (str.indexOf('&') === -1) return str;
    const txt = document.createElement('textarea');
    txt.innerHTML = str;
    return txt.value;
  }

  function scrubEntities(root) {
    if (!root) return;
    const walker = document.createTreeWalker(root, NodeFilter.SHOW_TEXT, null, false);
    let node;
    while ((node = walker.nextNode())) {
      if (node.nodeValue && node.nodeValue.indexOf('&#') !== -1) {
        node.nodeValue = _bn(node.nodeValue);
      }
    }
  }

  // 1. SYLLABUS DATABASE
  const SYLLABUS = {"political_science": {"name": "রাষ্ট্রবিজ্ঞান (Political Science)", "years": {"1": [{"code": "211901", "name": "Introduction to Political Science: Basic Concepts", "credit": 4}, {"code": "211903", "name": "Political Organization & Political System (UK & USA)", "credit": 4}, {"code": "211501", "name": "History of the Emergence of Independent Bangladesh", "credit": 4}, {"code": "212009", "name": "Introducing Sociology / Social Anthropology", "credit": 4}, {"code": "212209", "name": "Principles of Economics", "credit": 4}, {"code": "212111", "name": "Bangla National Culture / Foundation English", "credit": 4}], "2": [{"code": "221901", "name": "Political Organizations and The Political Systems of UK and USA", "credit": 4}, {"code": "221903", "name": "Political Thought: Ancient and Medieval", "credit": 4}, {"code": "221905", "name": "Public Administration in Bangladesh", "credit": 4}, {"code": "222009", "name": "Bangladesh Society and Culture", "credit": 4}, {"code": "221609", "name": "History of Western World", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "231901", "name": "Modern Political Thought", "credit": 4}, {"code": "231903", "name": "Comparative Politics", "credit": 4}, {"code": "231905", "name": "Politics and Governance in South Asia", "credit": 4}, {"code": "231907", "name": "International Politics: Theory and Practice", "credit": 4}, {"code": "231909", "name": "Research Methodology and Statistics", "credit": 4}, {"code": "231911", "name": "Political Sociology", "credit": 4}, {"code": "231913", "name": "Women in Politics and Development", "credit": 4}, {"code": "231915", "name": "Peace and Conflict Studies", "credit": 4}], "4": [{"code": "241901", "name": "Local Government and Rural Development in Bangladesh", "credit": 4}, {"code": "241903", "name": "Public Policy and Governance", "credit": 4}, {"code": "241905", "name": "Human Rights and Social Justice", "credit": 4}, {"code": "241907", "name": "Foreign Policy of Major Powers", "credit": 4}, {"code": "241909", "name": "Security Studies and Arms Control", "credit": 4}, {"code": "241911", "name": "Environmental Politics and Development", "credit": 4}, {"code": "241913", "name": "Politics of Middle East", "credit": 4}, {"code": "241915", "name": "Constitutional Development of Bangladesh", "credit": 4}, {"code": "241918", "name": "Comprehensive / Viva-Voce", "credit": 4}]}}, "english": {"name": "ইংরেজি (English)", "years": {"1": [{"code": "211101", "name": "English Reading Skills", "credit": 4}, {"code": "211103", "name": "English Writing Skills", "credit": 4}, {"code": "211105", "name": "Introduction to Poetry", "credit": 4}, {"code": "211107", "name": "Introduction to Prose (Fiction & Non-Fiction)", "credit": 4}, {"code": "211501", "name": "History of the Emergence of Independent Bangladesh", "credit": 4}, {"code": "211909", "name": "Political Science / History Subsidiary", "credit": 4}], "2": [{"code": "221101", "name": "Introduction to Drama", "credit": 4}, {"code": "221103", "name": "Romantic Poetry", "credit": 4}, {"code": "221105", "name": "Advanced Reading and Writing", "credit": 4}, {"code": "221107", "name": "History of English Literature", "credit": 4}, {"code": "221909", "name": "Subsidiary Course - II", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "231101", "name": "Victorian Poetry", "credit": 4}, {"code": "231103", "name": "19th Century English Novel", "credit": 4}, {"code": "231105", "name": "17th Century English Poetry and Drama", "credit": 4}, {"code": "231107", "name": "Shakespeare", "credit": 4}, {"code": "231109", "name": "Introduction to Linguistics", "credit": 4}, {"code": "231111", "name": "Literary Criticism", "credit": 4}, {"code": "231113", "name": "American Literature", "credit": 4}, {"code": "231115", "name": "African Literature in English", "credit": 4}], "4": [{"code": "241101", "name": "Modern Poetry", "credit": 4}, {"code": "241103", "name": "Modern Drama", "credit": 4}, {"code": "241105", "name": "Modern Novel", "credit": 4}, {"code": "241107", "name": "Classics in Translation", "credit": 4}, {"code": "241109", "name": "ELT (English Language Teaching)", "credit": 4}, {"code": "241111", "name": "South Asian Literature in English", "credit": 4}, {"code": "241113", "name": "Continental Literature", "credit": 4}, {"code": "241115", "name": "Post-Colonial Literature", "credit": 4}, {"code": "241120", "name": "Viva-Voce", "credit": 4}]}}, "accounting": {"name": "হিসাববিজ্ঞান (Accounting)", "years": {"1": [{"code": "212501", "name": "Principles of Accounting", "credit": 4}, {"code": "212503", "name": "Principles of Finance", "credit": 4}, {"code": "212505", "name": "Principles of Marketing", "credit": 4}, {"code": "212507", "name": "Principles of Management", "credit": 4}, {"code": "212509", "name": "Business Mathematics", "credit": 4}, {"code": "211501", "name": "History of the Emergence of Independent Bangladesh", "credit": 4}], "2": [{"code": "222501", "name": "Intermediate Accounting", "credit": 4}, {"code": "222503", "name": "Business Communication and Report Writing", "credit": 4}, {"code": "222505", "name": "Business Statistics", "credit": 4}, {"code": "222507", "name": "Taxation in Bangladesh", "credit": 4}, {"code": "222509", "name": "Business Law", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "232501", "name": "Cost Accounting", "credit": 4}, {"code": "232503", "name": "Management Accounting", "credit": 4}, {"code": "232505", "name": "Audit and Assurance", "credit": 4}, {"code": "232507", "name": "Financial Management", "credit": 4}, {"code": "232509", "name": "Advanced Accounting - I", "credit": 4}, {"code": "232511", "name": "Banking and Insurance", "credit": 4}, {"code": "232513", "name": "Company Law", "credit": 4}, {"code": "232515", "name": "Macro Economics", "credit": 4}], "4": [{"code": "242501", "name": "Advanced Accounting - II", "credit": 4}, {"code": "242503", "name": "Accounting Theory", "credit": 4}, {"code": "242505", "name": "Cost Management", "credit": 4}, {"code": "242507", "name": "Advanced Auditing & Professional Ethics", "credit": 4}, {"code": "242509", "name": "Public Sector Accounting & Finance", "credit": 4}, {"code": "242511", "name": "Research Methodology", "credit": 4}, {"code": "242513", "name": "International Accounting", "credit": 4}, {"code": "242515", "name": "Project Management", "credit": 4}, {"code": "242518", "name": "Viva-Voce", "credit": 4}]}}, "management": {"name": "ব্যবস্থাপনা (Management)", "years": {"1": [{"code": "212601", "name": "Introduction to Business", "credit": 4}, {"code": "212603", "name": "Principles of Management", "credit": 4}, {"code": "212605", "name": "Principles of Accounting", "credit": 4}, {"code": "212607", "name": "Principles of Marketing", "credit": 4}, {"code": "212609", "name": "Business Mathematics", "credit": 4}, {"code": "211501", "name": "History of Independent Bangladesh", "credit": 4}], "2": [{"code": "222601", "name": "Human Resource Management", "credit": 4}, {"code": "222603", "name": "Business Communication", "credit": 4}, {"code": "222605", "name": "Business Statistics", "credit": 4}, {"code": "222607", "name": "Legal Environment of Business", "credit": 4}, {"code": "222609", "name": "Principles of Finance", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "232601", "name": "Operations Management", "credit": 4}, {"code": "232603", "name": "Organizational Behavior", "credit": 4}, {"code": "232605", "name": "Financial Management", "credit": 4}, {"code": "232607", "name": "Marketing Management", "credit": 4}, {"code": "232609", "name": "Cost Accounting", "credit": 4}, {"code": "232611", "name": "Taxation in Bangladesh", "credit": 4}, {"code": "232613", "name": "Company Law", "credit": 4}, {"code": "232615", "name": "Macro Economics", "credit": 4}], "4": [{"code": "242601", "name": "Strategic Management", "credit": 4}, {"code": "242603", "name": "Bank Management", "credit": 4}, {"code": "242605", "name": "Supply Chain Management", "credit": 4}, {"code": "242607", "name": "Industrial Relations", "credit": 4}, {"code": "242609", "name": "Project Management", "credit": 4}, {"code": "242611", "name": "International Business", "credit": 4}, {"code": "242613", "name": "Total Quality Management", "credit": 4}, {"code": "242615", "name": "E-Commerce", "credit": 4}, {"code": "242618", "name": "Viva-Voce", "credit": 4}]}}, "economics": {"name": "অর্থনীতি (Economics)", "years": {"1": [{"code": "212201", "name": "Basic Microeconomics", "credit": 4}, {"code": "212203", "name": "Basic Macroeconomics", "credit": 4}, {"code": "212205", "name": "Basic Mathematics for Economics", "credit": 4}, {"code": "212207", "name": "Basic Statistics for Economics", "credit": 4}, {"code": "211501", "name": "History of Independent Bangladesh", "credit": 4}, {"code": "212009", "name": "Introducing Sociology", "credit": 4}], "2": [{"code": "222201", "name": "Intermediate Microeconomics", "credit": 4}, {"code": "222203", "name": "Mathematical Economics", "credit": 4}, {"code": "222205", "name": "Statistical Methods for Economics", "credit": 4}, {"code": "222207", "name": "Economy of Bangladesh", "credit": 4}, {"code": "221909", "name": "Political Science Subsidiary", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "232201", "name": "Intermediate Macroeconomics", "credit": 4}, {"code": "232203", "name": "International Trade", "credit": 4}, {"code": "232205", "name": "Public Finance", "credit": 4}, {"code": "232207", "name": "Introduction to Econometrics", "credit": 4}, {"code": "232209", "name": "Agricultural Economics", "credit": 4}, {"code": "232211", "name": "Money and Banking", "credit": 4}, {"code": "232213", "name": "Research Methodology", "credit": 4}, {"code": "232215", "name": "Demography and Population Studies", "credit": 4}], "4": [{"code": "242201", "name": "Development Economics", "credit": 4}, {"code": "242203", "name": "International Finance", "credit": 4}, {"code": "242205", "name": "Applied Econometrics", "credit": 4}, {"code": "242207", "name": "Environmental and Resource Economics", "credit": 4}, {"code": "242209", "name": "Labor Economics", "credit": 4}, {"code": "242211", "name": "Health Economics", "credit": 4}, {"code": "242213", "name": "Economic History of Modern World", "credit": 4}, {"code": "242215", "name": "Urban and Regional Economics", "credit": 4}, {"code": "242218", "name": "Viva-Voce", "credit": 4}]}}, "sociology": {"name": "সমাজবিজ্ঞান (Sociology)", "years": {"1": [{"code": "212001", "name": "Introductory Sociology", "credit": 4}, {"code": "212003", "name": "Social History of the World", "credit": 4}, {"code": "211501", "name": "History of Independent Bangladesh", "credit": 4}, {"code": "211909", "name": "Political Science Subsidiary", "credit": 4}, {"code": "212209", "name": "Economics Subsidiary", "credit": 4}, {"code": "212111", "name": "Social Anthropology", "credit": 4}], "2": [{"code": "222001", "name": "Classical Sociological Theory", "credit": 4}, {"code": "222003", "name": "Social Structure of Bangladesh", "credit": 4}, {"code": "222005", "name": "Sociology of Religion", "credit": 4}, {"code": "222007", "name": "Social Problems and Social Policy", "credit": 4}, {"code": "221909", "name": "Subsidiary Course", "credit": 4}, {"code": "221109", "name": "English (Compulsory - Non Credit)", "credit": 0}], "3": [{"code": "232001", "name": "Modern Sociological Theory", "credit": 4}, {"code": "232003", "name": "Social Research Methods", "credit": 4}, {"code": "232005", "name": "Social Statistics", "credit": 4}, {"code": "232007", "name": "Rural Sociology", "credit": 4}, {"code": "232009", "name": "Urban Sociology", "credit": 4}, {"code": "232011", "name": "Political Sociology", "credit": 4}, {"code": "232013", "name": "Sociology of Development", "credit": 4}, {"code": "232015", "name": "Gender and Society", "credit": 4}], "4": [{"code": "242001", "name": "Contemporary Sociological Theory", "credit": 4}, {"code": "242003", "name": "Sociology of Environment", "credit": 4}, {"code": "242005", "name": "Criminology and Penology", "credit": 4}, {"code": "242007", "name": "Industrial Sociology", "credit": 4}, {"code": "242009", "name": "Demography and Population Studies", "credit": 4}, {"code": "242011", "name": "Social Inequality and Stratification", "credit": 4}, {"code": "242013", "name": "Sociology of Health and Illness", "credit": 4}, {"code": "242015", "name": "Globalization and Society", "credit": 4}, {"code": "242018", "name": "Viva-Voce", "credit": 4}]}}};

  // Grade point mapping
  const GRADE_SCALE = {
    "A+": 4.00,
    "A": 3.75,
    "A-": 3.50,
    "B+": 3.25,
    "B": 3.00,
    "B-": 2.75,
    "C+": 2.50,
    "C": 2.25,
    "D": 2.00,
    "F": 0.00
  };

  // State
  let currentProgram = 'honours'; // honours, degree, masters
  let currentMode = 'mode-year';

  // DOM Elements
  const progBtns = document.querySelectorAll('.htbd-prog-btn');
  const tabBtns = document.querySelectorAll('.htbd-tab-btn');
  const modePanels = document.querySelectorAll('.htbd-mode-panel');

  const dashGaugeCircle = document.getElementById('dash-gauge-circle');
  const dashCgpaVal = document.getElementById('dash-cgpa-val');
  const dashDivisionBadge = document.getElementById('dash-division-badge');
  const dashTotalCredits = document.getElementById('dash-total-credits');
  const dashTotalPoints = document.getElementById('dash-total-points');
  const dashProgramBadge = document.getElementById('dash-program-badge');
  const dashTrendLine = document.getElementById('dash-trend-line');
  const dashTrendTitle = document.getElementById('dash-trend-title');
  const dashTrendSub = document.getElementById('dash-trend-sub');
  const dashTrendPoints = document.getElementById('dash-trend-points');

  // Program switching (Clean Class Toggle, Zero Inline Style Pollution)
  progBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      progBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentProgram = btn.dataset.prog;
      updateProgramUI();
      calculateYearMode();
    });
  });

  function updateProgramUI() {
    const y3Card = document.querySelector('.htbd-year-card[data-year="3"]');
    const y4Card = document.querySelector('.htbd-year-card[data-year="4"]');

    if (currentProgram === 'honours') {
      dashProgramBadge.textContent = _bn('স্নাতক (সম্মান)');
      if (y3Card) y3Card.style.display = 'block';
      if (y4Card) y4Card.style.display = 'block';
    } else if (currentProgram === 'degree') {
      dashProgramBadge.textContent = _bn('ডিগ্রি (পাস)');
      if (y3Card) y3Card.style.display = 'block';
      if (y4Card) y4Card.style.display = 'none';
    } else if (currentProgram === 'masters') {
      dashProgramBadge.textContent = _bn('মাস্টার্স');
      if (y3Card) y3Card.style.display = 'none';
      if (y4Card) y4Card.style.display = 'none';
    }
  }

  // Tab switching (Clean Class Toggle, Zero Inline Style Pollution)
  tabBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      tabBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      currentMode = btn.dataset.mode;
      modePanels.forEach(p => p.style.display = 'none');
      const targetPanel = document.getElementById('panel-' + currentMode);
      if (targetPanel) targetPanel.style.display = 'block';

      if (currentMode === 'mode-year') calculateYearMode();
      if (currentMode === 'mode-subject') calculateSubjectMode();
      if (currentMode === 'mode-target') calculateTargetMode();
      if (currentMode === 'mode-improvement') calculateImprovementMode();
    });
  });

  // ---------------------------------------------------------------------------
  // MODE 1: YEAR-WISE CALCULATION
  // ---------------------------------------------------------------------------
  const yearCards = document.querySelectorAll('.htbd-year-card');

  yearCards.forEach(card => {
    const range = card.querySelector('.htbd-yr-range');
    const input = card.querySelector('.htbd-yr-gpa');
    const credit = card.querySelector('.htbd-yr-credit');

    range.addEventListener('input', () => {
      input.value = parseFloat(range.value).toFixed(2);
      calculateYearMode();
    });

    input.addEventListener('input', () => {
      let raw = input.value.trim();
      if (raw === '') {
        range.value = 0;
      } else {
        let val = parseFloat(raw) || 0;
        if (val > 4) val = 4;
        if (val < 0) val = 0;
        range.value = val;
      }
      calculateYearMode();
    });

    credit.addEventListener('input', calculateYearMode);
  });

  function calculateYearMode() {
    let totalPoints = 0;
    let totalCredits = 0;
    let yearGpas = [];

    yearCards.forEach(card => {
      const year = parseInt(card.dataset.year);
      if (currentProgram === 'degree' && year > 3) return;
      if (currentProgram === 'masters' && year > 2) return;

      const input = card.querySelector('.htbd-yr-gpa');
      const credit = card.querySelector('.htbd-yr-credit');
      const rawVal = input.value.trim();

      if (rawVal !== '') {
        const gpa = parseFloat(rawVal);
        const cr = parseFloat(credit.value) || 0;
        if (!isNaN(gpa) && cr > 0) {
          totalPoints += (gpa * cr);
          totalCredits += cr;
          yearGpas.push(gpa);
          return;
        }
      }
      yearGpas.push(null); // not entered
    });

    const cgpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
    updateDashboard(cgpa, totalCredits, totalPoints, yearGpas, {
      title: _bn('বর্ষভিত্তিক অগ্রগতি গ্রাফ'),
      sub: _bn('১ম → ৪র্থ বর্ষ'),
      type: 'year'
    });
    saveState();
  }

  document.getElementById('btn-reset-year').addEventListener('click', () => {
    yearCards.forEach(card => {
      card.querySelector('.htbd-yr-gpa').value = '';
      card.querySelector('.htbd-yr-range').value = 0;
    });
    calculateYearMode();
  });

  // ---------------------------------------------------------------------------
  // DASHBOARD UPDATER (PURE CSS BADGES & GAUGE ACCURACY)
  // ---------------------------------------------------------------------------
  function getDivisionText(cgpa, credits) {
    if (credits === 0 || cgpa === 0) return _bn('পয়েন্ট বা গ্রেড ইনপুট দিন');
    if (cgpa >= 3.00) return _bn('First Class (১ম শ্রেণি)');
    if (cgpa >= 2.25) return _bn('Second Class (২য় শ্রেণি)');
    if (cgpa >= 2.00) return _bn('Third Class (৩য় শ্রেণি)');
    return _bn('নট প্রমোটেড / ডিগ্রি অপ্রাপ্ত');
  }

  function updateDashboard(cgpa, credits, points, trendData, trendConfig) {
    const formattedCgpa = cgpa.toFixed(2);
    dashCgpaVal.textContent = formattedCgpa;
    dashTotalCredits.textContent = credits;
    dashTotalPoints.textContent = points.toFixed(2);

    // Update Circular Gauge
    const circumference = 314.16;
    const progress = Math.min(Math.max(cgpa / 4.00, 0), 1);
    const offset = circumference - (progress * circumference);
    dashGaugeCircle.style.strokeDashoffset = offset;

    // Remove old badge classes
    dashDivisionBadge.className = 'htbd-badge';

    let strokeColor = '#2563eb';
    const divText = getDivisionText(cgpa, credits);
    dashDivisionBadge.textContent = _bn(divText);
    scrubEntities(dashDivisionBadge);

    if (credits === 0 || cgpa === 0) {
      strokeColor = '#94a3b8';
      dashDivisionBadge.classList.add('htbd-badge-empty');
      dashGaugeCircle.style.strokeDashoffset = circumference;
    } else if (cgpa >= 3.00) {
      strokeColor = '#15803d'; // Emerald
      dashDivisionBadge.classList.add('htbd-badge-first');
    } else if (cgpa >= 2.25) {
      strokeColor = '#2563eb'; // Blue
      dashDivisionBadge.classList.add('htbd-badge-second');
    } else if (cgpa >= 2.00) {
      strokeColor = '#d97706'; // Amber
      dashDivisionBadge.classList.add('htbd-badge-third');
    } else {
      strokeColor = '#dc2626'; // Red
      dashDivisionBadge.classList.add('htbd-badge-fail');
    }

    dashGaugeCircle.style.stroke = strokeColor;

    // Adaptive Dynamic Trend Graph
    const cfg = trendConfig || {
      title: _bn('বর্ষভিত্তিক অগ্রগতি গ্রাফ'),
      sub: _bn('১ম → ৪র্থ বর্ষ'),
      type: 'year'
    };

    if (dashTrendTitle) {
      dashTrendTitle.textContent = cfg.title;
      scrubEntities(dashTrendTitle);
    }
    if (dashTrendSub) {
      dashTrendSub.textContent = cfg.sub;
      scrubEntities(dashTrendSub);
    }

    if (dashTrendPoints && dashTrendLine) {
      dashTrendPoints.innerHTML = '';
      let validPoints = [];

      if (cfg.type === 'course') {
        // Course-wise mode: trendData is array of label and val
        const list = Array.isArray(trendData) ? trendData : [];
        if (list.length > 0) {
          const count = list.length;
          const startX = 20;
          const endX = 180;
          const stepX = count > 1 ? ((endX - startX) / (count - 1)) : 0;

          list.forEach((item, idx) => {
            const val = (item && typeof item === 'object') ? item.val : item;
            if (val !== null && !isNaN(val)) {
              const x = count === 1 ? 100 : Math.round(startX + (idx * stepX));
              const y = 50 - (Math.min(Math.max(val / 4.00, 0), 1) * 40);
              const yFixed = y.toFixed(1);
              validPoints.push(x + ',' + yFixed);

              const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
              circle.setAttribute('cx', x);
              circle.setAttribute('cy', yFixed);
              circle.setAttribute('r', '4');
              circle.setAttribute('fill', '#1e40af');
              circle.setAttribute('stroke', '#ffffff');
              circle.setAttribute('stroke-width', '1.5');
              circle.style.transition = 'all 0.3s ease';

              const titleElem = document.createElementNS('http://www.w3.org/2000/svg', 'title');
              const lbl = (item && item.label) ? item.label : ('কোর্স ' + (idx + 1));
              titleElem.textContent = lbl + ': ' + val.toFixed(2) + ' GP';
              circle.appendChild(titleElem);

              dashTrendPoints.appendChild(circle);
            }
          });

          if (validPoints.length >= 2) {
            dashTrendLine.setAttribute('points', validPoints.join(' '));
            dashTrendLine.style.opacity = '1';
          } else if (validPoints.length === 1) {
            dashTrendLine.setAttribute('points', validPoints[0] + ' ' + validPoints[0]);
            dashTrendLine.style.opacity = '0.5';
          } else {
            dashTrendLine.setAttribute('points', '10,50 190,50');
            dashTrendLine.style.opacity = '0.2';
          }
        } else {
          dashTrendLine.setAttribute('points', '10,50 190,50');
          dashTrendLine.style.opacity = '0.2';
        }
      } else {
        // Year mode: trendData is array of numbers or nulls [y1, y2, y3, y4]
        const xCoords = [20, 70, 120, 170];
        const list = Array.isArray(trendData) ? trendData : [];

        xCoords.forEach((x, i) => {
          const val = list[i];
          const hasVal = (val !== null && val !== undefined && !isNaN(val) && val > 0);
          const y = hasVal ? (50 - (Math.min(Math.max(val / 4.00, 0), 1) * 40)) : 50;
          const yFixed = y.toFixed(1);

          if (hasVal) {
            validPoints.push(x + ',' + yFixed);
          }

          const circle = document.createElementNS('http://www.w3.org/2000/svg', 'circle');
          circle.setAttribute('cx', x);
          circle.setAttribute('cy', yFixed);
          circle.setAttribute('r', hasVal ? '4' : '3');
          circle.setAttribute('fill', '#1e40af');
          circle.setAttribute('stroke', '#ffffff');
          circle.setAttribute('stroke-width', hasVal ? '1.5' : '1');
          circle.style.opacity = hasVal ? '1' : '0.25';
          circle.style.transition = 'all 0.3s ease';

          const titleElem = document.createElementNS('http://www.w3.org/2000/svg', 'title');
          titleElem.textContent = (i + 1) + 'ম বর্ষ: ' + (hasVal ? val.toFixed(2) + ' GPA' : 'ইনপুট নেই');
          circle.appendChild(titleElem);

          dashTrendPoints.appendChild(circle);
        });

        if (validPoints.length >= 2) {
          dashTrendLine.setAttribute('points', validPoints.join(' '));
          dashTrendLine.style.opacity = '1';
        } else if (validPoints.length === 1) {
          dashTrendLine.setAttribute('points', validPoints[0] + ' ' + validPoints[0]);
          dashTrendLine.style.opacity = '0.5';
        } else {
          dashTrendLine.setAttribute('points', '20,50 70,50 120,50 170,50');
          dashTrendLine.style.opacity = '0.2';
        }
      }
    }
  }

  // ---------------------------------------------------------------------------
  // MODE 2: COURSE-WISE DETAILED GPA
  // ---------------------------------------------------------------------------
  const coursesContainer = document.getElementById('courses-container');
  const btnAddCourse = document.getElementById('btn-add-course');
  const btnResetCourses = document.getElementById('btn-reset-courses');
  const btnLoadSyllabus = document.getElementById('btn-load-syllabus');
  const selDept = document.getElementById('sel-dept');
  const selYear = document.getElementById('sel-year');

  function createCourseRow(code = '', name = '', credit = 4, selectedGrade = '', exactPoint = '') {
    const row = document.createElement('div');
    row.className = 'htbd-course-row';

    let initialPoint = '';
    if (exactPoint !== null && exactPoint !== '' && !isNaN(exactPoint)) {
      initialPoint = parseFloat(exactPoint).toFixed(2);
    } else if (selectedGrade && GRADE_SCALE[selectedGrade] !== undefined) {
      initialPoint = GRADE_SCALE[selectedGrade].toFixed(2);
    }

    const displayName = name ? code + ' - ' + name : code;
    const cOpts = [[4,'৪ ক্রেডিট'],[3,'৩ ক্রেডিট'],[2,'২ ক্রেডিট'],[0,'নন-ক্রেডিট']]
      .map(([v,t]) => `<option value="${v}" ${credit === v ? 'selected' : ''}>${t}</option>`).join('');
    const gOpts = [['','-- গ্রেড --'],['A+','A+ (4.00)'],['A','A (3.75)'],['A-','A- (3.50)'],
      ['B+','B+ (3.25)'],['B','B (3.00)'],['B-','B- (2.75)'],['C+','C+ (2.50)'],['C','C (2.25)'],['D','D (2.00)'],['F','F (0.00)']]
      .map(([v,t]) => `<option value="${v}" ${selectedGrade === v ? 'selected' : ''}>${t}</option>`).join('');

    row.innerHTML = `
      <div class="cr-top">
        <div class="cr-name">
          <input type="text" class="c-name" value="${displayName}"
            placeholder="কোর্স কোড ও নাম"
            style="width:100%;box-sizing:border-box;padding:7px 10px;border:1px solid #cbd5e1;border-radius:6px;font-size:13.5px;" />
        </div>
        <div class="cr-del-wrap">
          <button type="button" class="btn-del-course" title="কোর্স মুছুন">×</button>
        </div>
      </div>
      <div class="cr-controls">
        <div class="cr-col cr-col-credit">
          <span class="cr-label">ক্রেডিট</span>
          <select class="c-credit" style="width:100%;box-sizing:border-box;padding:7px 4px;border:1px solid #cbd5e1;border-radius:6px;font-size:13px;text-align:center;">
            ${cOpts}
          </select>
        </div>
        <div class="cr-col cr-col-grade">
          <span class="cr-label">লেটার গ্রেড</span>
          <select class="c-grade" style="width:100%;box-sizing:border-box;padding:7px 4px;border:1px solid #cbd5e1;border-radius:6px;font-size:13px;font-weight:700;">
            ${gOpts}
          </select>
        </div>
        <div class="cr-col cr-col-point">
          <span class="cr-label">পয়েন্ট (GP)</span>
          <input type="number" class="c-point"
            min="0.00" max="4.00" step="0.01"
            value="${initialPoint}"
            placeholder="0.00"
            style="width:100%;box-sizing:border-box;padding:7px 4px;border:1.5px solid #94a3b8;border-radius:6px;font-size:14px;font-weight:700;text-align:center;"
            title="পয়েন্ট টাইপ করলে গ্রেড অটো-সিলেক্ট হবে" />
        </div>
      </div>
    `;

    const cCredit = row.querySelector('.c-credit');
    const cGrade  = row.querySelector('.c-grade');
    const cPoint  = row.querySelector('.c-point');
    const btnDel  = row.querySelector('.btn-del-course');

    // Grade dropdown -> Point input (Sync)
    cGrade.addEventListener('change', () => {
      const gr = cGrade.value;
      if (gr && GRADE_SCALE[gr] !== undefined) {
        cPoint.value = GRADE_SCALE[gr].toFixed(2);
      } else if (gr === '') {
        cPoint.value = '';
      }
      calculateSubjectMode();
    });

    // Point input -> Auto Select matching Letter Grade
    const syncPointToGrade = () => {
      const rawVal = cPoint.value.trim();
      if (rawVal === '') {
        cGrade.value = '';
        calculateSubjectMode();
        return;
      }
      let p = parseFloat(rawVal);
      if (isNaN(p)) {
        cGrade.value = '';
        calculateSubjectMode();
        return;
      }
      if (p > 4.00) p = 4.00;
      if (p < 0.00) p = 0.00;

      let g = 'F';
      if      (p >= 4.00) g = 'A+';
      else if (p >= 3.75) g = 'A';
      else if (p >= 3.50) g = 'A-';
      else if (p >= 3.25) g = 'B+';
      else if (p >= 3.00) g = 'B';
      else if (p >= 2.75) g = 'B-';
      else if (p >= 2.50) g = 'C+';
      else if (p >= 2.25) g = 'C';
      else if (p >= 2.00) g = 'D';

      cGrade.value = g;
      calculateSubjectMode();
    };

    cPoint.addEventListener('input', syncPointToGrade);
    cPoint.addEventListener('keyup', syncPointToGrade);
    cPoint.addEventListener('change', syncPointToGrade);

    cCredit.addEventListener('change', calculateSubjectMode);
    btnDel.addEventListener('click', () => {
      row.remove();
      calculateSubjectMode();
    });

    coursesContainer.appendChild(row);
  }

  function calculateSubjectMode() {
    const rows = document.querySelectorAll('.htbd-course-row');
    let totalPoints = 0;
    let totalCredits = 0;
    let courseData = [];

    rows.forEach((r, idx) => {
      const cr = parseFloat(r.querySelector('.c-credit').value) || 0;
      const rawVal = r.querySelector('.c-point').value.trim();
      const nameInput = r.querySelector('.c-name');
      let cLabel = nameInput && nameInput.value.trim() ? nameInput.value.trim() : ('কোর্স ' + (idx + 1));
      if (cLabel.length > 25) cLabel = cLabel.substring(0, 22) + '...';

      if (rawVal !== '') {
        const gp = parseFloat(rawVal);
        if (!isNaN(gp) && cr > 0) {
          totalPoints += (cr * gp);
          totalCredits += cr;
          courseData.push({ label: cLabel, val: gp });
        }
      }
    });

    const gpa = totalCredits > 0 ? (totalPoints / totalCredits) : 0;
    updateDashboard(gpa, totalCredits, totalPoints, courseData, {
      title: _bn('কোর্সভিত্তিক পয়েন্ট বিশ্লেষণ'),
      sub: _bn('কোর্স ১ → শেষ কোর্স'),
      type: 'course'
    });
  }

  btnAddCourse.addEventListener('click', () => {
    const count = document.querySelectorAll('.htbd-course-row').length + 1;
    const name = 'কোর্স ' + (count < 10 ? '০' : '') + count;
    createCourseRow(name, '', 4, '', '');
    calculateSubjectMode();
  });

  btnResetCourses.addEventListener('click', () => {
    coursesContainer.innerHTML = '';
    createCourseRow('কোর্স ০১', '', 4, '', '');
    createCourseRow('কোর্স ০২', '', 4, '', '');
    createCourseRow('কোর্স ০৩', '', 4, '', '');
    createCourseRow('কোর্স ০৪', '', 4, '', '');
    createCourseRow('কোর্স ০৫', '', 4, '', '');
    createCourseRow('কোর্স ০৬', '', 4, '', '');
    calculateSubjectMode();
  });

  // Load syllabus on click
  btnLoadSyllabus.addEventListener('click', () => {
    const dept = selDept.value;
    const year = selYear.value;

    if (SYLLABUS[dept] && SYLLABUS[dept].years && SYLLABUS[dept].years[year]) {
      coursesContainer.innerHTML = '';
      const list = SYLLABUS[dept].years[year];
      list.forEach(c => {
        createCourseRow(c.code, c.name, c.credit, '', '');
      });
      calculateSubjectMode();
    } else {
      alert('এই বিভাগের জন্য কাস্টম কোর্স যোগ করুন।');
    }
  });

  // Smart Paste Parser
  const smartPasteBox = document.getElementById('smart-paste-box');
  const btnOpenSmartPaste = document.getElementById('btn-open-smart-paste');
  const btnCancelPaste = document.getElementById('btn-cancel-paste');
  const btnParsePaste = document.getElementById('btn-parse-paste');
  const smartPasteInput = document.getElementById('smart-paste-input');

  btnOpenSmartPaste.addEventListener('click', () => {
    smartPasteBox.style.display = 'block';
  });

  btnCancelPaste.addEventListener('click', () => {
    smartPasteBox.style.display = 'none';
  });

  btnParsePaste.addEventListener('click', () => {
    const raw = smartPasteInput.value;
    if (!raw.trim()) return;

    const pattern = /(\d{6})\s*[-:\s]*\s*([A-DF][+-]?|\d+(?:\.\d+)?)/gi;
    let match;
    let found = 0;

    coursesContainer.innerHTML = '';
    while ((match = pattern.exec(raw)) !== null) {
      const code = match[1];
      const valStr = match[2].trim().toUpperCase();
      const credit = (code === '221109') ? 0 : 4; // non credit english check

      const numVal = parseFloat(valStr);
      if (!isNaN(numVal) && numVal <= 4.00) {
        let matchedGrade = 'custom';
        for (const [g, val] of Object.entries(GRADE_SCALE)) {
          if (Math.abs(val - numVal) < 0.001) {
            matchedGrade = g;
            break;
          }
        }
        createCourseRow(code, '', credit, matchedGrade, numVal);
      } else {
        createCourseRow(code, '', credit, valStr);
      }
      found++;
    }

    if (found > 0) {
      smartPasteBox.style.display = 'none';
      smartPasteInput.value = '';
      calculateSubjectMode();
      alert(found + 'টি কোর্সের গ্রেড ও পয়েন্ট সফলভাবে অটো-ফিল করা হয়েছে!');
    } else {
      alert('সঠিক রেজাল্ট ফরম্যাট শনাক্ত করা যায়নি। অনুগ্রহ করে কোড ও গ্রেড বা পয়েন্ট (যেমন: 221901 A অথবা 221901 3.75) পেস্ট করুন।');
    }
  });

  // ---------------------------------------------------------------------------
  // MODE 3: TARGET FIRST CLASS PLANNER
  // ---------------------------------------------------------------------------
  const selCompletedYears = document.getElementById('target-completed-years');
  const inputCurrentCgpa = document.getElementById('target-current-cgpa');
  const selGoalCgpa = document.getElementById('target-goal-cgpa');
  const targetReqGpa = document.getElementById('target-req-gpa');
  const targetBadge = document.getElementById('target-badge');
  const targetAdvice = document.getElementById('target-advice');

  selCompletedYears.addEventListener('change', calculateTargetMode);
  inputCurrentCgpa.addEventListener('input', calculateTargetMode);
  selGoalCgpa.addEventListener('change', calculateTargetMode);

  function calculateTargetMode() {
    const completed = parseInt(selCompletedYears.value) || 2;
    const current = parseFloat(inputCurrentCgpa.value) || 2.75;
    const goal = parseFloat(selGoalCgpa.value) || 3.00;
    const remaining = 4 - completed;

    const totalRequired = (goal * 4) - (current * completed);
    const reqGpa = remaining > 0 ? (totalRequired / remaining) : goal;

    targetReqGpa.textContent = reqGpa > 0 ? reqGpa.toFixed(2) : '0.00';

    targetBadge.className = 'htbd-badge';

    if (reqGpa <= 3.10) {
      targetBadge.classList.add('htbd-target-easy');
      targetBadge.textContent = 'সহজসাধ্য ও বাস্তবসম্মত';
      targetAdvice.textContent = 'আপনার কাঙ্ক্ষিত ফলাফল অর্জন করা বেশ সহজ। নিয়মিত ক্লাসের পড়া শেষ করলেই আপনি ফার্স্ট ক্লাস নিশ্চিত করতে পারবেন।';
    } else if (reqGpa <= 3.45) {
      targetBadge.classList.add('htbd-target-medium');
      targetBadge.textContent = 'সম্ভব, নিয়মিত অধ্যবসায় প্রয়োজন';
      targetAdvice.textContent = 'বাকি বর্ষগুলোর প্রতিটি বিষয়ে কমপক্ষে B+ বা A- গ্রেড পেতে হবে। ইনকোর্স ও ব্যবহারিকে পুরো নম্বর তোলার চেষ্টা করুন।';
    } else if (reqGpa <= 3.85) {
      targetBadge.classList.add('htbd-target-hard');
      targetBadge.textContent = 'চ্যালেঞ্জিং, কঠোর প্রস্তুতি লাগবে';
      targetAdvice.textContent = 'আপনাকে প্রতিটি বিষয়ে A বা A+ গ্রেড পেতে হবে। প্রয়োজনে পূর্ববর্তী বছরের C বা D পাওয়া বিষয়ে মানোন্নয়ন পরীক্ষা দেওয়ার পরামর্শ রইল।';
    } else {
      targetBadge.classList.add('htbd-target-impossible');
      targetBadge.textContent = 'অসম্ভব (মানোন্নয়ন পরীক্ষা দিন)';
      targetAdvice.textContent = 'গাণিতিকভাবে ৪.০০ এর বেশি জিপিএ তোলা অসম্ভব। পূর্ববর্তী বর্ষগুলোর খারাপ হওয়া বিষয়ের মানোন্নয়ন (Improvement) পরীক্ষা দেওয়া ছাড়া ৩.০০ স্পর্শ করা সম্ভব নয়।';
    }

    if (currentMode === 'mode-target') {
      updateDashboard(goal, completed * 32, current * completed * 32, [
        { label: 'বর্তমান CGPA', val: current },
        { label: 'টার্গেট CGPA', val: goal },
        { label: 'প্রয়োজনীয় GPA', val: Math.min(Math.max(reqGpa, 0), 4) }
      ], {
        title: _bn('টার্গেট ও প্রয়োজনীয় ফলাফল'),
        sub: _bn('বর্তমান → লক্ষ্য → প্রয়োজনীয়'),
        type: 'course'
      });
    }
  }

  // ---------------------------------------------------------------------------
  // MODE 4: IMPROVEMENT SIMULATOR
  // ---------------------------------------------------------------------------
  const impCurrentGpa = document.getElementById('imp-current-gpa');
  const impNewGpa = document.getElementById('imp-new-gpa');
  const impDeltaGpa = document.getElementById('imp-delta-gpa');
  const impCoursesList = document.getElementById('imp-courses-list');
  const btnAddImpCourse = document.getElementById('btn-add-imp-course');

  function createImpRow(name = '', oldGp = '', newGp = '') {
    const row = document.createElement('div');
    row.className = 'imp-course-row';

    const oldVal = (oldGp !== '' && !isNaN(oldGp)) ? parseFloat(oldGp).toFixed(2) : '';
    const newVal = (newGp !== '' && !isNaN(newGp)) ? parseFloat(newGp).toFixed(2) : '';

    row.innerHTML = `
      <div class="imp-top">
        <div class="imp-name-wrap">
          <input type="text" class="imp-name" placeholder="কোর্স নাম / কোড" value="${name}" style="padding: 7px 10px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13px; box-sizing: border-box; width: 100%;" />
        </div>
        <div class="imp-del-wrap">
          <button type="button" class="btn-del-imp" title="মুছুন">×</button>
        </div>
      </div>
      <div class="imp-bottom">
        <div class="imp-col imp-col-old">
          <span class="imp-label">পূর্বের পয়েন্ট (GP)</span>
          <input type="number" class="imp-old-gp" min="0.00" max="4.00" step="0.01" value="${oldVal}" placeholder="2.00" style="padding: 7px 4px; border: 1px solid #cbd5e1; border-radius: 6px; font-size: 13.5px; font-weight: 700; text-align: center; box-sizing: border-box; width: 100%;" title="পূর্বের গ্রেড পয়েন্ট" />
        </div>
        <div class="imp-col imp-col-new">
          <span class="imp-label">টার্গেট পয়েন্ট (সর্বোচ্চ ৩.২৫)</span>
          <input type="number" class="imp-new-gp" min="0.00" max="3.25" step="0.01" value="${newVal}" placeholder="3.25" style="padding: 7px 4px; border: 1px solid #86efac; border-radius: 6px; font-size: 13.5px; font-weight: 700; color: #15803d; text-align: center; box-sizing: border-box; width: 100%;" title="প্রত্যাশিত নতুন পয়েন্ট (সর্বোচ্চ ৩.২৫)" />
        </div>
      </div>
    `;

    row.querySelector('.imp-old-gp').addEventListener('input', calculateImprovementMode);
    row.querySelector('.imp-new-gp').addEventListener('input', calculateImprovementMode);
    row.querySelector('.btn-del-imp').addEventListener('click', () => {
      row.remove();
      calculateImprovementMode();
    });

    impCoursesList.appendChild(row);
  }

  impCurrentGpa.addEventListener('input', calculateImprovementMode);
  if (btnAddImpCourse) {
    btnAddImpCourse.addEventListener('click', () => {
      const count = document.querySelectorAll('.imp-course-row').length + 1;
      createImpRow('কোর্স ' + (count < 10 ? '০' : '') + count, '', '');
      calculateImprovementMode();
    });
  }

  function calculateImprovementMode() {
    const currentGpa = parseFloat(impCurrentGpa.value) || 2.65;
    const defaultCredits = 32;
    let oldPoints = currentGpa * defaultCredits;
    let gainedPoints = 0;

    const impRows = document.querySelectorAll('.imp-course-row');
    impRows.forEach(r => {
      const oldRaw = r.querySelector('.imp-old-gp').value.trim();
      const newRaw = r.querySelector('.imp-new-gp').value.trim();

      if (oldRaw !== '' && newRaw !== '') {
        const oldGp = parseFloat(oldRaw) || 0;
        let newGp = parseFloat(newRaw) || 0;
        if (newGp > 3.25) newGp = 3.25; // NU B+ ordinance cap
        const cr = 4; // standard 4 credit
        if (newGp > oldGp) {
          gainedPoints += (newGp - oldGp) * cr;
        }
      }
    });

    const updatedPoints = oldPoints + gainedPoints;
    const finalGpa = updatedPoints / defaultCredits;
    const delta = finalGpa - currentGpa;

    impNewGpa.textContent = finalGpa.toFixed(2);
    impDeltaGpa.textContent = (delta >= 0 ? '+' : '') + delta.toFixed(2) + ' GPA';

    if (currentMode === 'mode-improvement') {
      updateDashboard(finalGpa, defaultCredits, updatedPoints, [
        { label: 'পূর্বের GPA', val: currentGpa },
        { label: 'নতুন সম্ভাব্য GPA', val: finalGpa }
      ], {
        title: _bn('মানোন্নয়ন অগ্রগতি তুলনা'),
        sub: _bn('পূর্বের → নতুন GPA'),
        type: 'course'
      });
    }
  }

  // ---------------------------------------------------------------------------
  // OFFICIAL ACADEMIC TRANSCRIPT & 1-PAGE PDF PRINT ENGINE
  // ---------------------------------------------------------------------------
  const btnPrint = document.getElementById('btn-print-transcript');
  const transcriptModal = document.getElementById('htbd-transcript-modal');
  const btnCloseModal = document.getElementById('btn-close-modal');
  const btnTriggerPdfPrint = document.getElementById('btn-trigger-pdf-print');

  const modalInpName = document.getElementById('modal-inp-name');
  const modalInpCollege = document.getElementById('modal-inp-college');
  const modalInpSession = document.getElementById('modal-inp-session');

  const certStudentName = document.getElementById('cert-student-name');
  const certCollegeName = document.getElementById('cert-college-name');
  const certRegSession = document.getElementById('cert-reg-session');
  const certProgramName = document.getElementById('cert-program-name');
  const certTotalCredits = document.getElementById('cert-total-credits');
  const certTotalPoints = document.getElementById('cert-total-points');
  const certCgpa = document.getElementById('cert-cgpa');
  const certDivision = document.getElementById('cert-division');
  const certTableBody = document.getElementById('cert-table-body');
  const certFootCredits = document.getElementById('cert-foot-credits');
  const certFootCgpa = document.getElementById('cert-foot-cgpa');
  const certFootPoints = document.getElementById('cert-foot-points');
  const certRefNo = document.getElementById('cert-ref-no');
  const certIssueDate = document.getElementById('cert-issue-date');

  // Open Modal & Populate Certificate
  btnPrint.addEventListener('click', () => {
    populateCertificateData();
    transcriptModal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // prevent bg scroll
  });

  // Open Modal & Populate Certificate
  btnPrint.addEventListener('click', () => {
    populateCertificateData();
    scrubEntities(document.getElementById('htbd-transcript-modal'));
    transcriptModal.style.display = 'block';
    document.body.style.overflow = 'hidden'; // prevent bg scroll
  });

  // Close Modal
  function closeModal() {
    transcriptModal.style.display = 'none';
    document.body.style.overflow = '';
  }
  btnCloseModal.addEventListener('click', closeModal);
  transcriptModal.addEventListener('click', (e) => {
    if (e.target === transcriptModal) closeModal();
  });

  // Live Input Sync
  modalInpName.addEventListener('input', () => {
    certStudentName.textContent = modalInpName.value.trim() || _bn('পরীক্ষার্থী (Examinee)');
    scrubEntities(certStudentName);
  });
  modalInpCollege.addEventListener('input', () => {
    certCollegeName.textContent = modalInpCollege.value.trim() || _bn('জাতীয় বিশ্ববিদ্যালয় অধিভুক্ত কলেজ');
    scrubEntities(certCollegeName);
  });
  modalInpSession.addEventListener('input', () => {
    certRegSession.textContent = modalInpSession.value.trim() || _bn('২০২০-২১ (নিয়মিত)');
    scrubEntities(certRegSession);
  });

  // Pure deterministic Bengali numeral and date converter
  function toBnDigits(num) {
    const bnDigits = ['০', '১', '২', '৩', '৪', '৫', '৬', '৭', '৮', '৯'];
    return String(num).replace(/[0-9]/g, d => _bn(bnDigits[d]));
  }

  function getBnDateString(date) {
    const bnMonths = ['জানুয়ারি', 'ফেব্রুয়ারি', 'মার্চ', 'এপ্রিল', 'মে', 'জুন', 'জুলাই', 'আগস্ট', 'সেপ্টেম্বর', 'অক্টোবর', 'নভেম্বর', 'ডিসেম্বর'];
    const day = toBnDigits(date.getDate());
    const month = _bn(bnMonths[date.getMonth()]);
    const year = toBnDigits(date.getFullYear());
    return _bn(day + ' ' + month + ', ' + year);
  }

  function populateCertificateData() {
    const now = new Date();
    const dateFormatted = getBnDateString(now);
    const randomRef = 'Ref: NU-' + now.getFullYear() + '-' + Math.floor(10000 + Math.random() * 90000);
    certRefNo.textContent = _bn(randomRef);
    certIssueDate.textContent = _bn('তারিখ: ' + dateFormatted);

    // Student identity
    certStudentName.textContent = modalInpName.value.trim() || _bn('পরীক্ষার্থী (Examinee)');
    certCollegeName.textContent = modalInpCollege.value.trim() || _bn('জাতীয় বিশ্ববিদ্যালয় অধিভুক্ত কলেজ');
    certRegSession.textContent = modalInpSession.value.trim() || _bn('২০২০-২১ (নিয়মিত)');

    // Degree Name
    let progName = _bn('স্নাতক (সম্মান) চার বছর');
    if (currentProgram === 'degree') progName = _bn('ডিগ্রি (পাস) তিন বছর');
    else if (currentProgram === 'masters') progName = _bn('মাস্টার্স রেগুলার / প্রিলিমিনারি');
    certProgramName.textContent = _bn(progName);

    // CGPA & Metrics
    const cgpa = parseFloat(dashCgpaVal.textContent) || 0;
    const totalCredits = dashTotalCredits.textContent;
    const totalPoints = dashTotalPoints.textContent;
    const divText = getDivisionText(cgpa, parseFloat(totalCredits) || 0);

    certTotalCredits.textContent = totalCredits;
    certTotalPoints.textContent = totalPoints;
    certCgpa.textContent = cgpa.toFixed(2);
    certDivision.textContent = _bn(divText);

    certFootCredits.textContent = totalCredits;
    certFootCgpa.textContent = cgpa.toFixed(2);
    certFootPoints.textContent = totalPoints;

    // Table Rows
    certTableBody.innerHTML = '';
    const yearLabels = {
      '1': { bn: _bn('১ম বর্ষ বার্ষিক পরীক্ষা'), en: '1st Year Final Examination' },
      '2': { bn: _bn('২য় বর্ষ বার্ষিক পরীক্ষা'), en: '2nd Year Final Examination' },
      '3': { bn: _bn('৩য় বর্ষ বার্ষিক পরীক্ষা'), en: '3rd Year Final Examination' },
      '4': { bn: _bn('৪র্থ বর্ষ বার্ষিক পরীক্ষা'), en: '4th Year Final Examination' }
    };

    if (currentMode === 'mode-year') {
      let rowIdx = 1;
      yearCards.forEach(card => {
        const yr = card.dataset.year;
        if (currentProgram === 'degree' && parseInt(yr) > 3) return;
        if (currentProgram === 'masters' && parseInt(yr) > 2) return;

        const rawGpa = card.querySelector('.htbd-yr-gpa').value.trim();
        const gpa = rawGpa !== '' ? parseFloat(rawGpa).toFixed(2) : '0.00';
        const cr = card.querySelector('.htbd-yr-credit').value || '32';
        const pts = (parseFloat(gpa) * parseFloat(cr)).toFixed(2);

        let lg = 'F';
        const pNum = parseFloat(gpa);
        if      (pNum >= 4.00) lg = 'A+';
        else if (pNum >= 3.75) lg = 'A';
        else if (pNum >= 3.50) lg = 'A-';
        else if (pNum >= 3.25) lg = 'B+';
        else if (pNum >= 3.00) lg = 'B';
        else if (pNum >= 2.75) lg = 'B-';
        else if (pNum >= 2.50) lg = 'C+';
        else if (pNum >= 2.25) lg = 'C';
        else if (pNum >= 2.00) lg = 'D';

        const yInfo = yearLabels[yr] || { bn: toBnDigits(yr) + 'ম বর্ষ বার্ষিক পরীক্ষা', en: yr + 'th Year Final Examination' };
        const examTitle = yInfo.bn + ' (' + yInfo.en + ')';
        const rowBnIdx = toBnDigits(rowIdx < 10 ? '0' + rowIdx : rowIdx);

        const tr = document.createElement('tr');
        tr.style.background = (rowIdx % 2 === 0) ? '#f8fafc' : '#ffffff';
        tr.innerHTML = `
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${rowBnIdx}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 8px; font-weight: 600;">${examTitle}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${cr}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700; color: #1e3a8a;">${lg}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700;">${gpa}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 600;">${pts}</td>
        `;
        certTableBody.appendChild(tr);
        rowIdx++;
      });
    } else {
      const rows = document.querySelectorAll('.htbd-course-row');
      let rowIdx = 1;
      rows.forEach(r => {
        const rowBnIdx = toBnDigits(rowIdx < 10 ? '0' + rowIdx : rowIdx);
        const name = r.querySelector('.c-name').value.trim() || ('কোর্স ' + rowBnIdx);
        const cr = r.querySelector('.c-credit').value;
        const gr = r.querySelector('.c-grade').value || '-';
        const rawGp = r.querySelector('.c-point').value.trim();
        const gp = rawGp !== '' ? parseFloat(rawGp).toFixed(2) : '0.00';
        const pts = (parseFloat(cr) * parseFloat(gp)).toFixed(2);

        const tr = document.createElement('tr');
        tr.style.background = (rowIdx % 2 === 0) ? '#f8fafc' : '#ffffff';
        tr.innerHTML = `
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${rowBnIdx}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 8px; font-weight: 600;">${name}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center;">${cr}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700; color: #1e3a8a;">${gr}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 700;">${gp}</td>
          <td style="border: 1px solid #cbd5e1; padding: 5px 6px; text-align: center; font-weight: 600;">${pts}</td>
        `;
        certTableBody.appendChild(tr);
        rowIdx++;
      });
    }
    scrubEntities(document.getElementById('htbd-transcript-modal'));
  }

  // ---------------------------------------------------------------------------
  // ISOLATED IFRAME PRINT ENGINE (GUARANTEED 1-PAGE A4 PDF, ZERO OVERFLOW)
  // ---------------------------------------------------------------------------
  btnTriggerPdfPrint.addEventListener('click', () => {
    const paper = document.getElementById('htbd-certificate-paper');
    if (!paper) return;
    scrubEntities(paper);

    // Create an invisible, isolated iframe
    const iframe = document.createElement('iframe');
    iframe.style.position = 'fixed';
    iframe.style.right = '0';
    iframe.style.bottom = '0';
    iframe.style.width = '0';
    iframe.style.height = '0';
    iframe.style.border = '0';
    iframe.style.visibility = 'hidden';
    document.body.appendChild(iframe);

    const doc = iframe.contentWindow.document;
    doc.open();
    doc.write(`<!DOCTYPE html>
<html lang="bn">
<head>
  <meta charset="utf-8">
  <title>NU_Academic_Transcript_2026</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+Bengali:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://fonts.maateen.me/solaiman-lipi/font.css">
  <style>
    @font-face {
      font-family: 'SolaimanLipi';
      font-display: swap;
      font-style: normal;
      font-weight: 400;
      src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-normal-v1.0.woff2') format('woff2');
    }
    @font-face {
      font-family: 'SolaimanLipi';
      font-display: swap;
      font-style: normal;
      font-weight: 700;
      src: url('https://fonts.maateen.me/solaiman-lipi/solaimanlipi-bold-v1.0.woff2') format('woff2');
    }
    @page {
      size: A4 portrait;
      margin: 8mm 10mm;
    }
    * {
      box-sizing: border-box;
      -webkit-print-color-adjust: exact !important;
      print-color-adjust: exact !important;
      font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
    }
    body {
      margin: 0;
      padding: 0;
      background: #ffffff !important;
      color: #0c2340 !important;
      font-family: 'SolaimanLipi', 'Noto Sans Bengali', Arial, sans-serif !important;
    }
    #htbd-certificate-paper {
      width: 100% !important;
      max-width: 100% !important;
      box-shadow: none !important;
      padding: 16px !important;
      border: 3px solid #1e3a8a !important;
      border-radius: 6px !important;
    }
    .htbd-cert-inner-frame {
      border: 1.5px solid #b45309 !important;
      padding: 14px 16px !important;
    }
    table {
      page-break-inside: avoid;
    }
  </style>
</head>
<body>
  ${paper.outerHTML}
</body>
</html>`);
    doc.close();

    // Trigger Print once styles and fonts are 100% loaded
    const triggerPrint = () => {
      iframe.contentWindow.focus();
      iframe.contentWindow.print();
      setTimeout(() => iframe.remove(), 4000);
    };

    if (doc.fonts && doc.fonts.ready) {
      doc.fonts.ready.then(() => {
        setTimeout(triggerPrint, 250);
      }).catch(() => {
        setTimeout(triggerPrint, 600);
      });
    } else {
      setTimeout(triggerPrint, 700);
    }
  });

  // Copy Summary
  document.getElementById('btn-copy-summary').addEventListener('click', () => {
    const cgpa = dashCgpaVal.textContent;
    const div = dashDivisionBadge.innerText;
    const cr = dashTotalCredits.textContent;
    const text = `জাতীয় বিশ্ববিদ্যালয় সিজিপিএ ক্যালকুলেটর রেজাল্ট:
• সিজিপিএ: ${cgpa} / 4.00
• মূল্যায়ন: ${div}
• মোট ক্রেডিট: ${cr}
হিসাব করুন: https://www.helptrickbd.com/p/nu-cgpa-calculator.html`;

    navigator.clipboard.writeText(text).then(() => {
      alert('রেজাল্ট সামারি কপি হয়েছে!');
    });
  });

  // ---------------------------------------------------------------------------
  // LOCALSTORAGE PERSISTENCE
  // ---------------------------------------------------------------------------
  function saveState() {
    const data = {
      program: currentProgram,
      years: []
    };
    yearCards.forEach(c => {
      data.years.push({
        gpa: c.querySelector('.htbd-yr-gpa').value,
        credit: c.querySelector('.htbd-yr-credit').value
      });
    });
    try {
      localStorage.setItem('htbd_nu_cgpa_data', JSON.stringify(data));
    } catch (e) {}
  }

  function loadState() {
    try {
      const raw = localStorage.getItem('htbd_nu_cgpa_data');
      if (raw) {
        const data = JSON.parse(raw);
        if (data.years && data.years.length) {
          data.years.forEach((item, i) => {
            if (yearCards[i]) {
              if (item.gpa) {
                yearCards[i].querySelector('.htbd-yr-gpa').value = item.gpa;
                yearCards[i].querySelector('.htbd-yr-range').value = item.gpa;
              }
              if (item.credit) {
                yearCards[i].querySelector('.htbd-yr-credit').value = item.credit;
              }
            }
          });
        }
      }
    } catch (e) {}
  }

  // Initial Boot
  // ---------------------------------------------------------------------------
  // APP TOOLBAR INTEGRATION (FULLSCREEN, PRINT & RESET)
  // ---------------------------------------------------------------------------
  const btnFullscreen = document.getElementById('ht-btn-fullscreen');
  const appWrapper = document.querySelector('.ht-app-core-wrapper');
  if (btnFullscreen && appWrapper) {
    btnFullscreen.addEventListener('click', () => {
      appWrapper.classList.toggle('is-fullscreen');
      document.body.classList.toggle('ht-fullscreen-active');
      const isFull = appWrapper.classList.contains('is-fullscreen');
      const textSpan = btnFullscreen.querySelector('.ht-btn-text');
      if (textSpan) textSpan.textContent = isFull ? 'স্বাভাবিক ভিউ' : 'ফুলস্ক্রিন ভিউ';
    });
  }

  const btnToolbarPrint = document.getElementById('ht-btn-toolbar-print');
  if (btnToolbarPrint && btnPrint) {
    btnToolbarPrint.addEventListener('click', () => {
      btnPrint.click();
    });
  }

  const btnToolbarReset = document.getElementById('ht-btn-toolbar-reset');
  if (btnToolbarReset && btnResetYear) {
    btnToolbarReset.addEventListener('click', () => {
      if (confirm('আপনি কি নিশ্চিত যে সকল হিসাব মুছে রিসেট করতে চান?')) {
        btnResetYear.click();
      }
    });
  }

  scrubEntities(document.getElementById('htbd-nu-cgpa-app'));
  scrubEntities(document.getElementById('htbd-transcript-modal'));
  loadState();
  if (btnResetCourses) btnResetCourses.click(); // load empty initial course rows
  createImpRow('কোর্স ০১', '', '');
  createImpRow('কোর্স ০২', '', '');
  calculateYearMode();
  calculateTargetMode();
  calculateImprovementMode();
  scrubEntities(document.getElementById('htbd-nu-cgpa-app'));
  scrubEntities(document.getElementById('htbd-transcript-modal'));

})();
