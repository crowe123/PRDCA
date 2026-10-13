// Referral tracking: phone-link taps and referral form submissions go to /api/track,
// which keeps them for the private lead table on /dashboard/.
(function () {
  var city = document.body.getAttribute("data-city") || "";

  function send(event) {
    event.page = location.pathname;
    var body = JSON.stringify(event);
    try {
      if (navigator.sendBeacon && navigator.sendBeacon("/api/track", new Blob([body], { type: "application/json" }))) return;
    } catch (e) { /* fall through */ }
    fetch("/api/track", { method: "POST", body: body, headers: { "Content-Type": "application/json" }, keepalive: true })
      .catch(function () {});
  }

  document.addEventListener("click", function (e) {
    var link = e.target.closest && e.target.closest("a[data-track-call]");
    if (!link) return;
    send({ type: "call", city: city, target: link.getAttribute("data-track-call"),
           phone: link.getAttribute("href").replace("tel:", "") });
  });

  var form = document.getElementById("referral-form");
  if (!form) return;
  var status = form.querySelector(".form-status");
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    var button = form.querySelector("button[type=submit]");
    button.disabled = true;
    var data = new FormData(form);
    var select = form.elements.city;
    if (data.get("_gotcha")) { location.href = "/thanks/"; return; }
    var lead = {
      type: "form", page: location.pathname, city: select.options[select.selectedIndex].text,
      poolType: data.get("pool_type") || "", method: data.get("method") || "",
      name: data.get("name") || "", email: data.get("email") || "",
      contactPhone: data.get("phone") || "", notes: data.get("notes") || ""
    };
    // Save the lead to the site's own store and email it through Formspree;
    // the request counts as sent if either one succeeds.
    var saved = fetch("/api/track", { method: "POST", body: JSON.stringify(lead),
      headers: { "Content-Type": "application/json" } }).then(function (r) { return r.ok; }, function () { return false; });
    var mailed = fetch(form.action, { method: "POST", body: data, headers: { Accept: "application/json" } })
      .then(function (r) { return r.ok; }, function () { return false; });
    Promise.all([saved, mailed]).then(function (res) {
      if (res[0] || res[1]) { location.href = "/thanks/"; return; }
      button.disabled = false;
      status.hidden = false;
      status.textContent = "The request could not be sent. Please try again in a moment.";
    });
  });
})();
