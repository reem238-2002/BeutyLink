// يمكنك إضافة أي وظائف تفاعلية للأدمن هنا لاحقاً
console.log("Admin Dashboard جاهز للعمل!");



// ===============================
// Admin Dashboard - Blacklist System
// ===============================

document.addEventListener("DOMContentLoaded", () => {

    // ===============================
    // إضافة للقائمة السوداء
    // ===============================
    document.querySelectorAll(".blacklist-btn").forEach(btn => {
      btn.addEventListener("click", async function () {
  
        const id = this.getAttribute("data-id");
        const reason = prompt("سبب الحظر:");
  
        if (!reason) return;
  
        try {
          const res = await fetch(`/blacklist/add/${id}/`, {
            method: "POST",
            headers: {
              "Content-Type": "application/x-www-form-urlencoded",
              "X-CSRFToken": getCSRFToken()
            },
            body: `reason=${encodeURIComponent(reason)}`
          });
  
          const data = await res.json();
  
          showToast(data.message || "تم الحظر بنجاح", "success");
  
          // تحديث الواجهة بدون reload
          this.innerText = "تم الحظر 🚫";
          this.disabled = true;
  
        } catch (error) {
          showToast("حدث خطأ", "error");
        }
  
      });
    });
  
    // ===============================
    // إزالة من القائمة السوداء
    // ===============================
    document.querySelectorAll(".remove-blacklist-btn").forEach(btn => {
      btn.addEventListener("click", async function () {
  
        const id = this.getAttribute("data-id");
  
        if (!confirm("هل أنت متأكد من إزالة الحظر؟")) return;
  
        try {
          const res = await fetch(`/blacklist/remove/${id}/`);
          const data = await res.json();
  
          showToast(data.message || "تمت الإزالة", "success");
  
          // حذف العنصر من الصفحة مباشرة
          this.closest(".card")?.remove();
  
        } catch (error) {
          showToast("حدث خطأ", "error");
        }
  
      });
    });
  
  });
  
  
  // ===============================
  // CSRF TOKEN
  // ===============================
  function getCSRFToken() {
    return document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken'))
      ?.split('=')[1];
  }
  
  
  // ===============================
  // Toast Notification (بديل alert)
  // ===============================
  function showToast(message, type = "info") {
    let toast = document.querySelector(".toast");
  
    if (!toast) {
      toast = document.createElement("div");
      toast.className = "toast";
      document.body.appendChild(toast);
    }
  
    toast.innerText = message;
    toast.className = `toast show ${type}`;
  
    setTimeout(() => {
      toast.classList.remove("show");
    }, 3000);
  }






  function blacklistSalon(id){
    const reason = prompt("سبب الحظر:");
  
    if (!reason) return;
  
    fetch(`/blacklist/add/${id}/`, {
      method: "POST",
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
        "X-CSRFToken": getCSRFToken()
      },
      body: `reason=${encodeURIComponent(reason)}`
    })
    .then(res => res.json())
    .then(data => {
      alert(data.message);
      location.reload();
    });
  }
  
  
  // CSRF
  function getCSRFToken() {
    return document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken'))
      ?.split('=')[1];
  }