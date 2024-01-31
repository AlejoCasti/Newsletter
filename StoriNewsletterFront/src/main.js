import { createApp } from 'vue';
import './assets/styles.css';
import App from './App.vue';
import { createPinia } from 'pinia';
import router from './router';
import PrimeVue from 'primevue/config';
import 'primevue/resources/themes/aura-light-green/theme.css'
import 'sweetalert2/src/sweetalert2.scss'

const app = createApp(App);
const pinia = createPinia();

app.use(pinia);
app.use(router);
app.use(PrimeVue);

app.mount('#app');
