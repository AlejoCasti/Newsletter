import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import pugPlugin from 'vite-plugin-pug';

export default defineConfig({
  plugins: [vue(), pugPlugin()],
  define: {
    global: {}
  }
})
