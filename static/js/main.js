
document.addEventListener("DOMContentLoaded", () => {
  // Toggle nav in mobile
  const nav = document.querySelector("header nav");
  const toggle = document.querySelector(".nav-toggle");
  if (toggle && nav) {
    toggle.addEventListener("click", () => {
      nav.classList.toggle("open");
    });
  }

  // Active nav item based on body data-page
  const currentPage = document.body.dataset.page;
  if (currentPage) {
    document.querySelectorAll(".nav-link").forEach(link => {
      const page = link.getAttribute("data-page");
      if (page === currentPage) {
        link.classList.add("active");
      } else {
        link.classList.remove("active");
      }
    });
  }

  // Simple fade-up animation on scroll
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in-view");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.15 });

  document.querySelectorAll(".fade-up").forEach(el => observer.observe(el));

  // Toast helper
  function showToast(title, message, timeout = 3500) {
    let toast = document.querySelector(".toast");
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "toast";
      toast.innerHTML = '<div class="toast-title"></div><div class="toast-message"></div>';
      document.body.appendChild(toast);
    }
    toast.querySelector(".toast-title").textContent = title;
    toast.querySelector(".toast-message").textContent = message;
    toast.classList.add("show");
    setTimeout(() => toast.classList.remove("show"), timeout);
  }

  // Fake salon data for listings and booking select
  const salonData = [
    {
      id: "golden-art",
      nameAr: "صالون جولدن آرت بيوتي",
      nameEn: "Golden Art Beauty Salon",
      areaAr: "حدة",
      areaEn: "Hadda",
      priceTier: "متوسط",
      rating: 4.8,
      servicesAr: ["مكياج عرائس", "تسريحات شعر", "بدكير ومنكير"],
      servicesEn: ["Bridal makeup", "Hair styling", "Manicure & Pedicure"]
    },
    {
      id: "queen-style",
      nameAr: "بيوتي لينك كوين ستايل",
      nameEn: "Beauty Link Queen Style",
      areaAr: "السبعين",
      areaEn: "Al-Sabeen",
      priceTier: "فاخر",
      rating: 4.9,
      servicesAr: ["مكياج خليجي", "صبغات شعر", "عناية بالبشرة"],
      servicesEn: ["Gulf makeup", "Hair coloring", "Skin care"]
    },
    {
      id: "elegance-lounge",
      nameAr: "إليغانس لونج",
      nameEn: "Elegance Lounge",
      areaAr: "شملان",
      areaEn: "Shamlan",
      priceTier: "اقتصادي",
      rating: 4.5,
      servicesAr: ["تصفيف شعر", "حواجب", "خيوط"],
      servicesEn: ["Hair styling", "Eyebrows", "Threading"]
    }
  ];

  const isArabic = document.documentElement.lang === "ar";

  // Populate salons grid if present
  const salonGrid = document.getElementById("salonGrid");
  if (salonGrid) {
    salonData.forEach(salon => {
      const card = document.createElement("a");
      const detailsPage = isArabic ? "salon-details.html" : "salon-details.html";
      card.href = detailsPage + "?id=" + salon.id;
      card.className = "salon-card fade-up";
      card.innerHTML = `
        <div class="salon-cover">
          <div class="salon-cover-label">${isArabic ? "صالون معتمد في بيوتي لينك" : "Verified on Beauty Link"}</div>
        </div>
        <div class="salon-card-title-row">
          <div class="salon-card-name">
            ${isArabic ? salon.nameAr : salon.nameEn}
          </div>
          <span class="badge-soft">${isArabic ? salon.areaAr : salon.areaEn}</span>
        </div>
        <div class="salon-card-meta">
          <span>${isArabic ? "فئة السعر:" : "Price tier:"} ${salon.priceTier}</span>
          <span class="rating-stars">★ ${salon.rating.toFixed(1)}</span>
        </div>
      `;
      salonGrid.appendChild(card);
    });
  }

  // Populate booking salon select + dynamic services
  const bookingSalonSelect = document.getElementById("bookingSalon");
  const bookingServiceSelect = document.getElementById("bookingService");
  if (bookingSalonSelect && bookingServiceSelect) {
    bookingSalonSelect.innerHTML = `<option value="">${isArabic ? "اختاري الكوافير" : "Select salon"}</option>`;
    salonData.forEach(salon => {
      const opt = document.createElement("option");
      opt.value = salon.id;
      opt.textContent = isArabic ? salon.nameAr : salon.nameEn;
      bookingSalonSelect.appendChild(opt);
    });

    bookingSalonSelect.addEventListener("change", () => {
      bookingServiceSelect.innerHTML = "";
      const selected = salonData.find(s => s.id === bookingSalonSelect.value);
      if (!selected) {
        bookingServiceSelect.innerHTML = `<option value="">${isArabic ? "اختاري الكوافير أولاً" : "Select salon first"}</option>`;
        return;
      }
      const label = isArabic ? "اختاري الخدمة" : "Select service";
      const placeholder = document.createElement("option");
      placeholder.value = "";
      placeholder.textContent = label;
      bookingServiceSelect.appendChild(placeholder);
      const services = isArabic ? selected.servicesAr : selected.servicesEn;
      services.forEach(svc => {
        const opt = document.createElement("option");
        opt.value = svc;
        opt.textContent = svc;
        bookingServiceSelect.appendChild(opt);
      });
    });
  }

  // Booking form handler
  const bookingForm = document.getElementById("bookingForm");
  if (bookingForm) {
    bookingForm.addEventListener("submit", e => {
      e.preventDefault();
      showToast(
        isArabic ? "تم استلام الحجز" : "Booking received",
        isArabic
          ? "تم إرسال طلب الحجز إلى الكوافير المختار، وسيتم التأكيد عبر الهاتف أو واتساب."
          : "Your booking request has been sent to the selected salon. It will be confirmed by phone or WhatsApp."
      );
      bookingForm.reset();
    });
  }

  // Fake login forms
  document.querySelectorAll("form[data-role='login']").forEach(form => {
    form.addEventListener("submit", e => {
      e.preventDefault();
      const role = form.dataset.type || "user";
      showToast(
        isArabic ? "تسجيل الدخول (واجهة فقط)" : "Login (UI only)",
        isArabic
          ? "هذا النموذج واجهة Front-End فقط. فريق الباك-إند سيقوم بربطه بقاعدة البيانات."
          : "This is a front-end UI only. Your backend team will connect it to the database."
      );
    });
  });

  // Fake save forms
  document.querySelectorAll("form[data-role='save']").forEach(form => {
    form.addEventListener("submit", e => {
      e.preventDefault();
      showToast(
        isArabic ? "تم حفظ التعديلات (واجهة)" : "Changes saved (UI)",
        isArabic
          ? "تم تنفيذ سلوك حفظ شكلي في الواجهة. الباك-إند سيكمل المنطق الفعلي."
          : "A visual save interaction has been triggered. Backend will handle real saving."
      );
    });
  });
});










