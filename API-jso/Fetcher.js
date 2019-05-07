export function Fetcher (options) {
    if (options.base) this.base = options.base;
  };
  
  Fetcher.prototype.fetch = function(input, init) {
    if (input instanceof Request) {
      return window.fetch(input, init);
    }
  
    let url = this.base ? new URL(input, this.base) : new URL(input);
  
    if (! init) init = {};
  
    if (! init.headers) {
      init.headers = new Headers();
    } else if ( !( init.headers instanceof Headers) ) {
      init.headers = new Headers(init.headers);
    }
  
    let is_get = ! init.method || init.method == 'GET' || init.method == 'HEAD';
  
    // shortcut for query or form data
    if (init.form) {
      let form;
      if (is_get) {
        form = url.searchParams;
      } else {
        if (init.body) {
          return Promise.reject(new Error('The form shortcut should not be used when a body is specified'));
        }
  
        form = new FormData();
        init.body = form;
  
        if (! init.headers.has('Content-Type')) {
          init.headers.set('Content-Type', 'application/x-www-form-urlencoded');
        }
      }
  
      // if not iterable, try to make it iterable with Object.entries
      let items = typeof init.form[Symbol.iterator] === 'function' ? init.form : Object.entries(init.form);
      items.forEach(([key, value]) => form.append(key, value));
  
      delete init.form;
  
    // shortcut for JSON
    } else if (init.json) {
      if (init.body) {
        return Promise.reject(new Error('The json shortcut should not be used when a body is specified'));
      }
  
      init.body = JSON.stringify(init.json);
      delete init.json;
  
      if (! init.headers.has('Content-Type')) {
        init.headers.set('Content-Type', 'application/json');
      }
    }
  
    return window.fetch(url.toString(), init);
  };
  
  export default Fetcher;