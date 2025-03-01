const base_url = new URL(document.baseURI)

export const environment = {
  production: true,
  apiBaseUrl: document.baseURI + 'api/',
  apiVersion: '7',
  appTitle: 'Natural Stupidity',
  version: '0.0.1',
  webSocketHost: window.location.host,
  webSocketProtocol: window.location.protocol == 'https:' ? 'wss:' : 'ws:',
  webSocketBaseUrl: base_url.pathname + 'ws/',
}
