// taiwanustax.com:靜態資產 + 同源留資端點。
// /api/leads 透過 service binding 交給 taxagent Worker(驗證、蜜罐、寫入 R2 都在那邊,這裡不重複實作)。
export default {
  async fetch(request, env) {
    const url = new URL(request.url);

    if (url.hostname === "www.taiwanustax.com") {
      url.hostname = "taiwanustax.com";
      return Response.redirect(url.toString(), 301);
    }

    if (url.pathname === "/api/leads") {
      return env.TAXAGENT.fetch(request);
    }
    if (url.pathname.startsWith("/api/")) {
      return Response.json({ ok: false, error: "not found" }, { status: 404 });
    }

    return env.ASSETS.fetch(request);
  },
};
