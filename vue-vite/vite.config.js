import { defineConfig } from 'vite'

import vue from '@vitejs/plugin-vue'
import ssr from 'vite-plugin-ssr/plugin'
import legacy from '@vitejs/plugin-legacy'

// https://vitejs.dev/config/
// export default defineConfig({
//   plugins: [vue()]
// })


export default defineConfig({
  plugins: [
    vue(),
    ssr(),
    legacy({
      // for ie11
      targets: ["ie >= 11"],
      additionalLegacyPolyfills: ["regenerator-runtime/runtime"],
    }),
  ]
})

