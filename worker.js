/**
 * Grand Turk Shore Excursion — Workers Assets entry.
 * www → apex (one hop); .html → extensionless (one hop); else static assets / 404.
 */
const APEX_HOST = 'grandturkshoreexcursion.com';

export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    const host = url.hostname.toLowerCase();

    // Permanent one-hop www → apex (preserve path + query)
    if (host === `www.${APEX_HOST}`) {
      const dest = new URL(url.toString());
      dest.hostname = APEX_HOST;
      dest.protocol = 'https:';
      return Response.redirect(dest.toString(), 301);
    }

    // Permanent one-hop .html → extensionless (preserve query)
    if (url.pathname.toLowerCase().endsWith('.html')) {
      let path = url.pathname.slice(0, -5);
      if (path.toLowerCase().endsWith('/index')) path = path.slice(0, -6);
      if (path === '' || path === '/index') path = '/';
      const dest = new URL(url.toString());
      dest.pathname = path || '/';
      return Response.redirect(dest.toString(), 301);
    }

    return env.ASSETS.fetch(request);
  },
};
