// Private dashboard: referrals, site tracker and contractor pipeline. Data comes from /api/dashboard.
(function () {
  var KEY_NAME = "prc-dashboard-key";
  var PIPELINE = ["To call", "No answer", "Verified", "Not offering pool removal", "Listed", "Rejected"];
  var ITEM = ["Open", "Done"];
  var state = { data: null, days: 30 };
  var $ = function (id) { return document.getElementById(id); };

  function esc(v) {
    return String(v == null ? "" : v).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function getKey() { try { return sessionStorage.getItem(KEY_NAME) || ""; } catch (e) { return ""; } }
  function setKey(k) { try { sessionStorage.setItem(KEY_NAME, k); } catch (e) {} }

  function api(method, body) {
    var opts = { method: method, headers: { "x-dashboard-key": getKey() } };
    if (body) { opts.body = JSON.stringify(body); opts.headers["Content-Type"] = "application/json"; }
    var url = "/api/dashboard" + (method === "GET" ? "?days=" + state.days : "");
    return fetch(url, opts).then(function (r) {
      if (r.status === 401) { showLogin("That key was not accepted."); throw new Error("401"); }
      if (!r.ok) throw new Error("HTTP " + r.status);
      return r.json();
    });
  }

  function showLogin(msg) {
    $("login").hidden = false; $("app").hidden = true;
    $("login-msg").textContent = msg || "";
  }

  function load() {
    $("loading").hidden = false;
    api("GET").then(function (d) {
      state.data = d; $("login").hidden = true; $("app").hidden = false; render();
    }).catch(function (e) { if (e.message !== "401") $("error").textContent = "Could not load data: " + e.message; })
      .finally(function () { $("loading").hidden = true; });
  }

  function countBy(list, fn) {
    var m = {};
    list.forEach(function (x) { var k = fn(x) || "Unknown"; m[k] = (m[k] || 0) + 1; });
    return Object.keys(m).map(function (k) { return [k, m[k]]; }).sort(function (a, b) { return b[1] - a[1]; });
  }

  function bars(rows, empty) {
    if (!rows.length) return '<p class="muted">' + empty + "</p>";
    var max = rows[0][1];
    return '<ul class="bars">' + rows.map(function (r) {
      return '<li><span class="bar-label">' + esc(r[0]) + '</span><span class="bar-track"><span class="bar-fill" style="width:' +
        Math.max(4, Math.round(r[1] / max * 100)) + '%"></span></span><span class="bar-value">' + r[1] + "</span></li>";
    }).join("") + "</ul>";
  }

  function statusSelect(id, options, current) {
    return '<select data-id="' + esc(id) + '">' + options.map(function (o) {
      return "<option" + (o === current ? " selected" : "") + ">" + esc(o) + "</option>";
    }).join("") + "</select>";
  }

  function render() {
    var d = state.data, ev = d.events || [], st = d.statuses || {};
    var siteName = d.siteName;
    var calls = ev.filter(function (e) { return e.type === "call"; });
    var forms = ev.filter(function (e) { return e.type === "form"; });
    var contractorCalls = calls.filter(function (e) { return e.target !== siteName; });

    // KPI tiles
    $("kpis").innerHTML = [
      [ev.length, "referrals in the last " + d.days + " days"],
      [forms.length, "contact form requests"],
      [contractorCalls.length, "taps on a contractor's number"],
      [calls.length - contractorCalls.length, "taps on the site's own number"],
    ].map(function (k) { return '<div class="kpi"><b>' + k[0] + "</b><span>" + k[1] + "</span></div>"; }).join("");

    $("by-contractor").innerHTML = bars(countBy(contractorCalls, function (e) { return e.target; }), "No contractor calls yet.");
    $("by-city").innerHTML = bars(countBy(ev, function (e) { return e.city || "Site-wide pages"; }), "No referrals yet.");
    $("forms-by-city").innerHTML = bars(countBy(forms, function (e) { return e.city; }), "No form requests yet.");

    var recent = ev.slice().sort(function (a, b) { return a.at < b.at ? 1 : -1; }).slice(0, 100);
    $("recent").innerHTML = recent.length ? recent.map(function (e) {
      var what = e.type === "form" ? "Form: " + [e.poolType, e.method].filter(Boolean).join(", ") : "Call: " + e.target + " " + e.phone;
      return "<tr><td>" + esc(new Date(e.at).toLocaleString()) + "</td><td>" + (e.type === "form" ? "Form" : "Phone") +
        "</td><td>" + esc(e.city) + "</td><td>" + esc(what) + "</td><td>" + esc(e.page) + "</td></tr>";
    }).join("") : '<tr><td colspan="5" class="muted">No referral events recorded yet.</td></tr>';

    // Site tracker
    $("cities").innerHTML = d.cities.map(function (c) {
      var ev30 = ev.filter(function (e) { return e.city === c.name; }).length;
      return "<tr><td><a href=\"/" + esc(c.slug) + '/" target="_blank" rel="noopener">' + esc(c.name) + "</a></td><td>" +
        esc(c.region) + "</td><td>" + c.wave + "</td><td>" + c.listed + "</td><td>" + c.held + "</td><td>" + esc(c.confidence) +
        "</td><td>" + c.words + (c.words < 1500 ? ' <span class="flag">short</span>' : c.words > 2000 ? ' <span class="flag">long</span>' : "") +
        "</td><td>" + ev30 + "</td></tr>";
    }).join("");
    $("site-summary").textContent = d.pages + " indexable pages · " + d.cities.length + " city pages · " +
      d.cities.reduce(function (n, c) { return n + c.listed; }, 0) + " contractor cards · built " + new Date(d.generated).toLocaleDateString();

    $("items").innerHTML = d.openItems.map(function (it, i) {
      var id = "item:" + i, cur = (st[id] && st[id].status) || "Open";
      return '<tr class="' + (cur === "Done" ? "done" : "") + '"><td>' + esc(it) + "</td><td>" + statusSelect(id, ITEM, cur) + "</td></tr>";
    }).join("");

    // Contractor pipeline
    var filter = $("pipe-filter").value;
    var rows = d.pipeline.filter(function (b) {
      var cur = (st["biz:" + b.business] && st["biz:" + b.business].status) || "To call";
      return !filter || cur === filter;
    });
    $("pipeline").innerHTML = rows.map(function (b) {
      var id = "biz:" + b.business, s = st[id] || {}, cur = s.status || "To call";
      return "<tr><td><strong>" + esc(b.business) + "</strong><br><span class=\"muted\">" + esc(b.reason) + "</span></td><td>" +
        (b.phone ? '<a href="tel:' + esc(b.phone.replace(/[^0-9+]/g, "")) + '">' + esc(b.phone) + "</a>" : "—") + "</td><td>" +
        esc(b.base_city) + "</td><td>" + esc(b.cities.join(", ")) + "</td><td>" + statusSelect(id, PIPELINE, cur) +
        '<input class="note" data-id="' + esc(id) + '" placeholder="Note" value="' + esc(s.note || "") + '"></td></tr>';
    }).join("");
    $("pipe-count").textContent = PIPELINE.map(function (p) {
      return p + ": " + d.pipeline.filter(function (b) { return ((st["biz:" + b.business] || {}).status || "To call") === p; }).length;
    }).join(" · ");
  }

  function save(id) {
    var sel = document.querySelector('select[data-id="' + CSS.escape(id) + '"]');
    var note = document.querySelector('input.note[data-id="' + CSS.escape(id) + '"]');
    api("POST", { id: id, status: sel.value, note: note ? note.value : "" }).then(function (saved) {
      state.data.statuses[id] = saved; render();
    }).catch(function (e) { $("error").textContent = "Save failed: " + e.message; });
  }

  document.addEventListener("change", function (e) {
    if (e.target.matches("select[data-id]") || e.target.matches("input.note")) save(e.target.getAttribute("data-id"));
    if (e.target.id === "days") { state.days = Number(e.target.value); load(); }
    if (e.target.id === "pipe-filter") render();
  });
  $("login-form").addEventListener("submit", function (e) {
    e.preventDefault(); setKey($("key").value.trim()); load();
  });
  $("logout").addEventListener("click", function () { setKey(""); showLogin(""); });
  $("refresh").addEventListener("click", load);

  if (getKey()) load(); else showLogin("");
})();
