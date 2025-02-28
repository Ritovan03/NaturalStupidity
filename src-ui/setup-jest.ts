import '@angular/localize/init'
import { jest } from '@jest/globals'
import { setupZoneTestEnv } from 'jest-preset-angular/setup-env/zone'
import { TextDecoder, TextEncoder } from 'util'
if (process.env.NODE_ENV === 'test') {
  setupZoneTestEnv()
}
global.TextEncoder = TextEncoder
global.TextDecoder = TextDecoder

import { registerLocaleData } from '@angular/common'
import localeEnGb from '@angular/common/locales/en-GB'

registerLocaleData(localeEnGb)

/* global mocks for jsdom */
const mock = () => {
  let storage: { [key: string]: string } = {}
  return {
    getItem: (key: string) => (key in storage ? storage[key] : null),
    setItem: (key: string, value: string) => {
      if (value.length > 1000000) throw new Error('localStorage overflow')
      storage[key] = value || ''
    },
    removeItem: (key: string) => delete storage[key],
    clear: () => (storage = {}),
  }
}

Object.defineProperty(window, 'open', { value: jest.fn() })
Object.defineProperty(window, 'localStorage', { value: mock() })
Object.defineProperty(window, 'sessionStorage', { value: mock() })
Object.defineProperty(window, 'getComputedStyle', {
  value: () => ['-webkit-appearance'],
})
Object.defineProperty(navigator, 'clipboard', {
  value: {
    writeText: async () => {},
  },
})
Object.defineProperty(navigator, 'canShare', { value: () => true })
if (!navigator.share) {
  Object.defineProperty(navigator, 'share', { value: jest.fn() })
}
if (!URL.createObjectURL) {
  Object.defineProperty(window.URL, 'createObjectURL', { value: jest.fn() })
}
if (!URL.revokeObjectURL) {
  Object.defineProperty(window.URL, 'revokeObjectURL', { value: jest.fn() })
}
Object.defineProperty(window, 'ResizeObserver', { value: mock() })
Object.defineProperty(window, 'location', {
  configurable: true,
  value: { reload: jest.fn() },
})

HTMLCanvasElement.prototype.getContext = <
  typeof HTMLCanvasElement.prototype.getContext
>jest.fn()

// pdfjs
jest.mock('pdfjs-dist', () => ({
  getDocument: jest.fn(() => ({
    promise: Promise.resolve({ numPages: 3 }),
  })),
  GlobalWorkerOptions: { workerSrc: '' },
  VerbosityLevel: { ERRORS: 0 },
  globalThis: {
    pdfjsLib: {
      GlobalWorkerOptions: {
        workerSrc: '',
      },
    },
  },
}))
jest.mock('pdfjs-dist/web/pdf_viewer', () => ({}))
